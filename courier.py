import socket
from sunrise import overlappingintervals, validate

inaddress = ('localhost', 6000)
outaddress = ('localhost', 6001)

def unpack(bits, interval):
    q = []
    for z in range(0,len(bits),interval):
        q.append(bits[z:z+interval])
    return q

def receivedata():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(inaddress)
            s.listen()
            #s.settimeout(.001)
            #s.setblocking(False)
            #s.settimeout(5)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    print(data)
                    try:
                        raw = unpack(data, 3)
                        [validate(a) for a in raw]
                        if not overlappingintervals(raw[0], raw[1], raw[2], raw[3]):
                            # waketime = tuple(raw[0])
                            # endwaketime = tuple(raw[1])
                            # sleeptime = tuple(raw[2])
                            # endsleeptime = tuple(raw[3])
                            conn.sendall(b"thanks for updates")
                            return raw
                        else:
                            conn.sendall(b'overlapping intervals')
                    except:
                        conn.sendall(b"invalid")
                    if not data: break
        except BlockingIOError:
            pass
        except KeyboardInterrupt:
            'monitoring interrupted'

if __name__ == '__main__':
# packing of initial values
    while True:
        currentdata = receivedata()
