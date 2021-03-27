####  the host to work intermediate b/w clients ####

## libraries
import threading
import socket

## connection details
host = '127.0.0.1'
port = 55555

## creating server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
## binding server
server.bind((host, port))
## listining for connection request
server.listen()

clientList = []
nickNames = []

## sending msg to all
def broadcast(message):
    for client in clientList:
        client.send(message)

## working for a single client
## it will run for run for each client as a thread
def handle(client):
    while True:
        # if a client is sending some msg
        try:
            message = client.recv(1024) # get msg
            broadcast(message)
        except:
            ## terminate connection with this client
            clientList.remove(client)
            client.close()

            nickname = nickNames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nickNames.remove(nickname)
            break

## receive 
def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        ## getting the nickname
        client.send('Tell your nickname!'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nickNames.append(nickname)
        clientList.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        ## to handle connection with this client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        


## here server is receiving the message
print("Server is listening now!")
receive()