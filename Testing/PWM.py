import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#setup pwm pin
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,0)
#GPIO.setup(19, GPIO.OUT)
try:
	pwm.start(1)
	time.sleep(100)
except KeyboardInterrupt:
	print("interrupted")
    
except:
	print("other error")
finally:
	pwm.stop()
	GPIO.cleanup()
