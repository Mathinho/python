from machine import Pin
import time

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0

while True:
    p0.on()                 # set pin to "on" (high) level
    time.sleep(1)
    p0.off()
    time.sleep(1)