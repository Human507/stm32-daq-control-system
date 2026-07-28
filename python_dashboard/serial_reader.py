import serial
class SerialReader:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = serial.Serial(port, baud_rate)
    def read(self):
        data = self.connection.readline().decode("utf-8")
        data = float(data)
        return data
#need to add close() function