import sys
import os
import glob
import subprocess

curput = ""

def help_script():
    file_name = "help.txt"

    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"{file_name} not found.")

def panick_script():
    sys.exit()

def cmd_script():
    file_path = r"C:\Windows\system32\cmd"
    subprocess.Popen(["start", file_path], shell=True)

def shell_script():
    file_path = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell"
    subprocess.Popen(["start", file_path], shell=True)

def reg_script():
    file_path = r"C:\Windows\regedit"
    subprocess.Popen(["start", file_path], shell=True)

def note_script():
    file_path = r"C:\Windows\notepad"
    subprocess.Popen(["start", file_path], shell=True)

def plugin_list_script():
    # Get the path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the manifest.txt file
    manifest_path = os.path.join(script_dir, "plugins", "*", "manifest.txt")

    # Find the path to the manifest.txt file
    manifest_files = glob.glob(manifest_path)
    if len(manifest_files) == 0:
        print("Error: manifest.txt not found.")
        return

    manifest_file = manifest_files[0]

    # Read the value of "syntax" from the manifest.txt file
    with open(manifest_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("name="):
                continue
            nameplugin = line[len("name="):].split("#")[0]
            descriptionplugin = None
            for line in f:
                line = line.strip()
                if line.startswith("description="):
                    descriptionplugin = line[len("description="):].split("#")[0]
                    break
            if descriptionplugin is not None:
                print(f"{nameplugin}/ {descriptionplugin}")
            else:
                print(f"{nameplugin}/ <no description>")
            break
        else:
            print("Error: name not found in manifest.txt.")

def plugin_run_script():
    # Get the path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the source.py file
    source_path = os.path.join(script_dir, "plugins", curput, "source.py")

    # Check if the source file exists
    if not os.path.exists(source_path):
        print("Error: source.py not found.")
        exit()

    # Open the source file
    os.startfile(source_path)  # For Windows
    # Alternatively, use the following line for macOS:
    # os.system("open " + source_path)
    # Use the following line for Linux:
    # os.system("xdg-open " + source_path)
    


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

