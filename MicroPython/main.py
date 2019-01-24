from machine import Pin
import time

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('albg_wlan', 'boardalpha@0.9.168.192#14albg')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

while True:
    p0.on()                 # set pin to "on" (high) level
    time.sleep(1)
    p0.off()
    time.sleep(1)