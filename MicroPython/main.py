import ili9341, time, bitmapfont, math
from machine import Pin, SPI
from rgb import color565
hspi = SPI(1, 80000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
display = ili9341.ILI9341(hspi, cs=Pin(15), dc=Pin(4), rst=Pin(16))
display.fill(color565(255, 0, 0))
time.sleep(0.1)
display.fill(0)
time.sleep(0.1)
display.pixel(200, 200, color565(255, 255, 255))
time.sleep(0.1)
display.fill_rectangle(0, 0, 120, 170, color565(0, 0, 255))
display.hline(100, 20, 100, color565(0, 255, 0))
display.vline(100, 20, 100, color565(0, 255, 0))

bf = bitmapfont.BitmapFont(320, 240, display.pixel)
bf.init()
bf.text('test', 0, 0, 2)
bf.text('hallo Marta', 100, 200, 500)