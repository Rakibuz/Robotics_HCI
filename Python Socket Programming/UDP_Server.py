import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.2',12345))

while True:
    data,addr=sock.recvfrom(4096)
   
    message=bytes(("Hello I am UDP Server").encode('utf-8'))
    print(str(data))
    sock.sendto(message,addr)