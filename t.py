import os
import shutil

# Define the main folders and the target folders
main_folders = ['Railway_Station', 'LiveEvent', 'Experiments', 'Event_Entrances']
target_folders = ['train', 'val', 'test']

# Function to copy files from source to destination
def copy_files(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                os.makedirs(d)
            copy_files(s, d)
        else:
            shutil.copy2(s, d)

# Create new structure and copy files
for target in target_folders:
    if not os.path.exists(target):
        os.makedirs(target)
        os.makedirs(os.path.join(target, 'images'))
        os.makedirs(os.path.join(target, 'labels'))

    for folder in main_folders:
        img_src = os.path.join(folder, target, 'images')
        lbl_src = os.path.join(folder, target, 'labels')
        
        img_dst = os.path.join(target, 'images')
        lbl_dst = os.path.join(target, 'labels')

        copy_files(img_src, img_dst)
        copy_files(lbl_src, lbl_dst)

print("Files copied successfully.")