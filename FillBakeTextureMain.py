from PIL import Image
import sys
import logging

# Configure logging to write to a file
logging.basicConfig(filename='log/logfile.log', level=logging.DEBUG)

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

blurRaduis = 30

# Iterate over each pixel in the input image
for y in range(height):
    for x in range(width):
        # Get the RGBA color values of the pixel at (x, y)
        r, g, b, a = input_image.getpixel((x, y))

        print(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}, A: {a}")
        logging.info(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}, A: {a}")
        # Check if the alpha channel is less than 255
        if a < 255:
            # Set the pixel color to red on the output canvas
            # output_image.putpixel((x, y), (0, 0, 0, 255))

            # go left
            currentX = x
            currentPixelLFT = input_image.getpixel((x, y))
            for stepLFT in range(blurRaduis):
                if currentX-stepLFT<0:
                    break
                else:
                    currentPixelLFT = input_image.getpixel((currentX, y))
                    print(f"\tPixel at ({currentX}, {y}) - R: {currentPixelLFT[0]}, G: {currentPixelLFT[1]}, B: {currentPixelLFT[2]}, A: {currentPixelLFT[3]}")
                    logging.info(f"\tPixel at ({currentX}, {y}) - R: {currentPixelLFT[0]}, G: {currentPixelLFT[1]}, B: {currentPixelLFT[2]}, A: {currentPixelLFT[3]}")
                    if currentPixelLFT[3] < 255:
                        currentX = currentX - 1
                        continue
                    else:
                        break
            #weightRatioLFT = (float(stepLFT) / (blurRaduis-1))
            weightRatioLFT = 1 / float(stepLFT)
            print(f"weightRatioLFT : {weightRatioLFT}")
            logging.info(f"weightRatioLFT : {weightRatioLFT}")
            # go right
            # go up
            # go down
    sys.exit()


combined_image = Image.alpha_composite(combined_image, output_image)
combined_image = Image.alpha_composite(combined_image, input_image)

# Save the output image
combined_image.save("images/test01_output.png")