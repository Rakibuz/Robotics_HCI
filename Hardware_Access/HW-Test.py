import serial.tools.list_ports
# from tkinter import messagebox

 
# comlist = serial.tools.list_ports.comports()
# connected = []
# for element in comlist:
#     connected.append(element.device)
 
# messagebox.showinfo("Available COM Ports","" + str(connected) )

import win32com.client
wmi = win32com.client.GetObject("winmgmts:")
for serial in wmi.InstancesOf("Win32_SerialPort"):
       print (serial.Name, serial.Description)

 
 