import os
import sys

from api.prelude import UserConfig

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from utils.globals.config import *


def some_mock_func():
    pass


def mock_user_main() -> UserConfig:
    cfg = UserConfig()
    return cfg


def test_config():
    cfg = mock_user_main()
    # Assert that CONFIG is correctly returned
    assert cfg == UserConfig()
