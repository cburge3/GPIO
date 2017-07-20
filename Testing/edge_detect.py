import RPi.GPIO as GPIO
import time
from sunrise import receivedata as r

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)

timer = False
cycles = []

GPIO.output(21,GPIO.HIGH)

def average(l):
    return sum(l)/len(l)
try:
    while True:
        print(r())
        if GPIO.input(19) == False and timer == False:
            timer = True
            start = time.perf_counter()
            print("low",start)
        elif GPIO.input(19) == True and timer == True:
            timer = False
            end = time.perf_counter()
            print("high",end)
            print(end-start)
            cycles.append(end - start)
except KeyboardInterrupt:
    print("interrupted", 1/average(cycles))
finally:

    GPIO.cleanup()
