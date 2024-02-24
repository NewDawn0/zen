import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from main import *


def test_main_class_initialization():
    # Test that the Main class initializes correctly
    bufs = ["file1.txt", "file2.txt"]
    app = Main(bufs)
    assert app._bufs == bufs


def test_main_class_compose():
    # Test that the compose method yields the correct components
    bufs = ["file1.txt", "file2.txt"]
    app = Main(bufs)
    components = list(app.compose())
    assert len(components) == 2
    assert isinstance(components[0], FileTree)
    assert isinstance(components[1], BufManagerWrapper)


@patch("sys.argv", ["main.py"])
def test_main_function_without_args(capsys):
    # Test that the main function exits with an error message when no arguments are provided
    with pytest.raises(SystemExit) as excinfo:
        main()
    captured_err = str(excinfo.value)  # Capture the message passed to sys.exit()
    assert "Provide at least one filename/filepath" in captured_err
