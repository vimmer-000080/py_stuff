import os
import numpy as np
from skimage import io
from skimage.morphology import closing, disk
import matplotlib.pyplot as plt

# Define directories for input (processed images) and output (eyelash-free images)
processed_directory = '/home/idiot/output_imgs'       # Directory with saved edge-detected images
eyelash_free_directory = '/home/idiot/output_eyelashed_cleared' # Directory to save eyelash-free images
os.makedirs(eyelash_free_directory, exist_ok=True)

# Structuring element for morphological closing
structuring_element = disk(1)  # You may adjust the radius based on eyelash thickness

# Loop through the processed images
for file in os.listdir(processed_directory):
    if file.endswith('.bmp'):
        # Load the edge-detected image
        img_path = os.path.join(processed_directory, file)
        edge_image = io.imread(img_path, as_gray=True)
        
        # Apply morphological closing to remove eyelashes
        eyelash_free_image = closing(edge_image, structuring_element)
        
        # Save the eyelash-free image
        save_path = os.path.join(eyelash_free_directory, f'eyelash_free_{file}')
        plt.imsave(save_path, eyelash_free_image, cmap='gray')
        
        # Optional: Print progress
        print(f"Processed and saved eyelash-free image: {save_path}")

print("Eyelash removal completed for all images.")

