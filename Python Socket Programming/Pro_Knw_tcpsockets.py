from socket import*
import socket
import sys

try:
    sock=socket.socket(family=AF_INET,type=SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print("Reason: %s" %str(err))
    sys.exit()

print("Socekt created")

target_host=input("Enter the target_host name to connect: ")
target_port=input("Enter the target port: ")

try:
    sock.connect((target_host,int(target_port)))
    print("socket connected to: %s" %(target_host+target_port))
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect: %s" %(target_host+target_port))
    print("Reason %s"%str(err))
    sys.exit()

