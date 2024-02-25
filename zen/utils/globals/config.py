# Import and load user config from the main function in userConfig module
import os
import sys

main_py_path = os.path.expanduser("~/.config/zen/__init__.py")
if not os.path.exists(main_py_path):
    exit("__init__.py not found in ~/.config/zen/")

# Push the user config
sys.path.insert(0, os.path.dirname(main_py_path))
import __init__ as user

CONFIG = user.main()

# Pop the user config
sys.path.pop(0)
