import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "demofile.txt")


try:
    # Open the file in append mode
    with open(file_path, 'a') as file:
        # Append some content to the file
        file.write("This is a demo file for appending.\n")

except IOError:
    print("An error occurred while trying to write to the file.")