import serial.tools.list_ports

ports=serial.tools.list_ports.comports()
serialInst =serial.Serial()

portList=[]

print('Make sure you have selected correct COM & Baud rate')
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))


val = input("Select Port: COM")
for x in range(0,len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar="COM"+str(val)
        print("You have Selected ---> "+portList[x])
 

serialInst.baudrate = 115200
serialInst.port=portVar
serialInst.open()


while True:
    if serialInst.in_waiting:
        packet=serialInst.readline()
        #print('\n')
        print(packet.decode('utf').rstrip('\n'))

