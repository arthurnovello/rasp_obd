import obd
from time import sleep

connection = obd.OBD(check_voltage=False)
connection.status()


def vel():
    return connection.query(obd.commands.SPEED)


def rpm():
    return connection.query(obd.commands.RPM)


def temp():
    return connection.query(obd.commands.COOLANT_TEMP)


velocidade = vel()
rotacao = rpm()
temperatura = temp()

while True:
    sleep(1)
    if velocidade != vel():
        velocidade = vel()

    if rotacao != rpm():
        rotacao = rpm()

    if temperatura != temp():
        temperatura = temp()

    print(velocidade)
    print(rotacao)
    print(temperatura)
