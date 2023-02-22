import os

# Set the path to the folder containing the images
folder_path = "./truly_defect"

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Sort the files so that they are renamed in the order they appear in the folder
files.sort()

# Create a loop to rename each file
for i, file in enumerate(files):
    # Get the file path
    file_path = os.path.join(folder_path, file)
    
    # Check if the file is an image
    if file.endswith(".jpg"):
        # Create the new file name
        new_file_name = "defect_{}.jpg".format(i + 1)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(file_path, new_file_path)
