#pylint:disable=E0602
#pylint:disable=E0401
#pylint:disable=E1101

import time, machine, ssd1306, dht
from neopixel import NeoPixel

i2c = machine.I2C(-1, machine.Pin(14), machine.Pin(12))
#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
#oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3d)

p0 = Pin(0, Pin.OUT)

neo = Pin(13, Pin.OUT)
np = NeoPixel(neo, 16)

while True:
    d.measure()
    oled.fill(0)
    oled.text("Temperatur:  " + str(d.temperature()) + "C", 0, 0)
    oled.text("Luftfeuchte: " + str(d.humidity()) + "%", 0, 10)
    oled.show()
    p0.on()                 # set pin to "on" (high) level
    np[0] = (0, 0, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    np[5] = (0, 0, 0)
    np[6] = (0, 0, 0)
    np[7] = (0, 0, 0)
    np[8] = (0, 0, 0)
    np[9] = (0, 0, 0)
    np[10] = (0, 0, 0)
    np[11] = (0, 0, 0)
    np[12] = (0, 0, 0)
    np[13] = (0, 0, 0)
    np[14] = (0, 0, 0)
    np[15] = (0, 0, 0)
    np.write()
    time.sleep(0.99)
    p0.off()
    np[0] = (10, 10, 10)
    np[1] = (10, 10, 10)
    np[2] = (10, 10, 10)
    np[3] = (10, 10, 10)
    np[4] = (10, 10, 10)
    np[5] = (10, 10, 10)
    np[6] = (10, 10, 10)
    np[7] = (10, 10, 10)
    np[8] = (10, 10, 10)
    np[9] = (10, 10, 10)
    np[10] = (10, 10, 10)
    np[11] = (10, 10, 10)
    np[12] = (10, 10, 10)
    np[13] = (10, 10, 10)
    np[13] = (10, 10, 10)
    np[14] = (10, 10, 10)
    np[15] = (10, 10, 10)
    np.write()
    time.sleep_ms(10)