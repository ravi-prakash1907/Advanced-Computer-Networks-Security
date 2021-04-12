## user who can connect to the server and access the calculator

## library
import threading
import socket

## connection details
host = '127.0.0.1'
port = 55555
choice = ''
connectionFlag = False

## creating client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## connecting to the binded port of server's ip
try:
    client.connect((host, port))
    connectionFlag = True
except ConnectionRefusedError:
    print("Server is down! Try later!!")

################

## receiving message from server
def receive():
    try:
        ## getting the outcome
        result = client.recv(1024).decode('ascii')
        print(result)

    except:
        print("Something went wrong!!")
        client.close()

receive()