import csv
class DataLogger:
    def __init__(self, filename, header):
        self.filename = filename
        self.file = open(filename, 'w', newline='')
        self.writer = csv.writer(self.file)
        self.header_written = False
        self.header = header
    def log(self, content):
        if self.header_written == False:
            self.writer.writerow(self.header)
            self.header_written = True
        self.writer.writerow(content)
        self.file.flush()
    def close(self):
        self.file.close()

"""
Logger Testing:
logger = DataLogger("test.csv")

logger.log(["time", "value"])
logger.log([0.1, 25.3])
logger.log([0.2, 25.5])

logger.close()"""