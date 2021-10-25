from machine import Pin
import time

led = Pin(25, Pin.OUT)

def dot():
    led.value(1) #1
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.5)

while True:
    for x in range(30):
        dot()
    # wait half an hour = 1800s
    time.sleep(1800)