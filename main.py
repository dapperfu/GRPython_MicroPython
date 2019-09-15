import machine

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

green_pwm = machine.PWM(green)
blue_pwm = machine.PWM(blue)
red_pwm = machine.PWM(red)

red_pwm.freq(1)
green_pwm.freq(1)
blue_pwm.freq(1)

# Light Sensor.
adc = machine.ADC(0)

import network
import secrets
import time

def connect_network():
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    wlan.connect(secrets.network, secrets.password)  # connect to an AP
    print("Connecting to wifi '{}'".format(secrets.network), end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("... Done!")
    print(wlan.ifconfig())  # get the interface's IP/netmask/gw/DNS addresses

connect_network()
import urequests

while True:
    try:
        r=urequests.get("http://192.168.8.193:5000/light_sensor/{}".format(adc.read()))
        green_pwm.duty(int(r.json()["green"]))
    except KeyboardInterrupt:
        break
    except:
        pass
    time.sleep(1)
