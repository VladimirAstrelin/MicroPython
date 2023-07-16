import tm1637
from machine import Pin
from time import sleep_ms
from machine import RTC

rtc = RTC()
tm = tm1637.TM1637(dio=Pin(21), clk=Pin(22))

rtc.datetime((2023,  7, 16,  7, 14, 15,  0, 0))
# rtc.datetim(YYYY, MM, DD, WD, HH, MM, SS, MS))
# WD 1 = Monday
# WD 7 = Sunday

isPoint = False

while True:
    t = rtc.datetime()
    tm.numbers(t[4], t[5], isPoint)
    sleep_ms(1000)
    isPoint = not isPoint
