import serial
import time
import matplotlib.pyplot as plt

print('Make sure you have selected correct COM & Baud rate')
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM5', 115200, timeout=1)
time.sleep(2)

 
for i in range(50):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        #num = int(string) # convert the unicode string to an int
        print(string)
         
ser.close()