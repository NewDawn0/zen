import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def run_tests():
    # Get the path to the tests directory
    tests_dir = os.path.dirname(os.path.abspath(__file__))

    # Iterate over the files in the tests directory
    for filename in os.listdir(tests_dir):
        print(filename)
        # Check if the file is a Python test module
        if filename.startswith("test_") and filename.endswith(".py"):
            # Import the test module
            module_name = filename[:-3]  # Remove the ".py" extension
            module = __import__(f"tests.{module_name}", fromlist=["*"])
            globals().update(vars(module))

    # Run all discovered tests
    pytest.main(["-v"])

run_tests()
