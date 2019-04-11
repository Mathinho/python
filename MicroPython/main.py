from machine import I2C, Pin
from ntptime import settime
import ssd1306, utime

rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

settime()

while True:
        zeit = utime.localtime()
        oled.fill(0)
        oled.text('ESP32', 45, 5)
        oled.text('MicroPython', 20, 20)
        oled.text(str("{:2d}".format(zeit[3] + 2)) + ':' + str("{:2d}".format(zeit[4])) + ':' + str("{:2d}".format(zeit[5])), 0, 45)
        oled.text(str("{:2d}".format(zeit[2])) + '.' + str("{:2d}".format(zeit[1])) + '.' + str(zeit[0]), 0, 55)
        oled.show()
        time.sleep(1)