import ipaddress
import pythonping
import threading


def ping(host):
    if pythonping.ping(str(host), verbose=False).success():
        print("Host %s is up" % host)
    return


def ping_sweep(cidr):
    hosts = list(ipaddress.IPv4Network(cidr).hosts())
    print("Starting a ping sweep of %s network..." % ipaddress.IPv4Network(cidr))
    for host in hosts:
        thread = threading.Thread(target=ping, args=[host])
        thread.start()
    return
