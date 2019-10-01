import Adafruit_DHT
import board
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


def dist(pinE, pinT):
    GPIO.setmode(GPIO.BCM)

    TRIG = pinT
    ECHO = pinE

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

    GPIO.cleanup()

    return distance


def temp(valor):
    dhtDevice = Adafruit_DHT.DHT11(board.D18)
    if valor == "TEMP":
        return dhtDevice.temperature
    elif valor == "HUMID":
        return dhtDevice.humidity
