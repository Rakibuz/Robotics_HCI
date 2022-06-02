
# Importing tkinter module
from tkinter import *  
import serial  


Arduino_Serial = serial.Serial('COM4',9600) 
 
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
 
 
 
# Defining method on click
def On_Clicked(event):
    Arduino_Serial.write('1'.encode()) 

def Off_Clicked(event):
    Arduino_Serial.write('0'.encode()) 

btn_on.bind("<Button-1>" ,On_Clicked)
#btn_on.pack()

btn_off.bind("<Button-2>",Off_Clicked)
#btn_off.pack()


root.mainloop()