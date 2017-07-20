import time
# def dim():
#     pin = 'OFF'
#     if zerocross == True:
#         start = time.perf_counter()
#         counter = 0
#         dc = yield
#         while True:
#             test = yield dc
#             if time.perf_counter() < start + test /100 * period:
#                 counter += 1
#                 if pin != 'ON':
#                     pin = 'ON'
#             else:
#                 pin = 'OFF'
#                 finish = time.perf_counter()
#                 print(finish-start, period, counter)
#                 start = time.perf_counter()
#                 break
#
# def transmit():
#     while True:
#         print("Transmission")
#         time.sleep(4)

def z():
    newdc = yield
    value = 0
    while True:
        dc = yield newdc
        # do things with new dc

#
# frequency = .1
# period = 1 / frequency
# zerocross = True
# f = z()
# for q in f:
#     print(q)
# print(f)
# next(f)
# print(f.send(4))
# f.send(50)
# f.send(30)
# #f.send(150)
# f.send(2)

def gen():
    mylist = range(1,6,2)
    for i in mylist:
        yield i*i,i

p = gen()
print(next(p),next(p),next(p))
print(p,next(p))