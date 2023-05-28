from PIL import Image

# Open the image file
input_image = Image.open("images/test01.png")

# Convert the image to RGBA mode (if it's not already)
input_image = input_image.convert("RGBA")

# Get the width and height of the image
width, height = input_image.size

# Create an empty canvas with the same resolution
output_image = Image.new("RGBA", (width, height))

# Create a new empty canvas
combined_image = Image.new("RGBA", (width, height))

# Iterate over each pixel in the input image
for y in range(height):
    for x in range(width):
        # Get the RGBA color values of the pixel at (x, y)
        r, g, b, a = input_image.getpixel((x, y))

        # Check if the alpha channel is less than 255
        if a < 255:
            # Set the pixel color to red on the output canvas
            output_image.putpixel((x, y), (0, 0, 0, 255))


combined_image = Image.alpha_composite(combined_image, output_image)
combined_image = Image.alpha_composite(combined_image, input_image)

# Save the output image
combined_image.save("images/test01_output.png")