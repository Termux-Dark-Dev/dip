import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (original color image)
image = cv2.imread('example.jpg')

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not load image.")
    exit()

# 1. Smoothing (Gaussian Blur) with a larger kernel for more blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # Increased kernel size for stronger blur

# 2. Sharpening (Using a stronger sharpening kernel)
sharpening_kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])  # Original kernel
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# 3. Unsharp Masking (Sharpening by subtracting a blurred version)
blurred_for_unsharp = cv2.GaussianBlur(image, (15, 15), 0)  # Use a larger kernel for blur
unsharp_masked_image = cv2.addWeighted(image, 2.5, blurred_for_unsharp, -1.5, 0)  # Higher weight for sharpening

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), plt.title('Blurred Image')
plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)), plt.title('Sharpened Image')
plt.subplot(2, 2, 4), plt.imshow(cv2.cvtColor(unsharp_masked_image, cv2.COLOR_BGR2RGB)), plt.title('Unsharp Masking')
plt.tight_layout()
plt.savefig("enhanced_image.png")
