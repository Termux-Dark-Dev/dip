import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (grayscale for easier derivative calculation)
image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not load image. Please check the file path.")
    exit()

# --- Gradient Operation (Sobel) ---
# Sobel operator for x and y gradients (edge detection)
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel in x direction
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel in y direction

# Compute the magnitude of the gradient (edge strength)
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# --- Laplacian Operation ---
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# --- Plotting Results ---
plt.figure(figsize=(12, 8))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Gradient X (Sobel)
plt.subplot(2, 3, 2)
plt.imshow(gradient_x, cmap='gray')
plt.title('Gradient X (Sobel)')
plt.axis('off')

# Gradient Y (Sobel)
plt.subplot(2, 3, 3)
plt.imshow(gradient_y, cmap='gray')
plt.title('Gradient Y (Sobel)')
plt.axis('off')

# Gradient Magnitude
plt.subplot(2, 3, 4)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude')
plt.axis('off')

# Laplacian
plt.subplot(2, 3, 5)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.axis('off')

# Save the plot
plt.savefig("image_derivatives_enhancements.png")
print("Enhancement result saved as 'image_derivatives_enhancements.png'")
