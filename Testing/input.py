import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#PUD_DOWN is normally low unless 3.3V is connected
#PUD_UP is normally high unless there is a path to ground

try:
    while 1:
        if GPIO.input(21):
            print ('Input was HIGH')
            time.sleep(1)
        else:
            print ('Input was LOW')
            time.sleep(1)
except KeyboardInterrupt:
    print ("User Interrupt")
finally:
    GPIO.cleanup()