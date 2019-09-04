import obd
from obd import OBDStatus

connection = obd.OBD()

if connection.status() == OBDStatus.OBD_CONNECTED:
    print("Conectado")
