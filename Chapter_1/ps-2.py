import os

# Specify the directory you want to list
directory_path = '/'  # Current directory; change to any path you want

try:
    # Get list of files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory_path}'.")
