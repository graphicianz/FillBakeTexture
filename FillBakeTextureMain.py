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

blurRaduis = 100

# Iterate over each pixel in the input image
for y in range(height):
    for x in range(width):
        # Get the RGBA color values of the pixel at (x, y)
        r, g, b, a = input_image.getpixel((x, y))

        #print(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}, A: {a}")
        #loggin.info(f"Main Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}, A: {a}")
        # Check if the alpha channel is less than 255
        if a < 255:
            # Set the pixel color to red on the output canvas
            # output_image.putpixel((x, y), (0, 0, 0, 255))

            # go left
            currentX = x
            currentPixelLFT = input_image.getpixel((x, y))
            for stepLFT in range(blurRaduis):
                if currentX<0:
                    #loggin.info(f"break, LFT currentX : {currentX}")
                    break
                else:
                    currentPixelLFT = input_image.getpixel((currentX, y))
                    #print(f"\tPixel at ({currentX}, {y}) - R: {currentPixelLFT[0]}, G: {currentPixelLFT[1]}, B: {currentPixelLFT[2]}, A: {currentPixelLFT[3]}")
                    #loggin.info(f"\tLFT Pixel at ({currentX}, {y}) - R: {currentPixelLFT[0]}, G: {currentPixelLFT[1]}, B: {currentPixelLFT[2]}, A: {currentPixelLFT[3]}")
                    if currentPixelLFT[3] < 255:
                        currentX = currentX - 1
                        continue
                    else:
                        break
            distanceLFT = 1 - (float(stepLFT) / (blurRaduis))
            #distanceLFT = 1 / max(1,float(stepLFT))
            #print(f"distanceLFT : {distanceLFT}")
            #loggin.info(f"distanceLFT : {distanceLFT}")

            # go right
            currentX = x
            currentPixelRGT = input_image.getpixel((x, y))
            for stepRGT in range(blurRaduis):
                if currentX > width-1:
                    #loggin.info(f"break, RGT currentX : {currentX}")
                    break
                else:
                    currentPixelRGT = input_image.getpixel((currentX, y))
                    #print(f"\tPixel at ({currentX}, {y}) - R: {currentPixelRGT[0]}, G: {currentPixelRGT[1]}, B: {currentPixelRGT[2]}, A: {currentPixelRGT[3]}")
                    #loggin.info(f"\tRGT Pixel at ({currentX}, {y}) - R: {currentPixelRGT[0]}, G: {currentPixelRGT[1]}, B: {currentPixelRGT[2]}, A: {currentPixelRGT[3]}")
                    if currentPixelRGT[3] < 255:
                        currentX = currentX + 1
                        continue
                    else:
                        break
            #distanceRGT = (float(stepRGT) / (blurRaduis-1))
            distanceRGT = 1 - (float(stepRGT) / (blurRaduis))
            #print(f"distanceRGT : {distanceRGT}")
            #loggin.info(f"distanceRGT : {distanceRGT}")

            # go up
            currentY = y
            currentPixelUP = input_image.getpixel((x, y))
            for stepUP in range(blurRaduis):
                if currentY<0:
                    #loggin.info(f"break, UP currentY : {currentY}")
                    break
                else:
                    currentPixelUP = input_image.getpixel((x, currentY))
                    #print(f"\tPixel at ({currentY}, {y}) - R: {currentPixelUP[0]}, G: {currentPixelUP[1]}, B: {currentPixelUP[2]}, A: {currentPixelUP[3]}")
                    #loggin.info(f"\tUP Pixel at ({x}, {currentY}) - R: {currentPixelUP[0]}, G: {currentPixelUP[1]}, B: {currentPixelUP[2]}, A: {currentPixelUP[3]}")
                    if currentPixelUP[3] < 255:
                        currentY = currentY - 1
                        continue
                    else:
                        break
            #distanceUP = (float(stepUP) / (blurRaduis-1))
            distanceUP = 1 - (float(stepUP) / (blurRaduis))
            #print(f"distanceUP : {distanceUP}")
            #loggin.info(f"distanceUP : {distanceUP}")

            # go down
            currentY = y
            currentPixelDOWN = input_image.getpixel((x, y))
            for stepDOWN in range(blurRaduis):
                if currentY > height+1:
                    #loggin.info(f"break, DOWN currentY : {currentY}")
                    break
                else:
                    currentPixelDOWN = input_image.getpixel((x, currentY))
                    #print(f"\tPixel at ({currentY}, {y}) - R: {currentPixelDOWN[0]}, G: {currentPixelDOWN[1]}, B: {currentPixelDOWN[2]}, A: {currentPixelDOWN[3]}")
                    #loggin.info(f"\tDOWN Pixel at ({x}, {currentY}) - R: {currentPixelDOWN[0]}, G: {currentPixelDOWN[1]}, B: {currentPixelDOWN[2]}, A: {currentPixelDOWN[3]}")
                    if currentPixelDOWN[3] < 255:
                        currentY = currentY + 1
                        continue
                    else:
                        break
            #distanceDOWN = (float(stepDOWN) / (blurRaduis-1))
            distanceDOWN = 1 - (float(stepDOWN) / (blurRaduis))
            #print(f"distanceDOWN : {distanceDOWN}")
            #loggin.info(f"distanceDOWN : {distanceDOWN}")  

            #output_image.putpixel((x, y), (0, 0, 0, 255))
            sumR = int(((currentPixelLFT[0]*distanceLFT) + (currentPixelRGT[0]*distanceRGT) + (currentPixelUP[0]*distanceUP) + (currentPixelDOWN[0]*distanceDOWN))/3.0)
            sumG = int(((currentPixelLFT[1]*distanceLFT) + (currentPixelRGT[1]*distanceRGT) + (currentPixelUP[1]*distanceUP) + (currentPixelDOWN[1]*distanceDOWN))/3.0)
            sumB = int(((currentPixelLFT[2]*distanceLFT) + (currentPixelRGT[2]*distanceRGT) + (currentPixelUP[2]*distanceUP) + (currentPixelDOWN[2]*distanceDOWN))/3.0)
            output_image.putpixel((x, y), (sumR, sumG, sumB, 255))
            #print(f"sum R:{sumR}, G:{sumG}, B:{sumB}")

    #print(f"coordinate : ({x},{y})")
    #if y>500:
    #    break


combined_image = Image.alpha_composite(combined_image, output_image)
combined_image = Image.alpha_composite(combined_image, input_image)

# Save the output image
combined_image.save("images/test01_output.png")