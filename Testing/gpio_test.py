import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(2, GPIO.IN)

counter = 0
try:
    while counter <1000000:
        GPIO.output(3,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(3, GPIO.LOW)
        time.sleep(5)
	print(counter)
        counter += 1
except KeyboardInterrupt:
    print("interrupted")
    
except:
    print("other error")
finally:

    GPIO.cleanup()
