import sys
from datetime import datetime

def append_datetime(filename):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(filename, 'a') as file:
            file.write(f"{current_time}\n")
        print(f"Date and time appended to {filename}")
    except IOError as e:
        print(f"Error: Unable to append to the file. {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python append_datetime.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    append_datetime(filename)
