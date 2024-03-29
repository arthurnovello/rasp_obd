import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from sensores import temp, dist
from buzz import buz


GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 4

print("In progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("waiting to settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.0001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    pulse_start = time.time()

while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print(distance)

GPIO.cleanup()


print(dist(4, 17))
buz("ON")
time.sleep(0.5)
buz("OFF")
print(temp("HUMID"))
print(temp("TEMP"))
