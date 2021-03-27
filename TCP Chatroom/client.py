####  the client that will actualy interact ####

## libraries
import threading
import socket

## connection details
host = '127.0.0.1'
port = 55555
nickname = input("Enter your nickname: ")
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
## here we need 2 threads for every client:
##      1. one to constently listen for new message from the server
##      2. one to send the msg

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'Tell your nickname!':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Somethig went wrong!!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

if connectionFlag:
    ## starting the thread to receive a message
    receiveThread = threading.Thread(target=receive)
    receiveThread.start()

    ## starting the thread to send a message
    sendThread = threading.Thread(target=write)
    sendThread.start()