# Importing tkinter module
from tkinter import *  
import serial  
import serial.tools.list_ports
from tkinter import messagebox
import pyttsx3


speech = pyttsx3.init()

# Creating a tkinter window
root = Tk()

# Initialize tkinter window with dimensions 300 x 250            
root.geometry('300x250')    


# Creating a Button
btn_on = Button(root, text = 'ON',width=5,height=3)
# Set the position of button  
btn_on.place(x=100, y=20)


btn_off= Button(root, text = 'OFF',width=5,height=3)
# Set the position of button 
btn_off.place(x=100, y=100)



arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    speech.say('No Arduino Found, Connect Arduino')
    speech.runAndWait()
    messagebox.showwarning('Info','No Arduino Found')
if len(arduino_ports)== 1:
    print(arduino_ports)
    id=0
    speech.say('Arduino Found at'+arduino_ports[id])
    speech.runAndWait()
if len(arduino_ports) > 1:
    messagebox.showwarning('Info','Multiple Arduinos found - using the first')
    id=0


Arduino_Serial = serial.Serial(arduino_ports[id],9600)    

# Defining method on click
def On_Clicked(event):
    Arduino_Serial.write('1'.encode()) 

def Off_Clicked(event):
    Arduino_Serial.write('0'.encode()) 
    #print('Hello')

btn_on.bind("<Button>",On_Clicked)  #bind(all the name Button,function name)
btn_on.pack()

btn_off.bind("<Button>",Off_Clicked)
btn_off.pack()


root.mainloop()