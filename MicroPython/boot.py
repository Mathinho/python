#pylint:disable=E0401

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import machine, network, esp

esp.osdebug(None)

import gc
gc.collect()

#ssid = 'WLAN-NJ7XPS'
#password = '3928154662345212'

ssid = 'albg_wlan'
password = 'boardalpha@0.9.168.192#14albg'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())