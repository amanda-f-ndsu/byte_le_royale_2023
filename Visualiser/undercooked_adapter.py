import json
import sys

class UnderCookedAdapter():
    def __init__(self, log_path):
        log_file = open(log_path)
        self.logs = json.loads(log_file.read())
    
    def print_logs(self):
        print(self.logs)

    def test_first_tick(self, output_path):
        self.output = []
        # Scores
        self.command(1, "add_score", [1, self.logs["1"]["clients"][0]["team_name"], 0, [400, 10]])
        self.command(1, "add_score", [2, self.logs["1"]["clients"][1]["team_name"], 0, [400, 30]])
        # Main floor
        height = len(self.logs["1"]["game_map"]["game_map"])
        width = len(self.logs["1"]["game_map"]["game_map"][0])
        self.command(1, "add_layer", ["floor", 0, width, height])
        self.command(1, "set_layer", ["floor", [[None, None, "floor"]]])
        output_file = open(output_path, 'w')
        output_file.write(json.dumps({"log": self.output}))
        
    def command(self, turn, command, value):
        self.output.append(self.create_command(turn, command, value))

    def create_command(self, turn, command, value):
        return {
            "turn": turn,
            "command": command,
            "value": value
        }
    
    def tile_key(self, num, occupied):
        if num == 0: return "null"
        if num == 10 and occupied is None: return "floor"
        if num == 10 and occupied == 2: return "counter"




def help():
    print("COMMAND USAGE for PYTHON 3")
    print("python ./adapter.py turnLogsFile outputFile")
    print("python ./adapter.py --help")
    print("Zero arguments will default to ./turn_logs.json")

if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        adapter = UnderCookedAdapter("turn_logs.json")
        adapter.test_first_tick("graphical.json")
    elif (len(sys.argv) == 3):
        adapter = UnderCookedAdapter(sys.argv[1])
    elif (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        help()
    else:
        help()
    