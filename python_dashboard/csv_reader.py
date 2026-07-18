import csv

def read_last_rows(filename, n):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    header = rows[0]
    data = rows[1:]
    return data[-n:]
print(read_last_rows('log.csv',5))