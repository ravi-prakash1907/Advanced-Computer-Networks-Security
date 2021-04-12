## A program to randomly toss a coin

## library
import socket
import random

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


## toss
def tossACoin():
    gotNum = random.randint(0, 100)
    res = gotNum % 2
    outcome = 'HEAD' if res == 0 else 'TAIL'
    return outcome


## receive 
def receive():
    flag = True
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        ## tossing the coin and sending the result
        Outcome = "Tossed coin landed on: "+tossACoin()
        client.send(Outcome.encode('ascii'))   

## here server is receiving the message
receive()