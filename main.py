import sys

try:
    filename = sys.argv[1]
except IndexError:
    print("It looks like you didn't specify a file! You can drag a file from the file browser in most operating systems to the console window. Make sure there's a space between the script (main.py) and the checklist you want to open.")
    sys.exit(1)
try:
    lines = open(filename).read().splitlines()
    print("Welcome to sneklist!\n")
    print(f"Opened: {filename}\n")
    print("Press any key to clear the current item and move to the next.\n---\n\n")
    for l in lines:
        print(l)
        input()
        print(f"✓ Finished: {l}\n")
    print(f"\nEnd of the checklist! Finished with {len(lines)} items.")
except FileNotFoundError:
    print(f"Sneklist could not find file: {filename}")
    sys.exit(1)
