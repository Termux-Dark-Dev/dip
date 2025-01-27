from PIL import Image

# Load the image
image = Image.open("example.jpg")

# Downsampling: Reduce image size to 25% (1/4 of original width and height)
downsampled = image.resize(
    (image.width // 4, image.height // 4),
    Image.Resampling.LANCZOS,  # High-quality downsampling
)

# Upsampling: Increase the downsampled image size back to original dimensions
upsampled = downsampled.resize(
    (image.width *2, image.height*2),
    Image.Resampling.NEAREST,  # Nearest neighbor for a pixelated effect
)

# Save the results (optional, for review)
# image.save("original_image.jpg")
# downsampled.save("downsampled_image.jpg")
# upsampled.save("upsampled_image.jpg")

# Display the images
image.show(title="Original Image")
downsampled.show(title="Downsampled Image (25%)")
upsampled.show(title="Upsampled Image (400%)")


# see in this code save the image and then look at the properties of the image in windows you will notice that downsampled image is of low res and upsampled image is of high res similar to org image