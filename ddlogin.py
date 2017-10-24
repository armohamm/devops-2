#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dexter's Device Login Utility, Version 1.0, by Dexter Park.
   Learn more: https://github.com/ddexterpark/neteng

   Paramiko-based ssh utility that connects to a list of devices (in parallel) and executes commands.

   Examlple: ddlogin.py -u admin -p password -l 192.168.1.1 -c dmesg 'uname -a' -o"""

import argparse, ddlog, os, paramiko, sys
from threading import Thread
from queue import Queue

def main(hostlist):
    global username, password, commands, output

    path = os.getcwd() + '//logs/'
    file = hostlist + '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    if output is True:
        ddlog.setup(path+file)
    else:
        ddlog.console()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostlist, username=username, password=password)
    except paramiko.AuthenticationException:
        ddlog.event("[-] Failed to Authenticate.",'error')
        pass
    except paramiko.SSHException:
        ddlog.event("[-] An SSH exception was raised. Check clients ssh settings.",'error') #, exc_info=True)
        pass
    except TimeoutError:
        ddlog.event("[-] host is not reachable.",'error')
        pass

    host = hostlist.strip('\n')
    ddlog.event('[+] successfully connected to ' + host,'info')

    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
        lines = iter(stdout.readline, "")
        for line in lines:
            ddlog.event('[+] '+line,'info')
        stdin.close()

try:
    if __name__ == "__main__":
            parser = argparse.ArgumentParser(description='Optional switches',prefix_chars='-+/',)
            parser.add_argument('-u', '--username', action='store', dest='username', help='The ssh username.')
            parser.add_argument('-p', '--password', action='store', dest='password', help='The ssh password.')
            parser.add_argument('-o', '--output', action='store_true', default=False, dest='output', help='Boolean switch for storing logs to file.')
            parser.add_argument('-l', '--hostlist', nargs='+',action='store', dest='hostlist', help='List of devices to interact with.')
            parser.add_argument('-c', '--commands', nargs='+',action='store', dest='commands', help='An exact list of commands to run.')
            args = parser.parse_args()
            username = args.username
            password = args.password
            output = args.output
            hostlist = args.hostlist
            commands = args.commands

            class ParallelConnections(Thread):
                def __init__(self, queue):
                    Thread.__init__(self)
                    self.queue = queue

                def run(self):
                    while True:
                        host = self.queue.get()
                        main(host)
                        self.queue.task_done()

            thread_count = 4
            queue = Queue()

            for i in range(thread_count):
                Parallel = ParallelConnections(queue)
                Parallel.daemon = True
                Parallel.start()

            for host in hostlist:
                queue.put(host)

            queue.join()
except KeyboardInterrupt:
    sys.exit('[-] Process aborted by user input')