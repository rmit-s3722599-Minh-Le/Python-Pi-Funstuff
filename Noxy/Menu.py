#!/usr/bin/env python3
import sys
import Customer as cust

def menuPrint():
    print("Menu")
    print("1. Register a customer")
    print("2. Call next customer")
    print("3. List customer in queue")
    print("0. Exit")

def main():
    global queueNum
    queueNum = 100
    global waitQueue
    global servedQueue
    waitQueue = []
    servedQueue = []
    while (True):
        menuPrint()
        text = input()
        if(text == "1"):
            #Register customer
            register() 
            queueNum += 1
        elif(text == "2"):
            print("selected call")
            call()
        elif (text =="3"):
            print("selected list")
            listCust()
        elif(text=="0"):
            sys.exit(0)
        else:
            continue



def register():
    print("Enter your name:")
    name = input()
    waitQueue.append(cust.Customer(queueNum,name))

def call():
    if not waitQueue:
        print("The wait queue is empty")
    else:
        while True:
            print("Looking for customer Queue No.{}".format(waitQueue[0].getQueue()))
            print("type in the repsonse: (respond or miss)")
            ans = input()
            ans = ans.lower()
            if(ans == "yes"):
                print("customer {} is being served".format(waitQueue[0].getName()))
                servedQueue.append(waitQueue.pop(0))
            elif(ans == "miss"):              
                waitQueue[0].incrmiss()
                if(waitQueue[0].getMissedCalls() == 3):
                    print("customer {} is being placed at the end of the queue".format(waitQueue[0].getName()))
                    waitQueue[0].resetMissedCalls()
                    servedQueue.append(servedQueue.pop(servedQueue[0]))

def listCust():
    if not waitQueue:
        print("The wait queue is empty")              
    else:
        for customer in waitQueue:
            customer.toString()

def exit():
    sys.exit(0)




if __name__ == "__main__":
    main()

