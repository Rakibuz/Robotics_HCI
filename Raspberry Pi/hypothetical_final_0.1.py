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
    "One": "e",
    "Two": "pediatric"
}
distanceMapping = {
    "Eight": 8,
    "Ten": 10
}
def convertHex(binaryValue):
	tmpB2 =int(str(binaryValue),2)
	return hex(tmpB2)

 
class Folder:
    menuId = ""
    images = []
    name = ""
    currentIndex = 0
    def __init__(self, distance, menuId):
        self.name = menuMapping[menuId]
        distancePath = distantToFolderMappings[distance]
        actualFolderPath = distancePath+"/"+self.name
        folderImages = self.get_files_in_directory(actualFolderPath)
        self.images = [file for file in folderImages if file.endswith(".png") or file.endswith(".jpg")]
        
        self.currentIndex = 0
        self.menuId = menuId
        self.openImage()
        #print(self.images)
    def openImage(self):
        print("Opening from Folder "+self.name+" with index "+str(self.currentIndex))
        img = Image.open(self.images[self.currentIndex])
        self.currentImage = img
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
        status = 1
        if signal == "Left":
           self.moveIndexToLeft()
           print(signal + " Pressed on " + self.name)
        elif signal == "Right":
            self.moveIndexToRight()
            print(signal + " Pressed on " + self.name)
        elif signal == self.findKey(menuMapping, self.name):
            print("Menu button pressed. Opening Next image")
            self.moveIndexToRight()
        else:
            status = -1
            print("Command not found inside class and status is -1")
        if status == 1:
            self.openImage()
        return status
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
def createFolder(distance, value):
    if value in menuMapping:
        return Folder(distance, value)
    else:
        return None
def process_signal(distance, value):
    selButton = value
    global currentFolder
    if currentFolder is not None:
        status = currentFolder.processIrSignal(selButton)
        if status == -1:
            print("Status found -1 from processSignal")
            newFolder = createFolder(distance, value)
            if newFolder is not None:
                currentFolder = newFolder
    else:
        currentFolder = createFolder(distance, value)
        if currentFolder is not None:
            print(menuMapping[value]+" Menu Selected")
        else:
            print("Command not found")
        
        


while True:
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
        elif inData in distanceMapping:
            distance = distanceMapping[inData]
            print(str(distance) + " Selected")
            currentFolder = None
        else:    
            process_signal(distance, inData)
            print("Action taken with "+str(distance)+" feet distance")

