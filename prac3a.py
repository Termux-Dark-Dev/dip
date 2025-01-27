import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image in grayscale
image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)  # The flag cv2.IMREAD_GRAYSCALE ensures the image is loaded in grayscale (black and white).

# Define a simple edge detection kernel (Sobel filter for horizontal edges)
kernel = np.array([[-1, -1, -1],
                   [ 0,  0,  0],
                   [ 1,  1,  1]])

# Perform convolution using cv2.filter2D
convolved_image = cv2.filter2D(image, -1, kernel)

# Save and visualize results
cv2.imwrite('original_image.png', image)
cv2.imwrite('convolved_image.png', convolved_image)

# Plot the original and convolved images side by side
plt.figure(figsize=(10, 5))  # Creates a figure with dimensions 10x5 inches.

plt.subplot(1, 2, 1) # Divides the figure into 1 row and 2 columns; selects the first subplot.
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(convolved_image, cmap='gray')
plt.title('Convolved Image')
plt.axis('off')

plt.savefig("comparison.png")
print("Original and convolved images saved as original_image.png, convolved_image.png, and comparison.png")
