from PIL import Image
import os

inputFolder = input("Path to input folder: ")
outputFolder = input("Path to output folder: ")

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

for filename in os.listdir(inputFolder):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(inputFolder, filename)).convert("RGBA")
        data = img.getdata()
        newData = []
        for item in data:
            if item[0] == item[1] == item[2]:
                newData.append((item[0], item[1], item[2], 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(os.path.join(outputFolder, filename), "PNG")
