import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="Hello UDP Server"
client_socket.sendto(msg.encode('utf-8'),('127.0.0.2',12345))
data,addr=client_socket.recvfrom(4096)
print("Server Says")
print(str(data))
client_socket.close()