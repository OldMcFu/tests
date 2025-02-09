import socket
import time
import threading

def send_binary_file_over_udp(file_path, sender_addr, receiver_list:list, packet_size, trigger_event:threading.Event, kill_event:threading.Event,suspend_event:threading.Event):
    # Create a UDP socket
    t_offset = 20.0/1000.0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(sender_addr)
    # Open the binary file in binary mode
    print("Wait for Trigger!")
    trigger_event.wait()
    print("Trigger was set!")
    while not kill_event.is_set():
        with open(file_path, 'rb') as f:
            # Read the file in fixed-size packets
            t1 = time.clock_gettime(time.CLOCK_REALTIME)
            t2 = time.clock_gettime(time.CLOCK_REALTIME)
            while not kill_event.is_set():
                if suspend_event.is_set():
                    time.sleep(0.010)
                else:
                    t1 = t1 + t_offset
                    data = f.read(packet_size)
                    if not data:
                        break
                    t_sleep = t1 - time.clock_gettime(time.CLOCK_REALTIME)
                    if t_sleep < 0.0: t_sleep = 0.0
                    time.sleep(t_sleep)
                    # Send each packet to the specified host and port
                    for receiver in receiver_list:
                        sock.sendto(data, receiver)
                    

# Example usage
#file_path = 'path/to/your/binary/file'
#host = '127.0.0.1'
#port = 12345
#packet_size = 1024
#send_binary_file_over_udp(file_path, host, port, packet_size)
