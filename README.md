### Command Line Network Automation Tools.
A repo for network automation of design, deployment, and operations tasks.

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
