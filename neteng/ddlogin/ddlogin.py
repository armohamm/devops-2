#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dexter's Device Login Utility, Version 1.0, by Dexter Park.
   Learn more: https://github.com/ddexterpark/neteng

   Paramiko-based ssh utility that connects to a list of devices (in parallel) and executes commands.

   Examlple: ddlogin.py -u admin -p password -l 192.168.1.1 -c dmesg 'uname -a' -o"""

import argparse
import os
import sys
from queue import Queue
from threading import Thread

import paramiko

from neteng.ddlogin import helper


def main(hostlist):
    global username, password, commands, output

    # Option for logging.
    path = os.getcwd() + "//data/"
    file = hostlist + ' ' + helper.timestamp() + '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    if output is True:
        helper.setup(path + file, 'info')
    else:
        helper.console('info')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostlist, username=username, password=password)
    except paramiko.AuthenticationException:
        helper.event("[-] Failed to Authenticate.", 'error')
        pass
    except paramiko.SSHException:
        helper.event("[-] An SSH exception was raised. Check clients ssh settings.", 'error')
        pass
    except TimeoutError:
        helper.event("[-] host is not reachable.", 'error')
        pass

    host = hostlist.strip('\n')
    helper.event('[+] successfully connected to ' + host, 'info')

    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
        lines = iter(stdout.readline, "")
        for line in lines:
            helper.event('[OUTPUT] ' + line, 'info')
        stdin.close()


if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Optional switches', prefix_chars='-+/',)
        parser.add_argument('-u', '--username', action='store', dest='username', help='The ssh username.')
        parser.add_argument('-p', '--password', action='store', dest='password', help='The ssh password.')
        parser.add_argument('-o', '--output', action='store_true', default=False, dest='output',
                            help='Boolean switch for storing logs to file.')
        parser.add_argument('-l', '--hostlist', nargs='+', action='store', dest='hostlist',
                            help='List of devices to interact with.')
        parser.add_argument('-c', '--commands', nargs='+', action='store', dest='commands',
                            help='An exact list of commands to run.')
        args = parser.parse_args()
        username = args.username
        password = args.password
        output = args.output
        hostlist = args.hostlist
        commands = args.commands

        try:
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