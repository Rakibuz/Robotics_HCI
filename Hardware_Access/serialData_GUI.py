import tkinter as tk
import time
import serial
import threading
import continuous_threading

print('Make sure you have selected correct COM & Baud rate')
ser = serial.Serial('COM5',115200)
val1 = 0

index = []
 
def readserial():
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("utf-8")
    print(ser_bytes)
    x = ser_bytes.split(",")
    #print(type(ser_bytes))
    # print(x[1])
    #index.append(x)
    #print(type(index))
    tk.Label(root,text=x[0]).place(x=50,y=10)
    tk.Label(root,text=x[1]).place(x=48,y=40)
    tk.Label(root,text=x[2]).place(x=47,y=70)

    time.sleep(0.2)


t1 = continuous_threading.PeriodicThread(0.5, readserial)
root = tk.Tk()
root.geometry("300x250")
 
w = tk.Label(root,text=' ').place(x=10,y=10)
w1 = tk.Label(root,text=' ').place(x=10,y=40)
w1 = tk.Label(root,text='').place(x=10,y=50)
t1.start()

root.title('ESP32-CAM')
root.mainloop()