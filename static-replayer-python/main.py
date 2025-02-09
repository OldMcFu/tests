import threading
import jsonrpc
import replayer


def main():
    # Create an Event object
    trigger_event = threading.Event()
    kill_event = threading.Event()
    suspend_event = threading.Event()
    jsonrpc_ip = "127.0.0.1"
    jsonrpc_port = 50000
    
    replayer_ip = ("127.0.0.1", 0)
    binary_file_path = "myfile.bin"
    package_size = 10
    replayer_receiver_list = [("127.0.0.1", 60000), ("127.0.0.1", 60001), ("127.0.0.1", 60002)]
    thread1 = threading.Thread(target=jsonrpc.receive_jsonrpc_requests_over_udp, args=(jsonrpc_ip, jsonrpc_port, trigger_event,kill_event,suspend_event,))
    thread2 = threading.Thread(target=replayer.send_binary_file_over_udp, args=(binary_file_path, replayer_ip, replayer_receiver_list, package_size, trigger_event,kill_event,suspend_event,))
    
    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()
if __name__ == "__main__":
    main()