import os
import shutil

# Define your current directories for images and ground truth
images_dir = 'C:/Users/HP/Downloads/archive/ShanghaiTech/part_A/Test/images'
ground_truth_dir = 'C:/Users/HP/Downloads/archive/ShanghaiTech/part_A/Test/ground-truth'

# Define the new folder where the combined files will be saved
new_train_dir = 'C:/Users/HP/Downloads/archive/ShanghaiTech/part_A/Test/Test_Data'

# Create the new directory if it doesn't exist
if not os.path.exists(new_train_dir):
    os.makedirs(new_train_dir)

# Iterate over the images in the images folder
for image_file in os.listdir(images_dir):
    if image_file.endswith('.jpg'):
        # Get the image name without the extension
        image_name = os.path.splitext(image_file)[0]

        # Define the ground truth file path based on the image name
        ground_truth_file = f'GT_{image_name}.mat'

        # Define new names for image and ground truth
        new_image_name = f'{image_name}.jpg'
        new_gt_name = f'{image_name}_ann.mat'

        # Full paths of the current image and ground truth
        image_path = os.path.join(images_dir, image_file)
        ground_truth_path = os.path.join(ground_truth_dir, ground_truth_file)

        # Full paths of where to save the renamed files
        new_image_path = os.path.join(new_train_dir, new_image_name)
        new_gt_path = os.path.join(new_train_dir, new_gt_name)

        # Copy the image file to the new directory with the new name
        shutil.copy(image_path, new_image_path)

        # Check if the corresponding ground truth file exists
        if os.path.exists(ground_truth_path):
            # Copy the ground truth file to the new directory with the new name
            shutil.copy(ground_truth_path, new_gt_path)
        else:
            print(f"Ground truth file not found for {image_name}")

print(f"All files moved and renamed successfully to {new_train_dir}")
