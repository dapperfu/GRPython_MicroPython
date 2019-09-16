import machine

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
relay = machine.Pin(12, machine.Pin.OUT)

led = machine.Pin(13, machine.Pin.OUT)
led_pwm = machine.PWM(led)
led_pwm.freq(1)
led_pwm.duty(512)

