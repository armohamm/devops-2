from netaddr import IPAddress, IPNetwork
from subprocess import run
import sys

run("pip3 install netaddr", shell=True, check=True)

# https://media.readthedocs.org/pdf/netaddr/latest/netaddr.pdf
# netaddr has so much potential for future scripts such as re-iping, and IPAM. Must investigate further.


def main(subnet):
    ipn =  IPNetwork(subnet)
    ip = IPAddress(ipn.value)
    if ipn.version == 4:
        print('IP Version: ', ipn.version)
        print('Address:   ', ipn.ip, '        ', ipn.ip.bits())
        print('Netmask:   ', ipn.netmask, '=', ipn._prefixlen, ' ',ipn.network.bits())
        print('Wildcard:  ', ipn.hostmask, '          ',ipn.hostmask.bits())
        print('=>')
        print('Network:   ', ipn.cidr)
        print('HostMin:   ', ipn.network + 1)
        print('HostMax:   ', ipn.broadcast-1)
        print('Address Space:', ipn.size)
        print('Hex conversion: ', ip.__hex__())
    else:
        print('IP Version: ', ipn.version)
        print('Address:   ', ipn.ip)
        print('Netmask:   ', ipn.netmask)
        print('Wildcard:  ', ipn.hostmask)
        print('=>')
        print('Network:   ', ipn.cidr)
        print('Broadcast: ', ipn.broadcast)
        print('HostMin:   ', ipn.network + 1)
        print('HostMax:   ', ipn.broadcast-1)
        print('Address Space:', ipn.size)

if __name__ == "__main__":
    subnet = sys.argv[1] if len(sys.argv) > 1 else sys.exit(0)
    main(subnet)