import time
import RPi.GPIO as GPIO


refreshtime = 1

#define toggle functionality
class ToggleSwitch:
    def __init__(self, input, output):
        self.last = 0
        self.input = input
        self.output = output

    def toggle(self):

        if GPIO.input(self.input):
            if self.last == 0:
                GPIO.output(self.output, GPIO.HIGH)
                self.last = 1
                time.sleep(.5)
            elif self.last == 1:
                GPIO.output(self.output, GPIO.LOW)
                self.last = 0
                time.sleep(.5)
        time.sleep(.05)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

yellow = ToggleSwitch(21, 11)
green = ToggleSwitch(22, 13)
blue = ToggleSwitch(23, 15)
#PUD_DOWN is normally low unless 3.3V is connected
#PUD_UP is normally high unless there is a path to ground

try:
    while 1:
        yellow.toggle()
        green.toggle()
        blue.toggle()

except KeyboardInterrupt:
    print ("User Interrupt")
finally:
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.cleanup()

