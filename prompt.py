import sys
import os
import glob
import subprocess

curput = ""

def help_script():
    try:
        with open("help.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"help.txt not found.")

def panick_script():
    sys.exit()

def cmd_script():
    subprocess.Popen(["start", r"C:\Windows\system32\cmd"], shell=True)

def shell_script():
    subprocess.Popen(["start", r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell"], shell=True)

def reg_script():
    subprocess.Popen(["start", r"C:\Windows\regedit"], shell=True)

def note_script():
    subprocess.Popen(["start", r"C:\Windows\notepad"], shell=True)

def plugin_list_script():
    # Define the path to the "plugins" folder
    plugins_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugins")

    # Get a list of all directories in the "plugins" folder
    directories = [f for f in os.listdir(plugins_path) if os.path.isdir(os.path.join(plugins_path, f))]

    for directory in directories:
        manifest_path = os.path.join(plugins_path, directory, "manifest.txt")

        # Find the path to the manifest.txt file
        if not os.path.isfile(manifest_path):
            print(f"Error: manifest.txt not found in {directory}")
            continue
        
        nameplugin = directory

        # Read the value of "description" from the manifest.txt file
        with open(manifest_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line.startswith("description="):
                    continue
                descriptionplugin = line[len("description="):].split("#")[0]
                if descriptionplugin is not None:
                    print(f"{nameplugin} / {descriptionplugin}")
                else:
                    print(f"{nameplugin} / <no description>")
                break
            else:
                print(f"Error: description not found in {manifest_path}")

def plugin_run_script():
    # Get the path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the source.py file
    source_path = os.path.join(script_dir, "plugins", curput, "source.py")

    # Check if the source file exists
    if not os.path.exists(source_path):
        print("Error: source.py not found.")
    else:
        # Open the source file
        os.startfile(source_path)  # For Windows
        # os.system("open " + source_path) <- macOS
        # os.system("xdg-open " + source_path) <- Linux

while True:
    user_input = input("Enter command: ")
    if user_input.lower() in ["help", "?"]:
        help_script()
    elif user_input.lower() in ["pan", "panick", "hide", "p"]:
        panick_script()
    elif user_input.lower() in ["cmd"]:
        cmd_script()
    elif user_input.lower() in ["shell", "powershell"]:
        shell_script()
    elif user_input.lower() in ["reg", "rege", "regedit", "re"]:
        reg_script()
    elif user_input.lower() in ["note", "notepad"]:
        note_script()
    elif user_input.lower().startswith("plugin run "):
        curputplace = user_input.split(" ")
        curput = curputplace[2]
        plugin_run_script()
    elif user_input.lower() in ["plugin list"]:
        plugin_list_script()
    else:
        print('Please input a valid command')
