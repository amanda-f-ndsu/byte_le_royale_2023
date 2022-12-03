# Bytiser Readme
- Visualiser with the goal of being able to use it for each year
- Currently implemented with pygame

## How to use
- Create a config.json
- Use bytiser.run_log(log_path) to visualise a json log

## Config
- Note, this code block is commented
- JSON does not allow comments so remove all //comments before copying 
{
    // ALL VALUES ARE REQUIRED
    // frames per second
    "fps": 12,
    // tile size of each sprite in pixels
    "tile_size": [8, 8],
    // spacing between each sprite in pixels
    "tile_spacing": [1, 1],
    // spacing around in the tilemap in pixels
    "border_spacing": [0, 0],
    // screen width in pixels
    "screen_width": 1366,
    // screen height in pixels
    "screen_height": 768,
    // path to tile_map
    "tile_map": "./tilemap.png",
    // scale multiplier for sprites in visualiser
    "scale": 4,
    // fallback sprite in tilemap in case a key is not defined [x, y] (0 indexed)
    "fallback": [0, 6],
    // Dictionary of keys to define where each sprite is (empty dictionary is required even if no keys)
    "keys": {
        // NOT REQUIRED
        // Dictionary can be empty, examples given [x, y] (0 indexed)
        // The first sprite would be 0,0 and then the second to the right would be 1,0 etc
        "player": [4, 0],
        "enemy": [11, 0],
        "floor": [1, 1],
        "top_wall": [1, 0],
        "top_left_corner": [0, 0],
        "top_right_corner": [3, 0],
        "bottom_left_corner": [0, 2],
        "bottom_right_corner": [3, 2],
        "left wall": [0, 1],
        "right_wall": [3, 0]
    }
}