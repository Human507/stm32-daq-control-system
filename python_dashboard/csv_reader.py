import csv

def read_last_rows(filename, n):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    header = rows[0]
    data = rows[1:]
    return data[-n:]
def read_all_rows(filename):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    header = rows[0]
    data = rows[1:]
    return data