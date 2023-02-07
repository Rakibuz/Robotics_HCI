from array import *
class Folder:
    images = array('i', [])
    name = ""
    currentIndex = 0
    def __init__(self, images, name):
        self.images = array('i', images)
        self.name = name
        self.currentIndex = 0
    def openImage(self):
        print('Opening')
    def processIrSignal(self, signal):
        if signal == "Left":
            print(signal + " Pressed on " + self.name)
            #Do something
        elif signal == "Right":
            print(signal + " Pressed on " + self.name)
            #Do something
        elif signal == "One":
            print(signal + " Pressed on " + self.name)
            #Do something
        elif signal == "Two":
            print(signal + " Pressed on " + self.name)
            #Do something
        self.openImage()
    
currentFolder = None

def process_signal(value):
    selButton = value
    global currentFolder
    if currentFolder is not None:
        currentFolder.processIrSignal(selButton)
    else:
        if selButton == "One":
            currentFolder = colorBlindFolder
            currentFolder.openImage()
            print("Color Blind Menu Selected")
        elif selButton == "Two":
            currentFolder = alphabets
            currentFolder.openImage()
            print("Alphabet Menu Selected")
        else:
            print("There is no functionality of button "+ value+" in current context")

#

colorBlindFolder = Folder([1, 2, 3], "Color Blind")
#
alphabets = Folder([5, 6, 7], "Alphabet Folder")
alphabets.images = array('i', [3,4])
#
while True:
    inData = input("Enter a string: ")
    if inData == "Exit":
        currentFolder = None
    else:    
        process_signal(inData)