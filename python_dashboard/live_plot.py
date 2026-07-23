from matplotlib import pyplot as plt
from csv_reader import read_all_rows
from matplotlib.animation import FuncAnimation
def update(frame):
    data = read_all_rows('log.csv')
    time = []
    value = []
    for line in data:
        time.append(float(line[0]))
        value.append(float(line[1]))
    plt.cla()
    plt.plot(time, value)
fig = plt.figure()
ani = FuncAnimation(fig, update, interval=50)  # calls update() every 500ms
plt.show()

    
