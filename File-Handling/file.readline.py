import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "demofile.txt")

try:
    with open(file_path, 'r') as file:
        # Read the first line from the file
        while True:
            line = file.readline()
            if not line:
                break               # Stop if line is empty (EOF reached)
            print(line.strip())     # strip() removes the newline character

except IOError:
    print("An error occurred while trying to read the file.")