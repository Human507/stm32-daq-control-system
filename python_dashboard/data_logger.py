import csv
class DataLogger:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        self.writer = csv.writer(self.file)
        self.header_written = False