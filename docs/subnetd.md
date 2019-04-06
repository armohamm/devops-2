subnetd - IPv4/6 subnet calculator.

```

---IPv4---

Usage: python3 subnetd.py 208.67.222.222/22
IP Version:  4
Address:    208.67.222.222          11010000.01000011.11011110.11011110
Netmask:    255.255.252.0 = 22   11010000.01000011.11011100.00000000
Wildcard:   0.0.3.255            00000000.00000000.00000011.11111111
=>
Network:    208.67.220.0/22
HostMin:    208.67.220.1
HostMax:    208.67.223.254
Address Space: 1024
Hex conversion:  0xd043dede

---IPv6---

Usage: subnetd.py 2001:4860:4860::8888/48
IP Version:  6
Address:    2001:4860:4860::8888
Netmask:    ffff:ffff:ffff::
Wildcard:   ::ffff:ffff:ffff:ffff:ffff
=>
Network:    2001:4860:4860::/48
Broadcast:  2001:4860:4860:ffff:ffff:ffff:ffff:ffff
HostMin:    2001:4860:4860::1
HostMax:    2001:4860:4860:ffff:ffff:ffff:ffff:fffe
Address Space: 1208925819614629174706176

```