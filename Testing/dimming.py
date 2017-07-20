import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)


p = GPIO.PWM(19, 60)  # channel=12 frequency=50Hz

try:
    while 1:
        p.start(100)
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            #print(dc)
            time.sleep(.01)
        time.sleep(2)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            #print(dc)
            time.sleep(0.01)
        time.sleep(2)

except KeyboardInterrupt:
    print ("User Interrupt")
p.stop()
GPIO.cleanup()