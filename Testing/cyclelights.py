import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

counter = 0
timer = .2
try:
	while counter <1000000:
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		#print("1")
		time.sleep(timer)
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.HIGH)
		#print("2")
		time.sleep(timer)
		GPIO.output(13,GPIO.LOW)
		#print("3")
		GPIO.output(15,GPIO.HIGH)
		time.sleep(timer)
		#print(counter)
		counter += 1
except KeyboardInterrupt:
	print("interrupted")
# except:
# 	print("other error")
finally:
	#GPIO.output(11,GPIO.LOW)
	GPIO.cleanup()
