from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = 255
g = 255
b = 255
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
while(True):
    print("Type ur command:")
    ans = input()
    ans = ans.lower()
    
    if(ans == "exit"):
        sense.clear()
        exit(0)
    elif(ans == "color"):
        print("type as the color or in r,g,b")
        txt = input()
        if(txt.find(',')==3):
            rgbList = txt.split(",")
            sense.clear((int(rgbList[0]),int(rgbList[1]),int(rgbList[2])))
        else:
            txt = txt.lower()
            if(txt == "red"):
                sense.clear(red)
            elif(txt == "blue"):
                sense.clear(blue)
            elif(txt == "green"):
                sense.clear(green)
            else:
                print("unknown color or not patched yet")
        sleep(2)
    elif(ans == "temp"):
        temp = round(sense.get_temperature(), 1)
        print("Temperature: %s C" % temp)
        sense.show_message("%s C" % temp)
    elif(ans == "what"):
        sense.clear()
        sense.set_pixel(2, 2, (0, 0, 255))
        sense.set_pixel(4, 2, (0, 0, 255))
        sense.set_pixel(2, 4, (255, 0, 0))
        sense.set_pixel(3, 4, (255, 0, 0))
        sense.set_pixel(4, 4, (255, 0, 0))
        sense.set_pixel(2, 5, (255, 0, 0))
        sense.set_pixel(2, 6, (255, 0, 0))
        sense.set_pixel(3, 6, (255, 0, 0))
        sense.set_pixel(4, 6, (255, 0, 0))
        sense.set_pixel(4, 5, (255, 0, 0))
    else:
        continue



