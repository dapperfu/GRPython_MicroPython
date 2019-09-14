import machine

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("woke from a deep sleep")
green = machine.Pin(12)
green.off()

blue_pin = 13
blue = machine.Pin(blue_pin)
blue.off()

red_pin = 15
red = machine.Pin(red_pin)
red.off()

# Light Sensor.
from machine import ADC

adc = ADC(0)

import network
import secrets
import time


def connect_network():
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    wlan.connect(secrets.network, secrets.password)  # connect to an AP
    while not wlan.isconnected():
        time.sleep(1)
    print(wlan.config("mac"))  # get the interface's MAC adddress
    print(wlan.ifconfig())  # get the interface's IP/netmask/gw/DNS addresses

connect_network()
import urequests

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
# rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
# machine.deepsleep()

try:
    urequests.get("http://192.168.8.228:5000/light_sensor/{}".format(adc.read()))
except:
    pass
