# Imports, if you use libraries that aren't default, you will need to tell the user.
import subprocess  # subprocess is for opening applications.
import random
import os

curput = ""

def help_script():
     # Get the path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the source.py file
    source_path = os.path.join(script_dir, "help.txt")

    # Check if the source file exists
    if not os.path.exists(source_path):
        print("Error: help.txt not found.")

    with open(source_path, "r") as file:
        contents = file.read()
        print(contents)

def launch_script():
    # Get the path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if curput == "op":
        os.startfile(os.path.join(script_dir, "titles", curput, "Launcher.exe"))
    elif curput == "ff":
        os.startfile(os.path.join(script_dir, "titles", curput, "Launcher.exe"))

while True:
    user_input = input("Enter command: ")
    if user_input.lower() in ["help", "?"]:
        help_script()
    elif user_input.lower().startswith("launch ") or user_input.lower().startswith("l "):
        curputplace = user_input.split(" ")
        curput = curputplace[1]
        launch_script()
    else:
        print('Please input a valid command')