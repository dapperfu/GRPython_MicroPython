from machine import Pin
import time

# Pin 0

for pin in [2, 3, 4, 5, 12, 13, 14, 15, 16]:
    print(pin)
    Pin(pin, Pin.OUT).off()
    time.sleep(1)
    