import sys
import os
from datetime import datetime

def append_datetime_to_filename(filename):
    base, ext = os.path.splitext(filename)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = f"{base}_{current_time}{ext}"
    return new_filename

def append_datetime(filename):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_filename = append_datetime_to_filename(filename)
    
    try:
        # Rename the file
        os.rename(filename, new_filename)
        
        # Append the datetime to the file contents
        with open(new_filename, 'a') as file:
            file.write(f"{current_time}\n")
        
        print(f"File renamed to: {new_filename}")
        print(f"Date and time appended to {new_filename}")
    except IOError as e:
        print(f"Error: Unable to rename or append to the file. {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python append_datetime.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    append_datetime(filename)
