import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dummy.txt")

try:
    # Delete the file
    os.remove(file_path)
    print(f"The file at {file_path} has been deleted.") 
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")