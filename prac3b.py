import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the main image and template image
image = cv2.imread('main_image.jpg', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('template_image.jpg', cv2.IMREAD_GRAYSCALE)

# Perform template matching using cv2.matchTemplate
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Find the location of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Get the dimensions of the template
w, h = template.shape[::-1]

# Draw a rectangle around the matched region
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right, 255, 2)

# Save the result with the rectangle
cv2.imwrite('template_matching_result.png', image)

# Plot the result
plt.figure(figsize=(10, 5))
plt.imshow(image, cmap='gray')
plt.title('Template Matching Result')
plt.axis('off')
plt.savefig("template_matching_result.png")
print("Template matching result saved as template_matching_result.png")
