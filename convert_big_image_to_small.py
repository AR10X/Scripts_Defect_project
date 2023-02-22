import os
import cv2

# Load the original image
img = cv2.imread("./test_sample)", cv2.IMREAD_GRAYSCALE)

# Resizing the image
img = cv2.resize(img, (300, 300), interpolation = cv2.INTER_AREA)

# Get the image height and width
height, width = img.shape

# Calculate the number of rows and columns to break the image into
# rows = height // 300
# cols = width // 300

# Create a new folder to save the sub-images
folder_name = 'test_1'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

print("Processing...\n")

rows = 1
cols = 1

# Create a loop to break down the image into smaller images
for i in range(rows):
    for j in range(cols):
        # Get the current 300x300 sub-image
        sub_img = img[i * 300 : (i + 1) * 300, j * 300 : (j + 1) * 300]
        
        # Save the sub-image to a file in the new folder
        file_name = "sub_img_{}_{}.jpg".format(i, j)
        file_path = os.path.join(folder_name, file_name)
        cv2.imwrite(file_path, sub_img)


print("Completed!\n")
print("No of images created: " + str(rows*cols))