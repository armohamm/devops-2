#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dexter's Device Logger Utility, Version 1.0, by Dexter Park.
   Learn more: https://github.com/ddexterpark/devops"""

import logging, sys, time, datetime, pyshark

# Display timestamp.
def timestamp():
    format_time = "on {:%a, %d %b %Y at %I.%M%p}, PST".format(datetime.datetime.now())
    return format_time

# Creates a root logger for monitoring your program's events.
fileLogger = logging.getLogger()
fileLogger.setLevel(logging.DEBUG)

# Dictionary for filtering log messages by severity.
logMessages = {'debug': logging.DEBUG,
                'info': logging.INFO,
                'warning': logging.WARNING,
                'error': logging.ERROR,
                'critical': logging.CRITICAL}

# Call the console handler when you only want to see log messages in your terminal window.
def console(setLevel):
    # Formats the console messages
    consoleFormatStr = "[%(asctime)s, %(threadName)s, %(levelname)s] %(message)s"

    # Stream Handler for stdout, stderr
    consoleFormatter = logging.Formatter(consoleFormatStr)
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(consoleFormatter)

    # Switch for filtering console log messages.
    filterConsoleHandler = logMessages.get(setLevel, logging.DEBUG)
    consoleHandler.setLevel(filterConsoleHandler)

    #consoleHandler.setLevel(setLevel)
    fileLogger.addHandler(consoleHandler)

# Call setup handler when you want to see log messages in your terminal window AND save the output to a file.
def setup(logFile, setLevel):
    global fileLogger
    logFormatStr = "[%(asctime)s %(threadName)s, %(levelname)s] %(message)s"

    # File Handler for log file
    logFormatter = logging.Formatter(logFormatStr)
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setFormatter(logFormatter)

    # Switch for filtering file handler messages.
    filterFileHandler = logMessages.get(setLevel, logging.DEBUG)

    fileHandler.setLevel(filterFileHandler)
    fileLogger.addHandler(fileHandler)

    # Stream Handler for console (stdout, stderr)
    console(setLevel)

# Call event when you want to create log messages regardless of which handler you prefer.
# Example:  ddlog.event('[+] test message', 'info')
def event( string, level='debug'):
    switchLogLevels = {'debug': fileLogger.debug,'info': fileLogger.info,'warning': fileLogger.warning,
                         'error': fileLogger.error, 'critical': fileLogger.critical}
    switchLogLevels[level](string)

# (PreReq = setup or console), call pcap when you want to take a packet capture and save it as a .pcap
def pcap(interface):
        capture = pyshark.LiveCapture(interface=interface)
        capture.sniff(timeout=50)
        for packet in capture.sniff_continuously(packet_count=5):
            event('Just arrived:' + packet, 'info')