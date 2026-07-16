import time
from data_generator import DataGenerator
from data_logger import DataLogger

def main():
    sensor = DataGenerator()
    logger = DataLogger("log.csv")
    start_time = time.time()

    while True:
        t = time.time() - start_time
        value = sensor.read()
        logger.log([t, value])
        #print(f"t={t:.2f}, value={value:.2f}")

        time.sleep(0.1)  # simulates sampling rate (10 Hz)

if __name__ == "__main__":
    main()