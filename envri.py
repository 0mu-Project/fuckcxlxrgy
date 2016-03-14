#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0muWatchdog runtime environment
import sys
import os
import socket
import subprocess
from setting import port
# check version_info of python 
def checkenvir():
    if sys.version_info[0] == 3:
        # if use pypy3 will have this sys builtin
        is_pypy = '__pypy__' in sys.builtin_module_names
        if is_pypy is True:
            try:
                import flask
                return 'pypy3'
            except ImportError:
                try:
                    import pip  # NOQA
                    print('You dont have flask install , Auto Install!')
                    print('Please enter root password !')
                    # call subprocess to install unfound modules
                    subprocess.call(['sudo pypy3 -m pip install Flask'], shell=True)
                    subprocess.call(['sudo pypy3 -m pip install six'], shell=True)
                except ImportError:
                    print('You dont have pip install , please input your password to install ')
                    subprocess.call(['curl -s https://bootstrap.pypa.io/get-pip.py |sudo pypy3'], shell=True)
                return 'pypy3'
        else:
            try:
                import flask  # NOQA
                return 'python3'
            except ImportError:
                print('You dont have flask install , please input your password to install flask . ')
                # call subprocess to install unfound modules
                subprocess.call(['sudo python3 -m pip install Flask'], shell=True)
                subprocess.call(['sudo python3 -m pip install six'], shell=True)
                return 'python3'
    else:
        return 'python2'

# run master branch git pull to update server
def rungitpull():
    print('# Git status')
    subprocess.call(['git pull'], shell=True)

# use subprocess to call MDAUServer
def importapp():
    subprocess.call([checkenvir() + ' MDAUServer.py'], shell=True)
    subprocess.call([checkenvir() + ' NTFServer.py'], shell=True)

# use socket to check port open
def portcheck(portch):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        return s.connect_ex(('localhost', portch)) != 0
    finally:
        s.close()

# Main class 
if __name__ == '__main__':
    # loop for all time
    while 1:
        rungitpull()
        print('Now 0mu-WatchDog is run')
        if portcheck(port):
            importapp()
