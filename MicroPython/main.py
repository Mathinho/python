import ili9341
import time
from machine import Pin, SPI
from rgb import color565
#spi = SPI(mosi=Pin(13), sck=Pin(14), miso=Pin(12))
#hspi = SPI(1, 80000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
vspi = SPI(2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
display = ili9341.ILI9341(vspi, cs=Pin(15), dc=Pin(4), rst=Pin(16))
display.fill(color565(255, 0, 0))
#display.fill(ili9341.color565(0xff, 0x11, 0x22))
#display.pixel(120, 160, 0)
time.sleep(1)
display.fill(0)
time.sleep(1)
display.pixel(200, 200, color565(255, 255, 255))
time.sleep(1)
display.fill_rectangle(0, 0, 120, 170, color565(0, 0, 255))
#display.text('test', 100, 100, 100)
#text(display, "test", 100, 100)
display.hline(100, 20, 100, color565(0, 255, 0))
display.vline(100, 20, 100, color565(0, 255, 0))