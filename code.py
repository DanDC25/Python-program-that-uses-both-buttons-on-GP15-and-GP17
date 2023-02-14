# Write your code here :-)
from machine import pin
from adafruit_circuitplayground.express import cpx
import time

cpx.pixels.brightness = 0.1
cpx.pixels.fill((0, 0, 0))
cpx.pixels.show()

button_a = Pin(15, Pin.OUT)
button_b = Pin(17, Pin.IN, Pin.PULL_DOWN)

def buttonA_Pressed():
    button_a = True

def buttonB_Pressed():
    button_b = True

if buttonA_Pressed():
    for j in range(4):
        cpx.pixels[0] = (0,0,0)
        cpx.pixels[1] = (0,0,0)
        cpx.pixels[2] = (0,0,0)
        cpx.pixels[3] = (0,0,0)
        cpx.pixels[4] = (0,0,0)
        cpx.pixels[5] = (0,0,0)
        cpx.pixels[6] = (0,0,0)
        cpx.pixels[7] = (0,0,0)
        cpx.pixels[8] = (0,0,0)
        cpx.pixels[9] = (0,0,0)
        time.sleep(0.5)


if buttonB_pressed():
    for i in range(4):
        cpx.pixels[0] = (255,0,0)
        cpx.pixels[1] = (255,0,0)
        cpx.pixels[2] = (255,0,0)
        cpx.pixels[3] = (255,0,0)
        cpx.pixels[4] = (255,0,0)
        cpx.pixels[5] = (255,0,0)
        cpx.pixels[6] = (255,0,0)
        cpx.pixels[7] = (255,0,0)
        cpx.pixels[8] = (255,0,0)
        cpx.pixels[9] = (255,0,0)
        time.sleep(0.5)

