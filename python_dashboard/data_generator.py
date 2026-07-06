import numpy as np
import time

class DataGenerator:
    def __init__(self):
        self.t = 0

    def read(self):
        # simulate a sensor (RPM-like signal)
        value = 100 + 20 * np.sin(self.t) + np.random.normal(0, 1)
        self.t += 0.1
        return value


if __name__ == "__main__":
    gen = DataGenerator()
    for _ in range(10):
        print(gen.read())