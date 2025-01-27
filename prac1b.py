import numpy as np
from scipy.signal import chirp, spectrogram
from PIL import Image
import io

# Generate a chirp signal
sampling_rate = 1000
t = np.linspace(0, 1, sampling_rate, endpoint=False)
signal = chirp(t, f0=10, f1=200, t1=1, method='linear')  # Linear frequency sweep

# Compute Spectrogram
f, t_spec, Sxx = spectrogram(signal, fs=sampling_rate)

# Use PIL to display the spectrogram
def plot_spectrogram(data, filename):
    # Convert spectrogram data to an image
    img = Image.fromarray(np.uint8(255 * data / np.max(data)))  # Normalize and convert to 8-bit
    img = img.resize((800, 400))  # Resize for better visibility
    img.save(filename)
    img.show()

# Plot and save the spectrogram
plot_spectrogram(Sxx, "spectrogram.png")
