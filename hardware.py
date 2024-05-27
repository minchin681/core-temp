import MacTmp
import os
import time
from threading import Timer

temp = MacTmp.CPU_Temp()
zepeyou = int(temp[:2])
print("The CPU temperature is: " + str(zepeyou))
thetime = time.localtime()
now = time.asctime(thetime)


def show():
    w = 1
    while w <= 6:
        if w == 6:
            print("Your computer CPU temperature is " + str(zepeyou) + " & the count number is " + str(w))
            time.sleep(10)
            os.system("shutdown -h now")
        else:
            print("the temp is " + str(zepeyou) + " & the count number is " + str(w))
            time.sleep(10)
            w += 1

def check():
    print("CPU temperature check is starting! " + now)
    if zepeyou > 80:
        show()
    else:
        print("temperature is below threshhold good bye :)", zepeyou)
        t = Timer(1000, check)
        t.start()

check() 
