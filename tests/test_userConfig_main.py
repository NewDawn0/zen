import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest.mock import patch
import pytest

from userConfig.main import *


def test_main_initializes_user_config_with_key_bindings():
    config = main()
    assert isinstance(config, UserConfig)
    assert len(config.key_binds) == 7
    assert ("spc", "e") in config.key_binds
    assert ("ctrl+i", "spc", "i") in config.key_binds
    assert ("ctrl+o", "spc", "o") in config.key_binds
    assert ("Z", "Z") in config.key_binds
    assert ("spc", "w") in config.key_binds
    assert ("spc", "q") in config.key_binds
    assert ("spc", "o") in config.key_binds


@patch("subprocess.call")
def test_open_browser_calls_subprocess_with_correct_arguments(mock_call):
    open_browser()
    mock_call.assert_called_once_with(["open", "-a", "firefox"])
