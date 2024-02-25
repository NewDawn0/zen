import os
from shutil import copyfile

from setuptools import find_packages
from setuptools import setup


def copy_user_conf():
    config_dir = os.path.expanduser("~/.config/zen")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    main_py_dst = os.path.join(config_dir, "__init__.py")
    if not os.path.exists(main_py_dst):
        copyfile("gen/__init__.py", main_py_dst)


copy_user_conf()

REQUIREMENTS_FILE = "zen/requirements.txt"
REQUIRED = None
with open(REQUIREMENTS_FILE, "r") as f:
    REQUIRED = [line.strip() for line in f]

setup(
    name="zen",
    version="0.0.1",
    packages=find_packages(),
    install_requires=REQUIRED,
    entry_points={
        "console_scripts": [
            "zen = zen.main:main",
        ]
    },
    data_files=[(os.path.expanduser("~/.config/zen"), ["gen/__init__.py"])],
)
