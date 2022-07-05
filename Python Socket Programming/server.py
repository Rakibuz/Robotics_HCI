import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#AF_INET==== address from the internet(host,port no),  SOCK_STREAM used for TCP protocol
s.bind((socket.gethostname(),1025)) #server and client at the same computer
#port number greater than 1023 are non privilied port number
s.listen(5)

while True:
    clt, adr=s.accept()
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket Programming in Python","utf-8"))
    clt.close()