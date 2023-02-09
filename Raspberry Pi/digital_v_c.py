from array import *
import os
from datetime import datetime
from PIL import Image
import  RPi.GPIO as GPIO

pin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN)

 
 
distantToFolderMappings = {
    "0x300fdf20d": "/home/pi/Optoshi/12",
    "0x300fd728d": "/home/pi/Optoshi/10",
    "0x300fdb24d": "/home/pi/Optoshi/8",
     
}
menuMapping = {
    "0x300fd40bf": "e",
    "0x300fdc03f": "pediatric",
}



 

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
        if signal == "0x300fd8877":
           self.moveIndexToLeft()
           print(signal + " Pressed on " + self.name)
        elif signal == "0x300fd48b7":
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



def getBinary():
	num1s =0
	binary=1
	command=[]
	previousValue=0
	
	value=GPIO.input(pin)
	#print(value)
	
	while value:
		value=GPIO.input(pin)
	startTime=datetime.now()
	
	while True:
		if previousValue !=value:
			now=datetime.now()
			pulseTime =now-startTime
			startTime=now
			command.append((previousValue,pulseTime.microseconds))
			#print(command)
		
		if value:
			num1s +=1
		else:
			num1s = 0
		
		if num1s> 10000:
			break
			
		previousValue =value
		value=GPIO.input(pin)
	
	#print(command)
	for (typ,tme) in command:
		if typ == 1:
			if tme > 1000:
				binary=binary*10 +1
			else:
				binary *=10
				
	if len(str(binary)) >34:
		binary =int(str(binary)[:34])
		
	return binary

def convertHex(binaryValue):
	tmpB2 =int(str(binaryValue),2)
	return hex(tmpB2)


    
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
        """
        else:
            print("Command not found")
        """
        



while True:
    #distance = int(input("Enter a distance: "))
    distance = convertHex(getBinary())
    if distance is None:
        distance = "0x300fd728d"
    while True:
        #inData = input("Enter a string: ")
        inData = convertHex(getBinary())
        if inData == "0x300fda857" and currentFolder is None:
            print("Exiting to select distance")
            currentFolder = None
            break
        elif inData == "0x300fda857" and currentFolder is not None:
            print("Exiting to Select folder")
            currentFolder = None
        else:    
            process_signal(distance, inData)

 


 



