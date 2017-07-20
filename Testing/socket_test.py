import socket
s = socket.socket()
s.settimeout(5)
s.bind(('localhost',6000))
while True:
    try:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print(data)
                if not data: break
                conn.sendall(b"thanks for" + data)
    except socket.timeout:
        pass
    except KeyboardInterrupt:
        'monitoring interrupted'