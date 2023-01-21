# Bytiser Readme
- Visualiser with the goal of being able to use it for each year
- Currently implemented with pygame

# Command Line Controls
## First adapt the logs into a graphical json
- python undercooked_adapter.py logsFolder outputFile
## Then run the bytiser to show the graphical json
- python bytiser.py config.json inputFromAdapter.json
- Both bytiser and undercooked_adapter can be passed --help for a help page

## How to use
- Create a config.json
- Use bytiser.run_log(log_path) to visualise a json graphical log

## Graphical Logs
- JSON array of commands
- Each command consists of
    - turn: int
        - Used to track which turn this command is executed as the commands are stored in an array
        - All setup commands would be turn 0 for instance
    - command: string
    - value
## Config
- Note, this code block is commented
- JSON does not allow comments so remove all //comments after copying 
{
    // ALL VALUES ARE REQUIRED
    // frames per second
    "fps": 12,
    // use byteiser.py --fonts to list system fonts
    "font": "arial",
    // font size for score display
    "font_size": 20,
    // font color for score display in rgb
    "font_color": [0, 255, 0],
    // Width of window in pixels
    "screen_width": 1366,
    // Height of window in pixels
    "screen_height": 768,
    // Global tile size to scale all sprites to in pixels (usually your largest sprite size)
    // All tile sizes must be square at this time(same x and y)
    // This adjustment is made bc all sprites are on a grid of the same size, different sized grids are not supported at this time
    "global_tile_size": [8, 8],
    // Scale multiplier to change global_tile_size to something bigger
    "scale": 4,
    // Fallback sprite in tilemap in case a key is not defined [x, y] (0 indexed)
    "fallback": ["original", 0, 6],
    // Dictionary of keys to define where each tile_map is and the properties (empty dictionary is required even if no keys)
    "tile_maps": {
        // CAN BE EMPTY
        "original": {
            // ALL properties are required
            // Path to image
            "source": "./tilemap.png",
            // Size of each tile
            "tile_size": [8, 8],
            // Any spacing between each tile in pixels
            "tile_spacing": [1, 1],
            // Any spacing between the tilemap and image edge in pixels
            "border_spacing": [0, 0]
        },
        "letters": {
            "source": "./tilemapletters.png",
            "tile_size": [8, 8],
            "tile_spacing": [1, 1],
            "border_spacing": [0, 0]
        },
        "2by2": {
            "source": "./tilemaptwobytwo.png",
            "tile_size": [2, 2],
            "tile_spacing": [1, 1],
            "border_spacing": [1, 1]
        }
    },
    // Dictionary of keys to define where each sprite is (empty dictionary is required even if no keys)
    "keys": {
        // CAN BE EMPTY
        // When adding a sprite, refer to the string key, the visualizer handles croping the sprite out of the tilemap
        // The parameters are ["tilemap_key", x_pos, y_pos]
        // The x and y pos are just what sprite is referred to
        // The first sprite would be 0,0 and then the second to the right would be 1,0 etc
        "cook": ["letters", 4, 0],
        "floor": ["original", 1, 1],
        "counter": ["2by2", 0, 0],
        "dispenser": ["letters", 0, 1],
        "roller": ["letters", 0, 2],
        "cutter": ["letters", 3, 0],
        "oven": ["letters", 0, 1],
        "bin": ["letters", 2, 2],
        "combiner": ["letters", 2, 1],
        "storage": ["letters", 3, 1],
        "delivery": ["letters", 0, 2],
        "sauce": ["letters", 1, 2],
        "water": ["2by2", 2, 0]
    }
}

## Commands
### add_layer
Adds a layer with the name and z_index, layers are drawn in the order of low to high z_index, width and height are in number of tiles
"command": "add_layer"
"value": ["name", z_index, width, height]
### set_layer
Will clear and then write over the layer with new values, a [null, null] can be optionally included as a default sprite, otherwise will be transparent
Only one default sprite can be included in each set_layer command
"command": "set_layer"
"value": ["name", [
    [null, null, default_key],
    [x, y, key]
]]
### update_layer
Same as set_layer command but does not clear the layer before drawing
"command": "update_layer"
"value": ["name", [
    [null, null, default_key],
    [x, y, key]
]]
### add_score
Will add a score object, give it an id, text, and pixel x and y position
Same as set_layer command but does not clear the layer before drawing
"command": "add_score"
"value": [num_id, "Display Text", inital_value_number, [x, y]]
### set_score
Will set a scores properties, anything left as null will not be changed
If the id is null then all score objects will update
"command": "set_score"
"value": [num_id, "Display Text", [x, y]] 
### remove_score
Will remove a score object and clear it from the screen
If the id is null then all score objects will update
"command": "set_score"
"value": [num_id, "Display Text", [x, y]]

# To Do
- Change to different cook sprites (holding is already done)
- Test infestation and water tiles
## Visualiser/Art Polish
- Gif optimization
- Seperate save GIF as small and as full
- File chooser
- Main menu
- Buttons for pause, play, exit
- Slider for faster, slower
- Game End Screen
    - End game command that uses scores
- Walking animations
## Adapter
- Now that the visualiser is mostly done and gamelogs have been generated for us, we can work on a adapter
- The adapter uses a game log and turns it into a log of graphical commands 
- The visualiser uses the graphical commands which means only the adapter needs to be rewritten every year