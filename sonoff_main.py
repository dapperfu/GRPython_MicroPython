import connect_network

# Connect to the 
# connect_network.connect_network()
ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface

ap_config = {
    "essid": "sonoff-micropython-ap",
    "authmode": network.AUTH_WPA2_PSK,
    "password": "0xdeadbeef",
    "channel": 11,
}
ap.config(**ap_config) # set the ESSID of the access point

import machine

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
relay = machine.Pin(12, machine.Pin.OUT)

led = machine.Pin(13, machine.Pin.OUT)
led_pwm = machine.PWM(led)
led_pwm.freq(1)
led_pwm.duty(512)