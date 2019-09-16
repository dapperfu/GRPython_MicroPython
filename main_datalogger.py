import machine
import time

from machine import Pin
# Tri-color LED.
for pin in range(12,16):
    Pin(pin, Pin.OUT).off()

green = Pin(12, Pin.OUT)
green.off()
blue_pin = 13
blue = machine.Pin(blue_pin, Pin.OUT)
blue.off()
red_pin = 15
red = machine.Pin(red_pin, Pin.OUT)
red.off()

# Fancy bootup sequence.
time.sleep(0.5)
red.on()
time.sleep(0.5)
red.off()
green.on()
time.sleep(0.5)
green.off()
blue.on()
time.sleep(0.5)
blue.off()

green_pwm = machine.PWM(green)
blue_pwm = machine.PWM(blue)
red_pwm = machine.PWM(red)

# Light Sensor.
adc = machine.ADC(0)

import network
import secrets
import time

from connect_network import connect_network
connect_network()

import urequests

while True:
    try:
        # If the internet is down, this doesn't work so great.
"""
        r=urequests.get("http://192.168.8.193:5000/light_sensor/{}".format(adc.read()))
        green_pwm.freq(1)
        green_pwm.duty(int(r.json()["green"]))
"""
        # "Edge Computing"
        green_pwm.freq(1)
        
    except KeyboardInterrupt:
        break
    except:
        pass
    time.sleep(1)
