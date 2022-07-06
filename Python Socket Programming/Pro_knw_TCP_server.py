from base64 import decode
import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.2',12345))
server_socket.listen(5) #listen takes a back log parameter 5 connection here is keep waiting as the server is busy


while True:
    print("server waiting for conncetion:")
    client_socket,addr=server_socket.accept()
    print("Client connected from",addr)
    while True:
        data=client_socket.recv(1024) #this method received atmost 1024 bytes
        if not data or data.decode('utf-8')=='END':
            break
        print("received from client: %s"% data.decode("utf-8"))
        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print("Exited by the user")
    client_socket.close() 
    
    #server_socket.close()
            
