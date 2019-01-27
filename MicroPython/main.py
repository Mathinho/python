#pylint:disable=E0401
#pylint:disable=E1101

import machine, time, ssd1306, math

servo = machine.PWM(machine.Pin(13), freq=50)

i2c = machine.I2C(-1, machine.Pin(14), machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3d)

led = machine.PWM(machine.Pin(0), freq=50)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:
    for i in range(39, 116, 5):
        servo.duty(i)
        i = i + 1
        oled.fill(0)
        oled.text("Servo: " + str(i) + " Grad", 0, 0)
        oled.show()
        #time.sleep(1)
        pulse(led, 60)