import json
import socket
import threading

def receive_jsonrpc_requests_over_udp(host, port, trigger_event:threading.Event, kill_event:threading.Event,suspend_event:threading.Event):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified host and port
    sock.bind((host, port))

    while not kill_event.is_set():
        # Receive a JSON-RPC request as a byte string
        data, addr = sock.recvfrom(65000)

        # Parse the byte string as JSON
        request = json.loads(data)

        process_jsonrpc_request(request, trigger_event, kill_event,suspend_event)

def process_jsonrpc_request(request, trigger_event:threading.Event, kill_event:threading.Event,suspend_event:threading.Event):
    # Extract the method name and parameters from the request
    method = request['method']
    params = request['params']

    # Handle the method
    if method == 'trigger':
        trigger_event.set()
    elif method == 'kill':
        kill_event.set()
    elif method == "suspend":
        if suspend_event.is_set():
            suspend_event.clear()
        else:
            suspend_event.set()
    else:
        print({'error': {'code': -32601, 'message': 'Method not found'}})

# Example usage
#host = '127.0.0.1'
#port = 12345
#receive_jsonrpc_requests_over_udp(host, port)
