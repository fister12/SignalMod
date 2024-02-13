import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np

# Define your signal function
def your_signal1(t):
    # Generate a sine wave
    frequency = 1  # Hz
    amplitude = 1
    return amplitude * np.sin(2 * np.pi * frequency * t)

def your_signal2(t):
    # Generate another sine wave
    frequency = 2  # Hz
    amplitude = 0.5
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Initialize plot
app = QApplication(sys.argv)

win = pg.GraphicsLayoutWidget()  # Use GraphicsLayoutWidget instead of GraphicsWindow
p = win.addPlot()

# Initialize data arrays
t = []
y1 = []
y2 = []

def update():
    global t, y1, y2
    current_time = len(t) * 0.01  # Simulate real-time data, assuming a 100 Hz update rate
    new_data1 = your_signal1(current_time)  # Get real-time data for signal 1
    new_data2 = your_signal2(current_time)  # Get real-time data for signal 2
    t.append(current_time)
    y1.append(new_data1)
    y2.append(new_data2)
    p.plot(t, y1, pen='r', clear=True)  # Update plot with new data for signal 1 and clear previous plot
    p.plot(t, y2, pen='b')  # Plot signal 2 on the same plot
    p.setTitle("Signal 1 and Signal 2")  # Set plot title
    p.setLabel('left', 'Amplitude')  # Set y-axis label
    p.setLabel('bottom', 'Time')  # Set x-axis label

timer = pg.QtCore.QTimer()
timer.setInterval(10)  # Set update interval (adjust as needed)
timer.timeout.connect(update)
timer.start()

win.show()
sys.exit(app.exec_())
