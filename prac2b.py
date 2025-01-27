import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Create two sample signals (sine waves with a phase shift)
t = np.linspace(0, 10, 1000)
signal1 = np.sin(2 * np.pi * t)           # First sine wave
signal2 = np.sin(2 * np.pi * t + np.pi/4)  # Second sine wave with phase shift

# Compute correlation between the two signals
correlation = correlate(signal1, signal2, mode='full')

# Plot the first and second signals
plt.figure(figsize=(10, 4))
plt.plot(t, signal1, label="Signal 1")
plt.plot(t, signal2, label="Signal 2", linestyle='dashed')
plt.title("Two Signals")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.savefig("signals.png")
print("Signals plot saved as signals.png")

# Plot the correlation result
plt.figure(figsize=(8, 3))
lags = np.arange(-len(signal1) + 1, len(signal1))  # Lag values for x-axis
plt.plot(lags, correlation, label="Correlation")
plt.title("Correlation between Signal 1 and Signal 2")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.legend()
plt.savefig("correlation.png")
print("Correlation plot saved as correlation.png")
