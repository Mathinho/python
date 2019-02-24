#pylint:disable=E0401
#pylint:disable=E0602
from machine import Pin
import time

#p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0

#def do_connect():
#    import network
#    wlan = network.WLAN(network.STA_IF)
#    wlan.active(True)
#    if not wlan.isconnected():
#        print('connecting to network...')
#        wlan.connect('albg_wlan', 'boardalpha@0.9.168.192#14albg')
#        while not wlan.isconnected():
#            pass
#    print('network config:', wlan.ifconfig())

#do_connect()

#while True:
#    p0.on()                 # set pin to "on" (high) level
#    time.sleep(1)
#    p0.off()
#    time.sleep(1)

def web_page():
  d.measure()
  if led.value() == 0:
    gpio_state="AN"
  else:
    gpio_state="AUS"
  hum = str(d.humidity())
  
  html = """<html><head> <title>ESP8266 Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p>Luftfeuchtigkeit: <strong>""" + hum + """%</strong></p><p><a href="/?led=on"><button class="button">AN</button></a></p>
  <p><a href="/?led=off"><button class="button button2">AUS</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  #d.measure()
  #print(d.temperature())
  #print(d.humidity())
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(0)
  if led_off == 6:
    print('LED OFF')
    led.value(1)
  response = web_page()
  conn.send(response)

  conn.close()