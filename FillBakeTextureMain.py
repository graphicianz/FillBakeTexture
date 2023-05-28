from PIL import Image

# Open the image file
image = Image.open("images/test01.png")

# Convert the image to RGB mode (if it's not already)
image = image.convert("RGB")

# Get the width and height of the image
width, height = image.size

# Iterate over each pixel in the image
for y in range(height):
    for x in range(width):
        # Get the RGB color values of the pixel at (x, y)
        r, g, b = image.getpixel((x, y))

        # Do something with the color values
        # For example, print them
        print(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}")
    break
