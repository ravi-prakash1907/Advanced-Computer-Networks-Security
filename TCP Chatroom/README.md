# TCP Chatroom

This is a dummy appication to demonstrate the working of a chatroom. This chatroom works on the TCP protocol. The _server_ keeps on monitering all the connected clients and works as a mediator to cater the messages being between different users i.e. clients. Obviously to be the part of the chatroom, every new client must has to connect with the server, only!  
* _By default, the server runs on the local ip-address (i.e. `lcalhost` or `127.0.0.1`)._  
* For any other desired ip-address, change the same in [`server.py`](server.py)  

## Using this Application
1. run the server using ```python3 server.py```  
2. open a command line terminal and run ```python3 client.py```  
3. join the chatroom as a new client using by providing your nickname  
4. You can run as many inctances of the ```client.py``` as you want to join the chatroom!!  
5. Enjoy the chatting!!