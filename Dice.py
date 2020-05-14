#!/usr/bin/env python3
#recognition for http://yaab-arduino.blogspot.com/2016/08/display-two-digits-numbers-on-raspberry.html in shownumber() and showdigit()
from sense_hat import SenseHat
import random
import signal
import time
OFFSET_LEFT = -2
OFFSET_TOP = 2
sense = SenseHat()

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9
def handler(signum, frame):
    print("exiting")
    sense.clear()
    exit(0)
def main():
    signal.signal(signal.SIGINT, handler)
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x1 = acceleration['x']
    y1 = acceleration['y']
    z1 = acceleration['z']
    x1=round(x1, 0)
    y1=round(y1, 0)
    z1=round(z1, 0)
    while(True):
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)
        if(x !=x1 or y!=y1 or z!=z1):
            # print("x={0}, y={1}, z={2}".format(x, y, z))
            t = 400
            while t >= 0:
                num = random.randint(0,6)
                show_number(num, 0, 0, 255)
                t -=1
            x1 = x
            y1 = y
            z1 = z


# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)


if __name__ == "__main__":
    main()