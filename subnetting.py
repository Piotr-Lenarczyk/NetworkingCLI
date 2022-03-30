import ipaddress


def subnetting(cidr):
    network = ipaddress.IPv4Network(cidr)
    network_addr = "Network address: " + str(network.network_address)
    first_host = "First host: " + str(network[1])
    last_host = "Last host: " + str(network[len(list(network.hosts())) - 1])
    subnet_mask = "Subnet mask: " + str(network.netmask)
    broadcast_addr = "Broadcast address: " + str(network[len(list(network.hosts()))])
    print(network_addr)
    print(first_host)
    print(last_host)
    print(subnet_mask)
    print(broadcast_addr)
