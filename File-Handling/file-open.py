import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "demo-read.txt")

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except IOError:
    print("An error occurred while trying to read the file.")