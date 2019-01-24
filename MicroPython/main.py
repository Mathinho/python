from machine import pin
import time

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
time.sleep(100)
p0.off()
time.sleep(100)