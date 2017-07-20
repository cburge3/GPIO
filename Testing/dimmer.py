import RPi.GPIO as GPIO
import time
#from sunrise import calculatedutycycle
import socket

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)

localfrequency = 60
timer = False
movingaveragesamples = 50
cycles = []
[cycles.append(1/(2 * localfrequency)) for a in range(0,movingaveragesamples)]
print(cycles)

def fetch():
    data = None
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setblocking(False)
        try:
            s.connect(('localhost', 6001))
            data = s.recv(1024)
            print('Received', str(data))
        except:
            pass
    return data

waketime = (5, 35, 00)
endwaketime = (6, 00, 11)
sleeptime = (21, 15, 00)
endsleeptime = (21, 30, 22)

start = time.perf_counter()
triacon = False
newsinus = False
# time to let triac gate energize
delaytime = 0.0001
dc = 75
ontime = 0


#GPIO.output(21,GPIO.HIGH)

def average(l):
    return sum(l)/len(l)
try:
    while True:
        #check for updates
        data = fetch()
        cycletime = average(cycles)
        if data is not None:
            waketime, endwaketime, sleeptime, endsleeptime = [tuple(a) for a in data]
            print(waketime,endwaketime,sleeptime,endsleeptime)
            #time.sleep(10)
        #dc = calculatedutycycle(waketime, endwaketime, sleeptime, endsleeptime)
        targettime = (100 - dc) / 100 * cycletime
        if GPIO.input(19) == False and timer == False:
            print("begin sinus")
            #start of sinus
            timer = True
            start = time.perf_counter()
            print("low",start)
            newsinus = True
        elif time.perf_counter() - start >= targettime and triacon == False and newsinus == True:
            print("triac energized")
            GPIO.output(21, GPIO.HIGH)
            triacon = True
            ontime = time.perf_counter()
        elif time.perf_counter() - ontime > delaytime and triacon == True and newsinus == True:
            print('triac deenergized')
            GPIO.output(21, GPIO.LOW)
            triacon = False
            newsinus = False
        elif GPIO.input(19) == True and timer == True:
            #end of sinus
            print("end sinus")
            GPIO.output(21, GPIO.LOW)
            triacon = False
            timer = False
            newsinus = False
            end = time.perf_counter()
            print(end-start)
            cycles.append(end - start)
            cycles.pop(0)
        print(time.perf_counter())
except KeyboardInterrupt:
    print("interrupted", 1/(2*average(cycles)))
    print(cycles)
finally:

    GPIO.cleanup()
