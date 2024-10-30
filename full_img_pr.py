import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io, img_as_float
from scipy.ndimage import convolve

# Define the input directory and output directory
input_directory = '/home/idiot/Downloads'      # Replace with your image directory path
output_directory = '/home/idiot/output_imgs'  # Replace with directory to save output images

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define Sobel filters for x and y gradients
Gx = np.array([[-1, 1]])
Gy = Gx.T
sx, sy = 0.1, 0.1  # Gaussian membership function parameters

# Walk through all subdirectories and find .bmp files
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.endswith('.bmp'):
            # Load the image and convert to grayscale
            img_path = os.path.join(root, file)
            Irgb = io.imread(img_path)
            Igray = color.rgb2gray(Irgb)
            I = img_as_float(Igray)

            # Calculate image gradients
            Ix = convolve(I, Gx, mode='reflect')
            Iy = convolve(I, Gy, mode='reflect')

            # Define Gaussian membership functions for Ix and Iy (zero region)
            Ix_zero = np.exp(-((Ix / sx) ** 2) / 2)
            Iy_zero = np.exp(-((Iy / sy) ** 2) / 2)

            # Apply fuzzy logic rules for edge detection
            Iout_white = Ix_zero * Iy_zero    # Both Ix and Iy near zero -> white (edge)
            Ieval = Iout_white                # Output is white where edges are detected

            # Save the processed image
            save_path = os.path.join(output_directory, f'edge_{file}')
            plt.imsave(save_path, Ieval, cmap='gray')

            # Optional: Print progress
            print(f"Processed and saved: {save_path}")

print("Edge detection completed for all images.")
