from setuptools import find_packages
from setuptools import setup


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
)
