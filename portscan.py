import socket
import threading
import time


def port(ip, i):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, i))
        print("Port %d is open!" % i)
        s.close()
    except socket.error:
        return


def port_scan(ip, first, last):
    print("Starting a TCP scan...")
    start_time = time.time()
    for i in range(first, last + 1):
        thread = threading.Thread(target=port, args=(ip, i))
        thread.start()
    print("Scan of %d ports took %.3fs" % (last + 1 - first, time.time() - start_time))
    return
