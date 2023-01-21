import os
import sys
from PIL import Image
import math

# Can create a spritesheet by searching through a directory for png files
class SpritesheetGenerator:
    MAX_COLUMNS = 10

    def findAllPng(self, directory):
        output = []
        directory_list = os.listdir(directory)
        for x in directory_list:
            if os.path.isfile(directory + "/" + x):
                if(x.endswith(".png")):
                    output.append(directory + "/" + x)
            else:
                output.extend(self.findAllPng(directory + "/" + x))
        return output
    
    def getSize(self, path):
        return Image.open(path).size

    def getBestSquare(self, length):
        #Make better later using MAX_COLUMNS of like 64
        rows = math.ceil(length / SpritesheetGenerator.MAX_COLUMNS)
        return (SpritesheetGenerator.MAX_COLUMNS, rows)

    def createSpritesheet(self, files, size, outputPath):
        columns, rows = self.getBestSquare(len(files))
        x = 0
        y = 0
        background = Image.new("RGBA", (size*columns, size*rows), (0,0,0,0))
        for f in files:
            img = Image.open(f)
            offset = (size*x, size*y)
            background.paste(img, offset)
            x += 1
            if(x >= columns):
                x = 0
                y += 1
            if (y >= rows):
                print("ERROR: Y larger than rows at " + f)
        background.save(outputPath)            

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sg = SpritesheetGenerator()
        files = sg.findAllPng(sys.argv[1])
        sg.createSpritesheet(files, 32, sys.argv[2])
    else:
        print("Usage: python createSpritesheet.py DirectoryToSearch outputFile")