# Toss

This is a dummy appication to demonstrate the peer-to-peer network programming in python. This Application just tosses a coin randomly and let's you know about the outcome whether it is `HEAD` or `TAIL`.  
* _The server runs on the local ip-address (i.e. `lcalhost` or `127.0.0.1`)._  
* It internally generates a random number between \[0,100\] and takes the modulo operation of same with 2.  
    - If output is 0, it's `HEAD`  
    - If output is 1, it's `TAIL`  

## Using this Application
1. run the server using ```python3 serverToss.py```  
2. open a command line terminal and run ```python3 user.py```  
3. You'll immidiatly an output.  
4. Run `user.py` as many times as you want to take the trials.  