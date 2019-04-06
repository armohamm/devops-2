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