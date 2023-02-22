import os
import cv2

# Define the folder containing the images
folder_path = './sample_images'

print("Process started..")
img_no = 0
sub_img_no = 10000
# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    
    img_no += 1
    print("Filename: {} , image No: {}".format(filename, img_no))
    # Skip files that are not images
    if not filename.endswith('.jpg'):
        continue
    
    # Load the image
    img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
    
    # Resize the image
    img = cv2.resize(img, (4000, 3012), interpolation = cv2.INTER_AREA)

    # Get the image height and width
    height, width = img.shape

    # Calculate the number of rows and columns to break the image into
    rows = height // 300
    cols = width // 300

    # Create a new folder to save the sub-images
    folder_name = 'defect_images_org_4000'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a loop to break down the image into smaller images
    for i in range(rows):
        for j in range(cols):
            sub_img_no += 1
            print("Creating image: {}".format(sub_img_no))
            # Get the current 300x300 sub-image
            sub_img = img[i * 300 : (i + 1) * 300, j * 300 : (j + 1) * 300]

            # Save the sub-image to a file in the new folder
            file_name = "notknown_{}.jpg".format(sub_img_no)
            file_path = os.path.join(folder_name, file_name)
            cv2.imwrite(file_path, sub_img)
print("Process Completed!")