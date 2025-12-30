import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "demofile.txt")


try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        print("*** File Readlines ***")
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except IOError:
    print("An error occurred while trying to read the file.")