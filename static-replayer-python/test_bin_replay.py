import threading
import socket
import json

kill_request = {
    "jsonrpc": "2.0",
    "method": "kill",
    "params": [1, 2, 3],
    "id": 1
}

trigger_request = {
    "jsonrpc": "2.0",
    "method": "trigger",
    "params": [1, 2, 3],
    "id": 1
}

suspend_request = {
    "jsonrpc": "2.0",
    "method": "suspend",
    "params": [1, 2, 3],
    "id": 1
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified host and port
sock.bind(('127.0.0.1', 0))
sendto_addr = ('127.0.0.1', 50000)
cmd = ''
with open('myfile.bin', 'wb') as f:
    # Write 512 bytes of zeros to the file
        f.write(b'A' * 10)
        f.write(b'B' * 10)
        f.write(b'C' * 10)
        f.write(b'D' * 10)
while cmd != 'kill':
    cmd = input("please insert cmd: ")
    if cmd == 'trigger':
        request_json = json.dumps(trigger_request)
        sock.sendto(request_json.encode(), sendto_addr)
    elif cmd == 'suspend':
        request_json = json.dumps(suspend_request)
        sock.sendto(request_json.encode(), sendto_addr)
    elif cmd == 'kill':
        request_json = json.dumps(kill_request)
        sock.sendto(request_json.encode(), sendto_addr)
    else:
        pass
