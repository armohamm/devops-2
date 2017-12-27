### DevOps Tools for NetEng Automation.

![screenshot](devops.png)

# Suggested Platform and Software  

MacBook:
https://www.apple.com/macbook-pro/

PyCharm:
https://www.jetbrains.com/pycharm/download/

Docker:
https://docs.docker.com/engine/getstarted/

### Clone this repo

Use Git or your favorite IDE to clone this project. In PyCharm, use the GitHub option on the new project screen.          
 

# Command Line Tools  
ddlogin - A command line ssh tool that can execute commands against remote hosts (in parallel), and provides logging options for output.   
```
Usage:
ddlogin.py -u admin -p Passw0rd -h hostlist.txt -c commands.txt -o

ddlogin.py -u admin -p Passw0rd -h 192.168.1.2 -c 'show version' -o
```
ddlog - A simple, reusable logging module.   

```
import ddlog

path = os.getcwd() + '//logs/'
    file = hostlist +' '+ ddlog.timestamp()+'.log'
    if not os.path.exists(path):
        os.makedirs(path)
    if output is True:
        ddlog.setup(path+file, 'info')
    else:
        ddlog.console('info')

 
 ddlog.event("[-] Failed to Authenticate. ",'error')
 ddlog.event("[+] Authentication successful! ",'info')
```

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
