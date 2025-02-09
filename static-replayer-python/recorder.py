import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1', 60000))

while True:
    data, addr = sock.recvfrom(65000)
    print(f'{time.time()}: {data.decode()}')