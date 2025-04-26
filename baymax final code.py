from machine import Pin
import neopixel
import time

LED_PIN = 27
NUM_LEDS = 16
RELAY_PIN = 18
np = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)
relay = Pin(RELAY_PIN, Pin.OUT)
relay.value(1)
for i in range(NUM_LEDS):
    for j in range(NUM_LEDS):
        np[j] = (0, 0, 0)
    np[i] = (30, 10, 20)
    np.write()
    time.sleep(0.1)
for i in range(NUM_LEDS):
    np[i] = (20, 10, 200)
np.write()
time.sleep(2)
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)
np.write()
relay.value(0)
time.sleep(30)
relay.value(1)
