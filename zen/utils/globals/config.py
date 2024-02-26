# Import and load user config from the main function in userConfig module
import os
import sys

from zen.gen import CONTENTS

# Create __init__ if it does not exist
main_py_path = os.path.expanduser("~/.config/zen/__init__.py")
if not os.path.exists(main_py_path):
    config_dir = os.path.expanduser("~/.config/zen")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    main_py_dst = os.path.join(config_dir, "__init__.py")
    if not os.path.exists(main_py_dst):
        with open(main_py_path, "w+") as f:
            f.write(CONTENTS)

# Push the user config
sys.path.insert(0, os.path.dirname(main_py_path))
import __init__ as user

CONFIG = user.main()

# Pop the user config
sys.path.pop(0)
