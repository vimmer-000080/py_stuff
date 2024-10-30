import numpy as np
import cv2
import skfuzzy as fuzz

# Load and convert the image to grayscale
image = cv2.imread("eye.jpg", cv2.IMREAD_GRAYSCALE)

# Define membership functions based on grayscale intensity for fuzzy logic
def fuzzy_membership(gray_value):
    if gray_value < 80:
        return "Black"
    elif 80 <= gray_value < 160:
        return "Edge"
    else:
        return "White"

# Define fuzzy inference rules based on 3x3 neighborhood
def apply_fuzzy_rules(window):
    # Define rules based on neighborhood conditions
    # Check patterns for "Edge" classification
    rules = [
        (window[0, 0] == "White" and window[0, 1] == "White" and window[0, 2] == "White" and
         window[1, 0] == "White" and window[1, 1] == "Edge" and window[1, 2] == "White" and
         window[2, 0] == "Black" and window[2, 1] == "Black" and window[2, 2] == "Black"),
        # Other rules (e.g., diagonal, cross, etc.) can be added here
    ]
    return any(rules)

# Convert the grayscale image into fuzzy membership classes
def fuzzify_image(image):
    fuzzified_image = np.vectorize(fuzzy_membership)(image)
    return fuzzified_image

# Apply fuzzy rules to each pixel's 3x3 neighborhood
def fuzzy_edge_detection(image):
    fuzzified_image = fuzzify_image(image)
    output_image = np.zeros_like(image)

    # Loop over each pixel, excluding the borders
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # Extract 3x3 window around the current pixel
            window = fuzzified_image[i - 1:i + 2, j - 1:j + 2]
            if apply_fuzzy_rules(window):
                output_image[i, j] = 255  # Mark as edge
            else:
                output_image[i, j] = 0  # Non-edge pixel
    
    return output_image

# Perform fuzzy edge detection
edges = fuzzy_edge_detection(image)

# Display the result
cv2.imshow("Fuzzy Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

