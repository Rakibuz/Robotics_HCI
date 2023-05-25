import  RPi.GPIO as GPIO
from datetime import datetime
from PIL import Image

pin=11
Buttons=[0x300fd40bf,0x300fdc03f,0x300fd20df,0x300fda05f,0x300fd609f,0x300fde01f,0x300fd10ef,0x300fd906f,0x300fd50af,0x300fd30cf,0x300fdb24d,0x300fd728d,0x300fdf20d,0x300fd8877,0x300fd48b7]
ButtonsNames=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Zero","MENU","TITLE","L/R","Left_key","Right_key"]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN)




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


 
	
def process_signal(value):
	
	for button in range(len(Buttons)):
		if hex(Buttons[button]) == value:
			#print(ButtonsNames[button])
			if(ButtonsNames[button]=='One'):
				print("Ok")	 
				 
		 
		

while True:
	inData=convertHex(getBinary())
	#inData_filtered=inData[-4:] #collecting last four digit of Hex Code
	#print(type(inData))
	#print(inData)
	#process_signal(inData)
	test=process_signal(inData)
	print(test)
	 
	  
	 
