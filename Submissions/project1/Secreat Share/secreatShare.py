## importing modules
from shareBox import server as sender
from shareBox import client as receiver

######################

## main menu
def menu(extra):
    mainMenu = "\nMenu\n"+"-"*6+"\n\n1. Send Files! \n2. Receive Files!"+extra
    print(mainMenu)
    ch = input("\nEnter your choice: ")    
    return ch

## mainApp
def secreatShare(menuOption):
    choice = menu(menuOption)
    ## making host to share files
    if choice == '1':
        Sender = sender.server()
        print("\n"+"-"*20+"\n")
        Sender.server()
        return True
    ## making client to get files
    elif choice == '2':
        Receiver = receiver.client()
        print("\n"+"-"*20+"\n")
        Receiver.client()
        return True
    ## invalid input
    else:
        print("\n"+"-"*20+"\n")
        return False
    
    ## if ran at least once
    flag = False

######################


if __name__ == '__main__':
    flag = True
    firstRun = True
    addOnMenu = ''

    while flag:
        flag = secreatShare(addOnMenu)
        if flag and firstRun:
            firstRun = False
        elif not firstRun:
            addOnMenu = "\n*  Any other key to exit!!"
    
    if firstRun:
        print("\nSomething went wrong!!\nApp terminated unexpectedly!!")
    else:
        print("\nThanks for using 'Secreat Share'!\n")