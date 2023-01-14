import json
import sys

class UnderCookedAdapter():
    def __init__(self, log_path):
        self.log_path = log_path
        self.output = []

    def test(self, output_path):
        # Setup
        self.setup_scores()
        self.setup_gamemap()
        # Test some turns
        for i in range(1, 501):
            self.process_turn(i)
        # Save output
        output_file = open(output_path, 'w')
        output_file.write(json.dumps({"log": self.output}))

    def process_turn(self, turn_num):
        turn = open(self.log_path + "/turn_{:0>4}.json".format(turn_num))
        turn = json.loads(turn.read())
        game_map = turn["game_map"]["game_map"]
        dispensers, ovens, items = self.find_items_and_states(game_map)
        # Update dispensers with items
        self.command(turn_num, "update_layer", ["stations", dispensers])
        # Update ovens with state

        # Update items on map

        # Update ingredients on map 

        # Update position and icon of cooks
        cooks = []
        clients = turn["clients"]
        cooks.append([clients[0]["cook"]["position"][1], clients[0]["cook"]["position"][0], "white_cook"])
        cooks.append([clients[1]["cook"]["position"][1], clients[1]["cook"]["position"][0], "white_cook"])
        self.command(turn_num, "set_layer", ["cooks", cooks])


    def setup_scores(self):
        clients = open(self.log_path + "/turn_0001.json")
        clients = json.loads(clients.read())
        clients = clients["clients"]
        self.command(0, "add_score", [0, clients[0]["team_name"] + ": ", 0, [500, 10]])
        self.command(0, "add_score", [1, clients[1]["team_name"] + ": ", 0, [500, 30]])

    def setup_gamemap(self):
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
        # Update the station layer with the list of station positions
        self.command(0, "set_layer", ["stations", stations])
        # Add the items layer
        self.command(0, "add_layer", ["items0", 2, width, height])
        # Add the cook layer and set inital cook positions found during station setup
        self.command(0, "add_layer", ["cooks", 10, width, height])
        self.command(0, "set_layer", ["cooks", cooks])

    def find_items_and_states(self, game_map):
        dispensers = []
        ovens = []
        items = []
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile["occupied_by"] is not None:
                    key = self.tile_key(tile["occupied_by"]["object_type"])
                    if key == "dispenser":
                        dispensers.append([x, y, self.dispenser_key(tile["occupied_by"])])
                    if key == "oven":
                        ovens.append([x, y, self.oven_key(tile["occupied_by"])])
        
        return (dispensers, ovens, items)



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
        if num == 12: return "roller"
        if num == 13: return "slicer"
        if num == 14: return "oven"
        if num == 15: return "bin"
        if num == 16: return "combiner"
        if num == 17: return "storage"
        if num == 18: return "delivery"
        if num == 19: return "saucer"
        return "NoAdapterTileKeyError"
    
    def item_key(self, item):
        pass

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
        if dispenser["item"] == None:
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
        adapter.test("graphical.json")
    elif (len(sys.argv) == 3):
        adapter = UnderCookedAdapter(sys.argv[1])
        adapter.test(sys.argv[2])
    elif (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        help()
    else:
        help()
    