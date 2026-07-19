from matplotlib import pyplot as plt
from csv_reader import read_all_rows
data = read_all_rows('log.csv')
time = []
value = []
for line in data:
    time.append(float(line[0]))
    value.append(float(line[1]))
plt.plot(time, value)
plt.show()
