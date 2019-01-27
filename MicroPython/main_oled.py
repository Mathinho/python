#pylint:disable=E0602
#pylint:disable=E0401
#pylint:disable=E1101

import time, machine, ssd1306, dht, math

i2c = machine.I2C(-1, machine.Pin(14), machine.Pin(12))
#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
#oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3d)

p0 = Pin(0, Pin.OUT)

led = machine.PWM(machine.Pin(0), freq=1000)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:    
    d.measure()
    oled.fill(0)
    oled.text("Temperatur:  " + str(d.temperature()) + "C", 0, 0)
    oled.text("Luftfeuchte: " + str(d.humidity()) + "%", 0, 10)
    oled.text(str(machine.freq()), 0, 20)
    oled.show()
    pulse(led, 60)