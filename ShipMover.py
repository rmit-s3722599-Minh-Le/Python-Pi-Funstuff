#!/usr/bin/env python3
from sense_hat import SenseHat
import signal
import random
import time
import os
sense = SenseHat()
file_path = "SM_Score.txt"
def main():
    hsfileopener()
    signal.signal(signal.SIGINT, handler)
    thisShip = ship()
    thisBullet = bullet()
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        x=round(x, 0)
        if(x == 1):
            thisShip.moveRight()
        if(x == -1):
            thisShip.moveLeft()
        thisBullet.launch()
        thisShip.checkShip()
        if(thisBullet.reFire()):
            thisShip.incrPoint()
        # print("x={0}".format(x))

def hsfileopener():
    global hScore
    global hname
    if os.path.exists(file_path):
        f = open(file_path,"r")
        hScoreTxt = f.readline()
        hname = f.readline()
        hScore = int(hScoreTxt)
    else:
        f = open(file_path, "x")
        hScore = 0
        hname = "nan"
    print("--------------------------------")
    print("CURRENT HIGH SCORE: {}".format(hScore))
    print("HIGH SCORE NAME: {}".format(hname))
    print("--------------------------------")
    f.close()

def hsfilecloser():
    f = open(file_path,"w")
    f.write("{}\n".format(str(hScore)))
    f.write(hname)
    f.close()
    
def handler(signum, frame):
    print("exiting")
    sense.clear()
    exit(0)

class bullet:
    def __init__(self):
        self.xPos = random.randint(0,7)
        self.yPos = 0
        sense.set_pixel(self.xPos,self.yPos,(255,0,0))
    def launch(self):
        if (self.yPos < 7):
            # sense.clear()
            # print("firing")
            sense.set_pixel(self.xPos,self.yPos,(0,0,0))
            self.yPos = self.yPos + 1          
            sense.set_pixel(self.xPos,self.yPos,(255,0,0))
            time.sleep(0.1)
    def reFire(self):
        if(self.yPos == 7):
            # time.sleep(0.5)
            sense.set_pixel(self.xPos,self.yPos,(0,0,0))
            self.xPos = random.randint(0,7)
            self.yPos = 0
            sense.set_pixel(self.xPos,self.yPos,(255,0,0))
            return True
        else: 
            return False


class ship:
    def __init__(self):
        self.stamps = [2,3,4]
        self.setShip()
        self.points = 0

    def setShip(self):
        sense.clear()
        sense.set_pixel(self.stamps[0], 7, (0, 0, 255))
        sense.set_pixel(self.stamps[1], 6, (0, 0, 255))
        sense.set_pixel(self.stamps[2], 7, (0, 0, 255))
    def moveLeft(self):
        # x = 0
        if(self.stamps[0] != 0):
            self.stamps[0] = int(self.stamps[0]) - 1
            self.stamps[1] = int(self.stamps[1]) - 1
            self.stamps[2] = int(self.stamps[2]) - 1
            # for stamp in self.stamps:
            #     self.stamps[x] = stamp -1
            self.setShip()

    def moveRight(self):
        # x = 0
        if(self.stamps[0] != 5):
            # for stamp in self.stamps:
            #     self.stamps[x] = stamp +1
            self.stamps[0] = int(self.stamps[0]) + 1
            self.stamps[1] = int(self.stamps[1]) + 1
            self.stamps[2] = int(self.stamps[2]) + 1
            self.setShip()
    def checkShip(self):
        col = sense.get_pixel(self.stamps[0],7)
        col1 = sense.get_pixel(self.stamps[1],6)
        col2 = sense.get_pixel(self.stamps[2],7)

        if not(col[2] ==col1[2] and col1[2] == col2[2] and col[2]==col2[2]):
            print("Game over")
            print("Total Points: {}".format(self.points))
            global hScore
            global hname
            if (self.points > hScore):
                hScore = self.points
                print("NEW HIGH SCORE! TYPE IN YOUR NAME!")
                username = input()
                hname = username
            hsfilecloser()
            time.sleep(1)
            sense.clear()
            exit(0)
    def incrPoint(self):
        self.points = self.points + 1
if __name__ == "__main__":
    main()