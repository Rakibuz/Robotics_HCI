import evdev
from time import sleep
import pygame, sys, random
from pygame import display,movie
from PIL import Image

pygame.init()



#screen =pygame.display.set_mode((0,0))
#pygame.mouse.set_visible(0)
#login = pygame.image.load("/home/pi/Pictures/images/login.jpg")
#screen.blit(login,(0,0))

def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if (device.name == "gpio_ir_recv"):
            #print("Using device", device.path, "\n")
            return device
    print("No device found!")

dev = get_ir_device()

print("Press Button on Remote------------>")
#sleep(5)  # allow some time to press buttons on remote
#Sevents = dev.read()
"""
try:
    event_list = [event.value for event in events]
    print("Received commands:", event_list)
except BlockingIOError:
    print("No commands received.\n")
"""
while(True):
    event = dev.read_one()
    flag=0
    sleep(1)
    
    
    if (event):
        print(event)
        print(type(event))
       
        
        #print("Received commands", event.value)
        if(event.value==48898 and flag==0):
          print("You have pressed 1")
          flag==1
          #continue
          #sleep(2)
        elif(event.value==48899 and flag==0):
          print("You have pressed 2")
          flag==1
          #flag==1
          #sleep(2)
          #continue
        elif(event.value==48900 and flag==0):
          print("You have pressed 3")
          flag==1
          #sleep(2)
          #continue
        elif(event.value==48901 and flag==0):
          print("You have pressed 4")
          flag==1
          #sleep(2)
          #continue
        elif(event.value==48902 and flag==0):
          print("You have pressed 5")
          #continue  
          
          #screen.blit(pygame.image.load("/home/pi/Pictures/images/login.jpg"),(0,0))
          im = Image.open("/home/pi/Pictures/cdr-dbus-ssh/se_6.jpg")
          im.show()
          flag==1
          #break
          #sleep(2)
          #flag==1
          #pass
          #event=dev.stop_here()
          #continue
      
			
			
        
