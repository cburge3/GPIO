import time
from scipy.interpolate import interp1d
import socket

waketime = (5, 35, 00)
endwaketime = (6, 00, 11)
sleeptime = (21, 15, 00)
endsleeptime = (21, 30, 22)
address = ('localhost', 6000)
rampfunction = None
wakeramp = lambda x: x*x
sleepramp = lambda x:10000 - x*x
day = lambda x: 100
night = lambda x: 0
rampstarttime = (0, 0, 0)
interval = 100

def validate(testtime):
    if testtime[0] > 23 or testtime[0] < 0:
        raise ValueError('Invalid hours')
    if testtime[1] > 59 or testtime[1] < 0:
        raise ValueError('Invalid minutes')
    if testtime[2] > 59 or testtime[2] < 0:
        raise ValueError('Invalid seconds')


def timediff(begin,end):
    # this assumes that end is after beginning to always yield a positive difference
    begin = list(begin)
    end = list(end)
    if end[2] < begin[2]:
        end[2] += 60
        end[1] -= 1
    if end[1] < begin[1]:
        end[1] += 60
        end[0] -= 1
    if end[0] < begin[0]:
        end[0] += 24
    return [e - b for b, e in zip(begin, end)]


def tosecs(testtime):
    result = testtime[0]*3600
    result += testtime[1]*60
    result += testtime[2]
    return result


def characterization(function):
        x = range(0,100,1)
        # actual characterization function
        y = [function(t) for t in x]
        # normalization to 0 - 100
        y = [t / max(y) * 100 for t in y]
        return x, y


def between(t, start, end):
    # this function assumes that end is after start no matter what the day is
    return True if timediff(start,end) >= timediff(start,t) else False


def overlappingintervals(wt, ewt, st, est):
    return True if between(st,wt,ewt) or between(est,wt,ewt) or between(wt,st,est) or between(ewt,st,est) else False


def interpolationprotector(value,tmax):
    scaledvalue = value/tmax * 100
    return max(1,min(scaledvalue,99))


def calculatedutycycle(wt=waketime, ewt=endwaketime, st=sleeptime, est=endsleeptime):
    # this function assumes that waketime, endwaketime, sleeptime, and endsleeptime have already been validated against
    # overlapping intervals and for proper formatting
    t = time.localtime()
    curtime = t[3], t[4], t[5]
    rampstarttime = curtime
    interval = 100
    if between(curtime, wt, ewt):
        # print('sunrise')
        x, y = characterization(wakeramp)
        rampfunction = interp1d(x, y)
        rampstarttime = wt
        interval = tosecs(timediff(wt, ewt))
    elif between(curtime, st, est):
        # print('sunset')
        x, y = characterization(sleepramp)
        rampfunction = interp1d(x, y)
        rampstarttime = st
        interval = tosecs(timediff(st, est))
    elif between(curtime, est, wt):
        # print("nighttime")
        rampfunction = night
    elif between(curtime, ewt, st):
        # print("daytime")
        rampfunction = day
    else:
        raise Exception('Current time not within any defined bounds')
    return rampfunction(interpolationprotector(tosecs(timediff(rampstarttime, curtime)), interval))

if __name__ == '__main__':
    while True:
        dc = calculatedutycycle(waketime,endwaketime,sleeptime,endsleeptime)
        print(dc)
        time.sleep(5)
