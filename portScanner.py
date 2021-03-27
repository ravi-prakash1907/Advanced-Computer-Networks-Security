## Scanning multiple ports using multi threading ##

## scans the open ports:  if open unecessarly, it can be a security loophole
import socket
import threading 
from queue import Queue

## where to scan
target = '127.0.0.1'
queue = Queue() # empty queue for port storage 
openPorts = []


# to scan the desired port
def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM tells that we are using TCP, not UDP
        sock.connect((target, port))
        return True
    except:
        return False


## queue of ports
def fillQueue(ports):
    for port in ports:
        queue.put(port)

## to be used by thread
def scanner():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open!!".format(port))
            openPorts.append(port)


############
portRange = range(1,1324)
fillQueue(portRange)

threads = []
for th in range(100):
    thread = threading.Thread(target=scanner)
    threads.append(thread)

flag = True
for thread in threads:
    if flag:
        print()
        thread.start()
        flag = False
    else:
        thread.start()

for thread in threads:
    thread.join()

print("\nOpen ports: ",openPorts,"\n")