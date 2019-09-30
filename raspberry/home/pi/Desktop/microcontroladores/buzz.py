from gpiozero import Buzzer

buzzer = Buzzer(15)


def buz(cond):
    if cond == "ON":
        buzzer.on()
    elif cond == "OFF":
        buzzer.off()
