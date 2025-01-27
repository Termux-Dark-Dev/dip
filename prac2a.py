import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Define parameters
frequency = 1  # Frequency in Hz
periods = 3    # Number of periods to plot
samples_per_period = 500  # Resolution of the signal ---- Number of data points per period to ensure smoothness of the plot.
t = np.linspace(0, periods, periods * samples_per_period)

# Generate triangular wave using sawtooth function (width=0.5 for symmetry)
triangle_wave = sawtooth(2 * np.pi * frequency * t, width=0.5)

# Plot the triangle wave
plt.plot(t, triangle_wave, label="Triangle Wave")
plt.title("Triangular Waveform - 3 Periods")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.savefig("plot.png")
print("Plot saved as plot.png")
