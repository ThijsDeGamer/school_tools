# school tools
School tools is a python tool that allows you to do advanced things on school pc's. The target of this project is to make it easier for people to use python scripts and tools on school pc's.
The project is for educational purposes only, nothing bad is intended with this project, so please don't hack your school with this.

# Using the tool on PC
1) Download the most recent version of windows.zip.
2) Copy the folder from the zip file out of the zip file.
3) Done!

# Using the tool on USB
1) Download WPy64-3830.zip at [release](https://github.com/ThijsDeGamer/school_tools/releases).
2) Open the zip file.
3) Copy the folder thats inside their onto a USB-Stick.
4) Download the latest version of School Tools from [release](https://github.com/ThijsDeGamer/school_tools/releases).
5) Open the zip file.
6) Copy the folder thats inside their onto a USB-Stick.
7) Open IDLEX.exe (can take some time to open).
8) Click on "File" and then click on "Open...".
9) Navigate to the "V1.0 Windows" folder and open it.
10) Open prompt.py.
11) Press F5 or click 'Run' and then 'Run module'.
--------------------------------------
Please note that the panick function doesn't work when it's ran like this.
The panick function only works when the script is ran from an installed python version.

# Installing plugins
Here's a quick tutorial on how to download plugins.
1) Download the plugin.
2) Put the folder that contains the plugin into "plugins".
3) Enjoy! To see a list of plugins run the following command: "plugin list". You can run plugins using the following command "plugin run plugin_name".

# Making plugins
1) Navigate to the plugins folder, you will find a plugin called example in there.
2) Duplicate the plugin and rename it to what you want to call your plugin.
3) Open your new plugin folder and open manifest.txt
4) Change example found after name= to the folder name of your plugin.
5) Add in a description after the line description= (removing any of the comments may cause issues)
6) Close manifest.txt and open help.txt
7) Type in the command prompt(s) that will run the command and add in a short description about what the command does.
8) Close help.txt and start editing source.py (this can be done with notepad by renaming source.py to source.txt)
9) I can't help you very far here so I'm just going put a hello world print command down here: (remember to never remove the help function!)

```
import os

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

def print_script():
     print("Hello World!")

while True:
    user_input = input("Enter command: ")
    if user_input.lower() in ["help", "?"]:
        help_script()
    elif user_input.lower() in ["print"]:
        print_script()
    else:
        print('Please input a valid command')
