#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dexter's Device Logger Utility, Version 1.0, by Dexter Park.
   Learn more: https://github.com/ddexterpark/neteng"""

import logging, sys

# Creates a root logger for monitoring your program's events.
fileLogger = logging.getLogger()
fileLogger.setLevel(logging.DEBUG)

# Call the console handler when you only want to see log messages in your terminal window.
def console():
    consoleFormatStr = "[%(asctime)s, %(threadName)s, %(levelname)s] %(message)s"
    # Stream Handler for stdout, stderr
    consoleFormatter = logging.Formatter(consoleFormatStr)
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(consoleFormatter)
    consoleHandler.setLevel(logging.INFO)
    fileLogger.addHandler(consoleHandler)

# Call setup handler when you want to see log messages in your terminal window AND save the output to a file.
def setup(logFile):
    global fileLogger
    logFormatStr = "[%(asctime)s %(threadName)s, %(levelname)s] %(message)s"

    # File Handler for log file
    logFormatter = logging.Formatter(logFormatStr)
    fileHandler = logging.FileHandler(logFile )
    fileHandler.setFormatter( logFormatter )
    fileLogger.addHandler( fileHandler )

    # Stream Handler for console (stdout, stderr)
    console()

# Call event when you want to create log messages regardless of which handler you prefer.
def event( string, level='debug',print_screen=False, remove_newlines=False ):
    switch_log_levels = {'debug': fileLogger.debug,'info': fileLogger.info,'warning': fileLogger.warning,
                         'error': fileLogger.error, 'critical': fileLogger.critical}

    if remove_newlines:
        string = string.replace('\r', '').replace('\n', ' ')

    if print_screen:
        switch_log_levels[level](string)

    switch_log_levels[level](string)