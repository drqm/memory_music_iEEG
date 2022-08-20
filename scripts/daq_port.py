import os
os.chdir('~/LinuxDrivers/USB/python')
from usb_1208FS import *
usb1208FS = usb_1208FS()
def daq_write(val,chan=0):
      value = int(val,16)
      usb1208FS.AOut(chan,value)
