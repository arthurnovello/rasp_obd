import RPi.GPIO as GPIO
from time import sleep

def buz(cond):
    GPIO.setmode(GPIO.BCM)
    buzzer = 23
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.output(buzzer, GPIO.LOW)
    if cond == "ON":
        GPIO.output(buzzer, GPIO.HIGH)
        print("Beep")
    elif cond == "OFF":
        GPIO.output(buzzer, GPIO.LOW)
        print("No Beep")
        GPIO.cleanup()
