#Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

Max = 310

def main():

    while True:
        light = cp.light
        print((light,))
        time.sleep(.05)
        index = scale(light)
        off()
        cp.pixels[index] = (0, 50, 0)
        time.sleep(.25)

def scale(light):
    maxIndex = 9
    index = int( light/Max * maxIndex)
    return index
def off():
    for light in range(10):
        cp.pixels[light] = (0, 0, 0)
        time.sleep(.05)
main()
