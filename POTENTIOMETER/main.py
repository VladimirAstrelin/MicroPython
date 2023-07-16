from machine import Pin, ADC, PWM
from time import sleep_ms
from mapper import map

p32 = Pin(32, Pin.IN)

pot = ADC(p32)  # 'pot' stands for potentiometer
pot.atten(ADC.ATTN_11DB)  # attenuation 

p2 = Pin(2, Pin.OUT)
led = PWM(p2)
led.freq(60)

while True:
    pot_value = pot.read() # 0 - 4095
    pwm_value = map(pot_value, 0, 4095, 0, 1023)
    led.duty(pwm_value)    # 0 - 1023
    sleep_ms(500)
    print(pot_value)
