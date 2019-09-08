import obd


def connect():
    connection = obd.OBD()
    return connection.status()


connect()
