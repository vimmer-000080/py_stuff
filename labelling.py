import cv2
import numpy as np

# Initialize global variables to store the points for drawing and the circle data
drawing = False
ix, iy = -1, -1
circles = []  # Stack to store drawn circles for undo functionality

# Mouse callback function to draw the circle
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, image, temp_image, circles

    if event == cv2.EVENT_LBUTTONDOWN:  # On mouse click, start drawing
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # While moving the mouse, update the circle size
        if drawing == True:
            temp_image = image.copy()
            cv2.circle(temp_image, (ix, iy), int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2)), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:  # On mouse release, stop drawing
        drawing = False
        radius = int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2))
        cv2.circle(image, (ix, iy), radius, (0, 255, 0), 2)

        # Save the circle center and radius
        circles.append(((ix, iy), radius))
        print(f"Marked a circle at center: ({ix}, {iy}), radius: {radius}")

# Function to undo the last drawn circle
def undo_last_circle():
    global image, circles
    if circles:
        # Remove the last circle from the image
        circles.pop()  # Pop the last circle from the list
        image = cv2.imread(image_path)  # Reload the original image
        # Redraw all circles except the last one
        for center, radius in circles:
            cv2.circle(image, center, radius, (0, 255, 0), 2)
        print("Last circle undone.")

# Load the image
image_path = 'eye.jpg'  # Change this to your image path
image = cv2.imread(image_path)
temp_image = image.copy()

# Create a window and bind the mouse callback function
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while True:
    cv2.imshow('Image', temp_image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Press 'q' to exit
        break
    elif key == ord('u'):  # Press 'u' to undo the last circle
        undo_last_circle()

# After quitting, save the data for the circles
print("Circle data (center, radius):")
for center, radius in circles:
    print(f"Center: {center}, Radius: {radius}")

# Save the data to a file
with open("circles_data.txt", "w") as f:
    for center, radius in circles:
        f.write(f"Center: {center}, Radius: {radius}\n")
print("Circle data saved to 'circles_data.txt'")

cv2.destroyAllWindows()

