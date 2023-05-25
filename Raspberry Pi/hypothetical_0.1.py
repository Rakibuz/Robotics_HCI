from array import *
import os
from PIL import Image

Buttons=[0x300fd40bf,0x300fdc03f,0x300fd20df,0x300fda05f,0x300fd609f,0x300fde01f,0x300fd10ef,0x300fd906f,0x300fd50af,0x300fd30cf,0x300fdb24d,0x300fd728d,0x300fdf20d,0x300fd8877,0x300fd48b7]
ButtonsNames=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Zero","MENU","TITLE","L/R","Left_key","Right_key"]

distantToFolderMappings = {
    12: "C:/Users/rakib/OneDrive/Desktop/Optoshi/12 Feet",
    10: "C:/Users/rakib/OneDrive/Desktop/Optoshi/10 Feet",
    8: "C:/Users/rakib/OneDrive/Desktop/Optoshi/8 Feet"
}
menuMapping = {
    "one": "contrast",
    "two": "a",
}

def convertHex(binaryValue):
	tmpB2 =int(str(binaryValue),2)
	return hex(tmpB2)

 
class Folder:
    images = []
    name = ""
    currentIndex = 0
    def __init__(self, name, distance):
        distancePath = distantToFolderMappings[distance]
        actualFolderPath = distancePath+"/"+name
        folderImages = self.get_files_in_directory(actualFolderPath)
        self.images = [file for file in folderImages if file.endswith(".png") or file.endswith(".jpg")]
        self.name = name
        self.currentIndex = 0
        #print(self.images)
    def openImage(self):
        img = Image.open(self.images[self.currentIndex])
        img.show()
    def moveIndexToLeft(self):
         if self.currentIndex-1<0:
            self.currentIndex = len(self.images)-1
         else:
            self.currentIndex = self.currentIndex-1
         print("Processing done")
    def moveIndexToRight(self):
         if self.currentIndex+1<len(self.images):
            self.currentIndex = self.currentIndex + 1
         else:
            self.currentIndex = 0

    def processIrSignal(self, signal):
        print(signal)
        print(self.name)
        if signal == "Left":
           self.moveIndexToLeft()
           print(signal + " Pressed on " + self.name)
        elif signal == "Right":
            self.moveIndexToRight()
            print(signal + " Pressed on " + self.name)
        elif signal == self.findKey(menuMapping, self.name):
            print("Equal")
            self.moveIndexToRight()
        else:
            print("Command not found")
        print(self.currentIndex)
        self.openImage()

   


    def getImagePath(self, distance):
        return distantToFolderMappings[distance]+self.name
    def get_files_in_directory(self, directory):
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    def findKey(self, dictionary, value):
        for dict_key, dict_value in dictionary.items():
            if dict_value == value:
                return dict_key
        return None


    
currentFolder = None

def process_signal(distance, value):
    selButton = value
    global currentFolder
    if currentFolder is not None:
        currentFolder.processIrSignal(selButton)
         
    else:
        if value in menuMapping:
            currentFolder = Folder(menuMapping[value], distance)
            currentFolder.openImage()
            print(menuMapping[value]+" Menu Selected")
        else:
            print("Command not found")
        


while True:
    distance = int(input("Enter a distance: "))
    if distance is None:
        distance = 10
    while True:
        inData = input("Enter a string: ")
        if inData == "Exit" and currentFolder is None:
            print("Exiting to select distance")
            currentFolder = None
            break
        elif inData == "Exit" and currentFolder is not None:
            print("Exiting to Select folder")
            currentFolder = None
        else:    
            process_signal(distance, inData)

