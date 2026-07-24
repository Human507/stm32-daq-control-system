# STM32 DAQ + Control System

A real-time data acquisition and control system pairing STM32 firmware with a Python dashboard. Built to learn embedded systems, closed-loop control, and live data visualization from the ground up.

<!-- Demo: drop a screen recording (gif) of the live plot updating here once available -->
<!-- ![Live plot demo](docs/demo.gif) -->

## What It Does

The end goal: an STM32 microcontroller samples sensor data over ADC, drives a motor with PWM, and reads position/speed feedback from an encoder, running a PID control loop on-chip. Sensor and control data streams to a Python dashboard over UART for logging and live visualization.

```
STM32 (ADC, Encoder) -> UART -> Python (Log + Live Plot)
                ^
              PWM <- PID Loop (on-chip)
```

Design notes:
- Each piece has one job. Data generation, logging, and visualization are separate and don't depend on each other's internals.
- The Python dashboard and the acquisition loop run as separate processes that only talk to each other through a shared log file. This keeps things simple and avoids needing multithreading while the core system is still being built.
- Built in stages: got the full pipeline working with simulated data first, then moving to real hardware.

## Current Status

Done, Python software pipeline (simulated data):
- Data pipeline: DataGenerator to DataLogger to CSV, with automatic headers, write-flushing, and graceful shutdown on Ctrl+C
- CSV reading utilities for full-history and tail reads
- Static plotting of logged data with matplotlib
- Live, real-time plotting using matplotlib's FuncAnimation, reading the log file while a separate process is still writing to it

Still working on, hardware integration:
- STM32 firmware for ADC sampling and UART transmission
- SerialReader, a drop-in replacement for DataGenerator that reads live sensor data over serial (the architecture already supports this swap without touching the logging or plotting code)
- PWM motor drive and encoder feedback
- PID control loop running on-chip

## Tech Stack
Firmware: C, STM32 HAL
Software: Python, matplotlib, PySerial

## Setup

```
pip install matplotlib pyserial
```

## Running

The acquisition loop and the live dashboard run as separate processes. Start them in two terminals:

```
# Terminal 1, generates and logs data
python python_dashboard/main.py

# Terminal 2, reads log.csv and plots it live
python python_dashboard/live_plot.py
```

For a one-time plot of a finished run instead of a live one:
```
python python_dashboard/plot_data.py
```

## Why This Architecture

The Python side is split into small, single-purpose scripts (main.py for acquisition, live_plot.py for visualization) that only communicate through a file, not directly with each other. That keeps the core real-time loop simple and avoids needing threading while the system is still coming together. It's the same basic idea behind tools like Docker Compose or CI pipeline stages: independent processes coordinated through a shared resource instead of being tightly coupled.

## Repo Structure
```
python_dashboard/
  data_generator.py    # Simulated (soon real) sensor data source
  data_logger.py        # CSV logging with header and flush handling
  csv_reader.py          # Read utilities (tail and full history)
  main.py                 # Acquisition loop
  plot_data.py            # Static post-run plot
  live_plot.py             # Real-time plot (FuncAnimation)
```
