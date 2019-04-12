from machine import I2C, Pin
from ntptime import settime
import ssd1306, utime, gfx

rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
graphics = gfx.GFX(128, 64, oled.pixel)

settime()

while True:
        x = 1
        oled.fill(0)
        while x < 128:
                zeit = utime.localtime()
                oled.fill(0)
                graphics.fill_circle(x, 47, 2, 1)
                x = x + 1
                oled.text('ESP32', 45, 5)
                oled.text('MicroPython', 20, 20)
                oled.text(str("{:02d}".format(zeit[3] + 2)) + ':' + str("{:02d}".format(zeit[4])) , 0, 56)
                oled.text(str("{:02d}".format(zeit[2])) + '.' + str("{:02d}".format(zeit[1])) + '.' + str("{:02d}".format(zeit[0] - 2000)), 60, 56)
                graphics.line(0, 50, 128, 50, 2)
                oled.show()
                utime.sleep_ms(50)
                if x > 128:
                        x = 1