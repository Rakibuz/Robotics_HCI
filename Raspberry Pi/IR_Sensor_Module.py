import RPi.GPIO as GPIO
import time 
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)  #module out pin
GPIO.setup(10,GPIO.OUT) #led or buzzer output
 
while True:
     if GPIO.input(8) ==0:
         print("IR sensor detect the object")
         GPIO.output(10,True)
     else:
         GPIO.output(10,False)
         print("IR sensor not detect the object")
