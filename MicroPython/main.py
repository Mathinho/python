#pylint:disable=E0602
#pylint:disable=E0401

import time, machine, ssd1306, dht

i2c = machine.I2C(-1, machine.Pin(14), machine.Pin(12))
#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
#oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3d)

p0 = Pin(0, Pin.OUT)

while True:
    d.measure()
    oled.fill(0)
    oled.text("Temperatur:  " + str(d.temperature()) + "C", 0, 0)
    oled.text("Luftfeuchte: " + str(d.humidity()) + "%", 0, 10)
    oled.show()
    p0.on()                 # set pin to "on" (high) level
    time.sleep(0.99)
    p0.off()
    time.sleep_ms(10)