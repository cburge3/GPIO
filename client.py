# Echo client program
import socket

waketime = (9, 55, 35)
endwaketime = (9, 56, 59)
sleeptime = (16, 15, 59)
endsleeptime = (5, 00, 20)

c = bytearray()
l=[waketime,endwaketime,sleeptime,endsleeptime]
[[c.append(a) for a in b] for b in l]

# print(c)
HOST = 'localhost'    # The remote host
PORT = 6000              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(10)
    s.connect((HOST, PORT))
    s.sendall(c)
    response = s.recv(1024)
    print('Received', str(response))