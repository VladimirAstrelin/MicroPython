import machine
led = machine.Pin(2,machine.Pin.OUT)
led.off()

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  if led.value()==1:
    led_state = 'ON'
    print('led is ON')
  elif led.value()==0:
    led_state = 'OFF'
    print('led is OFF')
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body>
  <center><h2>ESP32 Web Server in MicroPython </h2></center>   
       <center>   
        <form>   
         <button type='submit' name="LED" value='1'> LED ON </button>   
         <button type='submit' name="LED" value='0'> LED OFF </button>   
        </form>   
       </center>   
       <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>
  </body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  led_on = request.find('/?LED=1')
  led_off = request.find('/?LED=0')
  if led_on == 6:
    print('LED ON')
    print(str(led_on))
    led.value(1)
  elif led_off == 6:
    print('LED OFF')
    print(str(led_off))
    led.value(0)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
#   conn.send('HTTP/1.1 200 OKn')
#   conn.send('Content-Type: text/htmln')
#   conn.send('Connection: close\n')
#   conn.sendall(response)
  conn.close()
