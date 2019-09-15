import machine
from machine import ADC, Pin, PWM


adc = ADC(0)

gpio5 = Pin(5, Pin.IN, Pin.PULL_UP)

import time

while True:
    print(time.time(), end=", ")
    print(adc.read(), end=", ")
    print(gpio5.value(), end=",\n")
    time.sleep(1)