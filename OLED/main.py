import ssd1306
import machine
import time

scl = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(21, machine.Pin.OUT, machine.Pin.PULL_UP)

i2c = machine.I2C(scl=scl, sda=sda, freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

def print_text(msg, x, y, clr):
    if clr:
        oled.fill(0)
    oled.text(msg, x, y)
    oled.show()
    
def my_rect(x, y, w, h, col):
    oled.framebuf.rect(x, y, w, h, col)
    oled.show()
    
# отображение текста на экране (x, y, флаг ( если 1, то очистить
# предварительно экран от предыдущего изображения )
print_text('Hello 12345', 10, 10, 0)
print_text('Welcome', 20, 20, 1)

# вывод логотипа MicroPython на экран
oled.fill(0)
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)
oled.text('MicroPython', 40, 0, 1)
oled.text('SSD1306', 40, 12, 1)
oled.text('OLED 128x64', 40, 24, 1)
oled.show()

