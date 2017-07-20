import time
import RPi.GPIO as GPIO


class DimmerSwitch:
    def __init__(self, input, output):
        #1 = up -1 = down
        self.direction = 1
        self.input = input
        self.output = output
        #0 - 100
        self.duty = 0
        GPIO.setup(input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(output, GPIO.OUT)
        self.pwm = GPIO.PWM(output, 60)
        self.pwm.start(self.duty)

    def ramp(self):
        if GPIO.input(self.input):
            while 1:
                self.pwm.ChangeDutyCycle(self.duty)
                if (self.duty == 100 and self.direction > 0 or
                    self.duty == 0 and self.direction < 0):
                    pass
                else:
                    self.duty += self.direction
                time.sleep(.02)
                if GPIO.input(self.input) == 0:
                    self.direction = -1 * self.direction
                    break
            # for dc in range(100, -1, -1):
            #     p.ChangeDutyCycle(dc)
            #     # print(dc)
            #     time.sleep(0.01)
            #time.sleep(2)

GPIO.setmode(GPIO.BOARD)

yellow = DimmerSwitch(21,11)
green = DimmerSwitch(22,13)
blue = DimmerSwitch(23, 15)

#PUD_DOWN is normally low unless 3.3V is connected
#PUD_UP is normally high unless there is a path to ground

try:
    while 1:
        yellow.ramp()
        green.ramp()
        blue.ramp()

except KeyboardInterrupt:
    print ("User Interrupt")
finally:
    GPIO.cleanup()

