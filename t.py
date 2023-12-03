# import os
# import fileinput
# import re

# # Define a function to replace lines starting with a number (other than 0) with 0.
# def replace_lines(filename):
#     with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
#         for line in file:
#             splitted_line =  line.split(" ")
#             if splitted_line[0]=="0":
#                 pass
#             else:
#                 splitted_line[0]="0"
#                 line = " ".join(splitted_line)
#             print(line, end='')

# # Walk through all directories and subdirectories in the current directory.
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.txt'):
#             filepath = os.path.join(root, file)
#             replace_lines(filepath)

# print("Lines starting with numbers (other than 0) have been changed to start with 0.")

import os

# Define a function to delete .bak files in a directory.
def delete_bak_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.bak'):
                filepath = os.path.join(root, file)
                os.remove(filepath)
                print(f"Deleted {filepath}")

# Specify the directory where you want to delete .bak files.
directory_to_search = '.'  # Change this to the directory of your choice.

# Call the function to delete .bak files in the specified directory.
delete_bak_files(directory_to_search)