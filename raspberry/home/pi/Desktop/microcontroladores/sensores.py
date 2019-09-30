import sys
import Adafruit_DHT
import board
from gpiozero import DistanceSensor


def dist(pinE, pinT):
    sensor = DistanceSensor(echo=pinE, trigger=pinT)
    return sensor.distance * 100


def temp(valor):
    dhtDevice = Adafruit_DHT.DHT11(board.D18)
    if valor == "TEMP":
        return dhtDevice.temperature
    elif valor == "HUMID":
        return dhtDevice.humidity
