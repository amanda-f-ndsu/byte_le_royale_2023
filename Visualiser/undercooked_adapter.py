import json
import sys

class UnderCookedAdapter():
    def __init__(self, log_path):
        self.log_path = log_path
        self.output = []

    def test(self, output_path):
        self.setup_scores()
        self.setup_gamemap()
        output_file = open(output_path, 'w')
        output_file.write(json.dumps({"log": self.output}))

    def setup_scores(self):
        pass
        #self.command(1, "add_score", [1, self.logs["1"]["clients"][0]["team_name"], 0, [400, 10]])
        #self.command(1, "add_score", [2, self.logs["1"]["clients"][1]["team_name"], 0, [400, 30]])

    def setup_gamemap(self):
        # Load just the gamemap from game_map.json
        game_map = open(self.log_path + "/game_map.json")
        game_map = json.loads(game_map.read())
        game_map = game_map["game_map"]["game_map"]
        # Find the length and width of the gamemap
        height = len(game_map)
        width = len(game_map[0])
        # Add and setup the floor layer
        self.command(1, "add_layer", ["floor", 0, width, height])
        self.command(1, "set_layer", ["floor", [[None, None, "floor"]]])
        # Add and setup the station layer
        self.command(1, "add_layer", ["stations", 1, width, height])
        stations = []
        # Create the list of x,y,key for the set_layer command
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile["occupied_by"] is not None:
                    key = self.tile_key(tile["occupied_by"]["object_type"])
                    if key != "cook":
                        stations.append([x, y, key])
        # Update the station layer with the list of station positions
        self.command(1, "set_layer", ["stations", stations])

        
        
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
        if num == 13: return "cutter"
        if num == 14: return "oven"
        if num == 15: return "bin"
        if num == 16: return "combiner"
        if num == 17: return "storage"
        if num == 18: return "delivery"
        if num == 19: return "sauce"
        return "NoAdapterTileKeyError"




def help():
    print("COMMAND USAGE for PYTHON 3")
    print("python ./adapter.py turnLogsFile outputFile")
    print("python ./adapter.py --help")
    print("Zero arguments will default to ./turn_logs.json")

if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        adapter = UnderCookedAdapter("./logs")
        adapter.test("graphical.json")
    elif (len(sys.argv) == 3):
        adapter = UnderCookedAdapter(sys.argv[1])
    elif (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        help()
    else:
        help()
    