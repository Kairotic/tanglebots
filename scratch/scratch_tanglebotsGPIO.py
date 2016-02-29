#!/usr/bin/env python
# Scratch interface for explorer hat touch buttons
# Copyright (C) 2016 by Dave Griffiths based on Simon Walters' ScratchGPIO, based on original code for PiFace by Thomas Preston

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import threading
import socket
import time
import sys
import os
import math
import subprocess

# touch code from pimoroni library

from cap1xxx import Cap1208
CAP_PRODUCT_ID = 107

class CapTouchSettings(object):
    type = 'Cap Touch Settings'

    @staticmethod
    def enable_multitouch(en=True):
        _cap1208.enable_multitouch(en)


class CapTouchInput(object):
    type = 'Cap Touch Input'

    def __init__(self, channel, alias):
        self.alias = alias
        self._pressed = False
        self._last_pressed = False
        self._held = False
        self.channel = channel
        self.handlers = {'press': None, 'release': None, 'held': None}
        for event in ['press', 'release', 'held']:
            _cap1208.on(channel=self.channel, event=event, handler=self._handle_state)

    def _handle_state(self, channel, event):
        if channel == self.channel:
            if event == 'press':
                self._pressed = True
            elif event == 'held':
                self._held = True
            elif event in ['release', 'none']:
                self._pressed = False
                self._held = False
            if callable(self.handlers[event]):
                self.handlers[event](self.alias, event)

    def has_changed(self):
        return self._pressed!=self._last_pressed
                
    def is_pressed(self):
        self._last_pressed = self._pressed
        return self._pressed

    def is_held(self):
        return self._held

    def pressed(self, handler):
        self.handlers['press'] = handler

    def released(self, handler):
        self.handlers['release'] = handler

    def held(self, handler):
        self.handlers['held'] = handler

try:
    _cap1208 = Cap1208()
    has_captouch = True
except IOError:
    has_captouch = False

if has_captouch:
    print("Explorer HAT Pro detected...")
    explorer_pro = True

touch=CapTouchSettings()
touch_buttons=[CapTouchInput(4, 1),
               CapTouchInput(5, 2),
               CapTouchInput(6, 3),
               CapTouchInput(7, 4),
               CapTouchInput(0, 5),
               CapTouchInput(1, 6),
               CapTouchInput(2, 7),
               CapTouchInput(3, 8)]
                
class ScratchSender(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.scratch_socket = socket
        self._stop = threading.Event()
        print "Sender Init"
        self.loopCmd = "" # sensor update string
        self.triggerCmd = "" # broadcast update string

    def stop(self):
        self._stop.set()
        print "Sender Stop Set"

    def stopped(self):
        return self._stop.isSet()       

    def addtosend_scratch_command(self, cmd):
        self.loopCmd += " "+ cmd
        
    def send_scratch_command(self, cmd):
        n = len(cmd)
        b = (chr((n >> 24) & 0xFF)) + (chr((n >> 16) & 0xFF)) + (chr((n >>  8) & 0xFF)) + (chr(n & 0xFF))
        self.scratch_socket.send(b + cmd)
        
    def run(self):
        while not self.stopped():
            for i,button in enumerate(touch_buttons):
                if button.has_changed():
                    sensor_name = 'touch'+str(i)
                    val='0'
                    if button.is_pressed(): val='1' 
                    bcast_str = '"' + sensor_name + '" ' + val
                    self.addtosend_scratch_command(bcast_str)
            
            time.sleep(0.05)
            if self.loopCmd <> "":
                self.send_scratch_command("sensor-update " + self.loopCmd)
            if self.triggerCmd <> "":
                self.scratch_socket.send(self.triggerCmd)                
            self.loopCmd = ""
            self.triggerCmd = ""


def create_socket(host, port):
    while True:
        try:
            print 'Trying'
            scratch_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scratch_sock.connect((host, port))
            break
        except socket.error:
            print "There was an error connecting to Scratch!"
            time.sleep(3)

    return scratch_sock

def cleanup_threads(threads):
    print ("cleanup threads started")
    for thread in threads:
        thread.stop()
    print "Threads told to stop"
    for thread in threads:
        thread.join()
    print "Waiting for join on main threads to complete"                
    print ("cleanup threads finished")



#Set some constants and initialise lists

PORT = 42001
DEFAULT_HOST = '127.0.0.1'
BUFFER_SIZE = 8192 #used to be 100
SOCKET_TIMEOUT = 2
lock = threading.Lock()

if __name__ == '__main__':
    SCRIPTPATH = os.path.split(os.path.realpath(__file__))[0]
    print "PATH:" ,SCRIPTPATH
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST
    host = host.replace("'", "")

    GPIOPlus = True
    if len(sys.argv) > 2:
        if sys.argv[2] == "standard":
            GPIOPlus = False
 
cycle_trace = 'start'

while True:

    if (cycle_trace == 'disconnected'):
        print "Scratch disconnected"
        cleanup_threads((sender,))
        print "Thread cleanup done after disconnect"
        INVERT = False
        print ("Pin Reset Done")
        time.sleep(1)
        cycle_trace = 'start'

    if (cycle_trace == 'start'):
        ADDON = ""
        INVERT = False
        # open the socket
        print 'Starting to connect...' ,
        the_socket = create_socket(host, PORT)
        print 'Connected!'
        the_socket.settimeout(SOCKET_TIMEOUT) #removed 3dec13 to see what happens
        sender = ScratchSender(the_socket)
        cycle_trace = 'running'
        print "Running...."
        sender.start()

    # wait for ctrl+c
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print ("Keyboard Interrupt")
        cleanup_threads((sender,))
        print "Thread cleanup done after disconnect"
        #time.sleep(5)
        sys.exit()
        print "CleanUp complete"




