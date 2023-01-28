import json
import sys

class UnderCookedAdapter():
    def __init__(self, log_path):
        self.log_path = log_path
        self.output = []

    def run(self, output_path):
        # Setup
        self.setup_scores()
        self.setup_gamemap()
        # Run turns 1 to 500
        for i in range(1, 501):
            self.process_turn(i)
        # Save output
        output_file = open(output_path, 'w')
        output_file.write(json.dumps({"log": self.output}))

    def process_turn(self, turn_num):
        turn = open(self.log_path + "/turn_{:0>4}.json".format(turn_num))
        turn = json.loads(turn.read())
        game_map = turn["game_map"]["game_map"]
        dispensers, ovens, items, held, ingOne, ingTwo, ingThree, wet_tiles, infested, scores = self.find_items_and_states(game_map, turn["clients"])
        # Update dispensers with items
        self.command(turn_num, "update_layer", ["stations", dispensers])
        # Update ovens with state
        self.command(turn_num, "update_layer", ["stations", ovens])
        # Update items on map
        self.command(turn_num, "set_layer", ["items", items])
        # Update ingredients on map 
        self.command(turn_num, "set_layer", ["ing_1", ingOne])
        self.command(turn_num, "set_layer", ["ing_2", ingTwo])
        self.command(turn_num, "set_layer", ["ing_3", ingThree])
        # Update position and icon of cooks
        cooks = []
        clients = turn["clients"]
        held_one = "_held" if clients[0]["cook"]["held_item"] != None else ""
        held_two = "_held" if clients[1]["cook"]["held_item"] != None else ""
        cooks.append([clients[0]["cook"]["position"][1], clients[0]["cook"]["position"][0], self.check_cook_skin(clients[0]) + held_one])
        cooks.append([clients[1]["cook"]["position"][1], clients[1]["cook"]["position"][0], self.check_cook_skin(clients[1]) + held_two])
        self.command(turn_num, "set_layer", ["cooks", cooks])
        self.command(turn_num, "set_layer", ["held", held])
        # Update wet tiles
        self.command(turn_num, "set_layer", ["water", wet_tiles])
        self.command(turn_num, "set_layer", ["infested", infested])
        # Update scores
        self.command(turn_num, "set_score", [0, clients[0]["team_name"] + ": ", scores[0], [500, 10]])
        self.command(turn_num, "set_score", [1, clients[1]["team_name"] + ": ", scores[1], [500, 30]])


    def setup_scores(self):
        clients = open(self.log_path + "/turn_0001.json")
        clients = json.loads(clients.read())
        clients = clients["clients"]
        self.command(0, "add_score", [0, clients[0]["team_name"] + ": ", 0, [500, 10]])
        self.command(0, "add_score", [1, clients[1]["team_name"] + ": ", 0, [500, 30]])

    def setup_gamemap(self):
        # Load the clients from turn 1
        clients = open(self.log_path + "/turn_0001.json")
        clients = json.loads(clients.read())
        clients = clients["clients"]
        # Load just the gamemap from game_map.json
        game_map = open(self.log_path + "/game_map.json")
        game_map = json.loads(game_map.read())
        game_map = game_map["game_map"]["game_map"]
        # Find the length and width of the gamemap
        height = len(game_map)
        width = len(game_map[0])
        # Add and setup the floor layer
        self.command(0, "add_layer", ["floor", 0, width, height])
        self.command(0, "set_layer", ["floor", [[None, None, "floor"]]])
        # Add and setup the station layer
        self.command(0, "add_layer", ["stations", 1, width, height])
        stations = []
        cooks = [] # Used to keep track of cooks when scanning all station tiles for later
        # Create the list of x,y,key for the set_layer command
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile["occupied_by"] is not None:
                    key = self.tile_key(tile["occupied_by"]["object_type"])
                    # The only non station on the game_map at the start is the two cooks
                    # Keep track of where the cooks are so we can initalize their position later
                    if key != "cook":
                        if key == "oven":
                            stations.append([x, y, "oven_empty"])
                        else:
                            stations.append([x, y, key])
                    else:
                        cooks.append([x, y, "white_cook"])
        # Add cooks
        cooks.append([3, 3, self.check_cook_skin(clients[0])])
        cooks.append([9, 3, self.check_cook_skin(clients[1])])
        # Update the station layer with the list of station positions
        self.command(0, "set_layer", ["stations", stations])
        # Add the items layer
        self.command(0, "add_layer", ["items", 2, width, height])
        # Add the cook layer and set inital cook positions found during station setup
        self.command(0, "add_layer", ["cooks", 10, width, height])
        self.command(0, "set_layer", ["cooks", cooks])
        # Add held layer
        self.command(0, "add_layer", ["held", 12, width, height])
        # Add ingredient layers
        self.command(0, "add_layer", ["ing_1", 13, width, height])
        self.command(0, "add_layer", ["ing_2", 14, width, height])
        self.command(0, "add_layer", ["ing_3", 15, width, height])
        # Add wet tiles layer
        self.command(0, "add_layer", ["water", 20, width, height])
        # Add infected tiles layer
        self.command(0, "add_layer", ["infested", 21, width, height])

    def find_items_and_states(self, game_map, clients):
        dispensers = []
        ovens = []
        items = []
        held = []
        ingOne = []
        ingTwo = []
        ingThree = []
        wet_tiles = []
        infested = []
        scores = []
        # Go through map and look at tiles
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                # Check for wet tile
                if tile["is_wet_tile"]:
                    wet_tiles.append([x, y, "water"])
                # Check for stations
                if tile["occupied_by"] is not None:
                    # Check if infested
                    if "is_infested" in tile["occupied_by"]:
                        if tile["occupied_by"]["is_infested"]:
                            infested.append([x, y, "infested"])
                    # Get key and update stations
                    key = self.tile_key(tile["occupied_by"]["object_type"])
                    if key == "dispenser":
                        dispensers.append([x, y, self.dispenser_key(tile["occupied_by"])])
                    elif key == "oven":
                        ovens.append([x, y, self.oven_key(tile["occupied_by"])])
                    # Check if item and not being held by cook
                    elif key != "cook" and "item" in tile["occupied_by"] and tile["occupied_by"]["item"] != None:
                        # Check if topping
                        if tile["occupied_by"]["item"]["object_type"] == 9:
                            items.append([x, y, self.item_key(tile["occupied_by"]["item"], False)])
                        # If a pizza, add pizza and ingredients
                        elif tile["occupied_by"]["item"]["object_type"] == 11:
                            item = tile["occupied_by"]["item"]
                            items.append([x, y, self.item_key(item, False)])
                            for i, t in enumerate(item["toppings"]):
                                if i == 0:
                                    continue
                                elif i == 1:
                                    ingOne.append([x, y, self.ingredient_key(t, False, 1)])
                                elif i == 2:
                                    ingTwo.append([x, y, self.ingredient_key(t, False, 2)])
                                elif i == 3:
                                    ingThree.append([x, y, self.ingredient_key(t, False, 3)])

        # Check held items in cooks and also grab scores
        for client in clients:
            cook = client["cook"]
            scores.append(cook["score"])
            if cook["held_item"] != None:
                item = cook["held_item"]
                held.append([cook["position"][1], cook["position"][0], self.item_key(item, True)])
                # If a pizza then also add ingredients
                if item["object_type"] == 11:
                    # Go through all toppings
                    for i, t in enumerate(item["toppings"]):
                        # Skip cheese
                        if i == 0:
                            continue
                        # Add the ingredient key (slightly different than topping keys)
                        elif i == 1:
                            ingOne.append([cook["position"][1], cook["position"][0], self.ingredient_key(t, True, 1)])
                        elif i == 2:
                            ingTwo.append([cook["position"][1], cook["position"][0], self.ingredient_key(t, True, 2)])
                        elif i == 3:
                            ingThree.append([cook["position"][1], cook["position"][0], self.ingredient_key(t, True, 3)])

        return (dispensers, ovens, items, held, ingOne, ingTwo, ingThree, wet_tiles, infested, scores)



    def command(self, turn, command, value):
        self.output.append(self.create_command(turn, command, value))

    def create_command(self, turn, command, value):
        return {
            "turn": turn,
            "command": command,
            "value": value
        }
    
    def tile_key(self, num):
        if num == 0: return "null"
        if num == 2: return "counter"
        if num == 6: return "dispenser"
        if num == 8: return "cook"
        if num == 11: return "pizza"
        if num == 12: return "roller"
        if num == 13: return "slicer"
        if num == 14: return "oven"
        if num == 15: return "bin"
        if num == 16: return "combiner"
        if num == 17: return "storage"
        if num == 18: return "delivery"
        if num == 19: return "saucer"
        return "NoAdapterTileKeyError"
    
    def item_key(self, item, is_held):
        prefix = "held_" if is_held else "item_"
        # Check if topping 
        if item["object_type"] == 9:
            main = self.topping_key(item)
        # Check if pizza
        elif item["object_type"] == 11:
            main = self.pizza_key(item)
        # Item enum?
        elif item["object_type"] == 5:
            print("Item?: " + str(item))
            main = "none"
        else:
            main = "none"
        
        # Check if sliced
        if "is_cut" in item:
            suffix = "_sliced" if item["is_cut"] else ""
        else:
            suffix = ""

        return prefix + main + suffix

    def ingredient_key(self, item, is_held, num):
        output = self.item_key(item, is_held)
        output = output.replace("_sliced", "")
        output += "_" + str(num)
        return output


    def pizza_key(self, pizza):
        toppings = pizza["toppings"]
        if pizza["state"] == 1:
            return "pizza_rolled"
        elif pizza["state"] == 2:
            if len(toppings) >= 1 and self.topping_key(toppings[0]) == "cheese":
                return "pizza_cheesed"
            else:
                return "pizza_sauced"
        elif pizza["state"] == 3:
            return "pizza_baked"
        else:
            return "pizza"

    def check_cook_skin(self, client):
        skin = client["cook_skin"]
        if skin == None:
            return "white_cook"
        elif skin == "white":
            return "white_cook"
        elif skin == "amanda":
            return "amanda_cook"
        elif skin == "mitchell":
            return "mitchell_cook"
        elif skin == "purple":
            return "purple_cook"
        elif skin == "jean":
            return "jean_cook"
        elif skin == "red":
            return "red_cook"
        elif skin == "blue":
            return "blue_cook"
        elif skin == "yellow":
            return "yellow_cook"
        elif skin == "john":
            return "john_cook"
        elif skin == "green":
            return "green_cook"
        elif skin == "brown":
            return "brown_cook"
        elif skin == "techno":
            return "techno_cook"
        else:
            return "white_cook"
        

    def topping_key(self, item):
        num = item["topping_type"]
        if num == 0:
            main = "none"
        elif num == 1:
            main = "dough"
        elif num == 2:
            main = "cheese"
        elif num == 3:
            main = "pepperoni"
        elif num == 4:
            main = "sausage"
        elif num == 5:
            main = "ham"
        elif num == 6:
            main = "mushroom"
        elif num == 7:
            main = "pepper"
        elif num == 8:
            main = "chicken"
        elif num == 9:
            main = "olive"
        elif num == 10:
            main = "anchovy"
        return main

    def oven_key(self, oven):
        if oven["is_powered"] == False:
            return "oven_off"
        elif oven["is_active"] == True:
            return "oven_baking"
        elif oven["timer"] <= 0:
            return "oven_finished"
        else:
            return "oven_empty"

    def dispenser_key(self, dispenser):
        if "item" not in dispenser or not dispenser["item"]:
            return "dispenser"
        else:
            num = dispenser["item"]["topping_type"]
            if num == 0:
                return "dispenser"
            elif num == 1:
                return "dispenser_dough"
            elif num == 2:
                return "dispenser_cheese"
            elif num == 3:
                return "dispenser_pepperoni"
            elif num == 4:
                return "dispenser_sausage"
            elif num == 5:
                return "dispenser_ham"
            elif num == 6:
                return "dispenser_mushroom"
            elif num == 7:
                return "dispenser_pepper"
            elif num == 8:
                return "dispenser_chicken"
            elif num == 9:
                return "dispenser_olive"
            elif num == 10:
                return "dispenser_anchovy"




def help():
    print("COMMAND USAGE for PYTHON 3")
    print("python ./adapter.py turnLogsFile outputFile")
    print("python ./adapter.py --help")
    print("Zero arguments will default to using ./logs/ and outputing to ./graphical.json")

if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        adapter = UnderCookedAdapter("./logs")
        adapter.run("graphical.json")
    elif (len(sys.argv) == 3):
        adapter = UnderCookedAdapter(sys.argv[1])
        adapter.run(sys.argv[2])
    elif (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        help()
    else:
        help()
    