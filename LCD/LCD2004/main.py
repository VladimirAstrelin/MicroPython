from time import sleep_ms, ticks_ms 
from machine import I2C, Pin 
from i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27  # 0x3F
gpio_state = "ON"

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)


# I2C Scanner:
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
for device in devices:
  print("At address: ",hex(device))
  
def display():
  lcd.clear()
  lcd.move_to(0, 0)
  lcd.putstr(f"I2C:{str(hex(device))}")
  lcd.move_to(0, 1)
  lcd.putstr(f"LED:{gpio_state}")
  lcd.move_to(0, 2)
  lcd.putstr(f"IP :{str(station.ifconfig()[0])}")
  
  

# Complete project details at https://RandomNerdTutorials.com

def web_page():
  global gpio_state
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
  display()
  


# The following line of code should be tested
# using the REPL:

# 1. To print a string to the LCD:
#    lcd.putstr('Hello world')
# 2. To clear the display:
#	 lcd.clear()
# 3. To control the cursor position:
# 	 lcd.move_to(2, 1)
# 4. To show the cursor:
#  	 lcd.show_cursor()
# 5. To hide the cursor:
#	 lcd.hide_cursor()
# 6. To set the cursor to blink:
#	 lcd.blink_cursor_on()
# 7. To stop the cursor on blinking:
#	 lcd.blink_cursor_off()
# 8. To hide the currently displayed character:
#	 lcd.display_off()
# 9. To show the currently hidden character:
#	 lcd.display_on()
# 10. To turn off the backlight:
#	 lcd.backlight_off()
# 11. To turn ON the backlight:
#	 lcd.backlight_on()
# 12. To print a single character:
#	 lcd.putchar('x')
# 13. To print a custom character:
#	 happy_face = bytearray([0x00, 0x0A, 0x00, 0x04, 0x00, 0x11, 0x0E, 0x00])
#	 lcd.custom_char(0, happy_face)
#	 lcd.putchar(chr(0))
