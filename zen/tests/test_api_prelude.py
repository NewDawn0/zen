import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from api.prelude import UserConfig, KEYBIND, ACTION


def test_user_config_initialization():
    # Test that UserConfig initializes with an empty key_binds dictionary
    config = UserConfig()
    assert config.key_binds == {}


def test_user_config_add_keybind():
    # Test adding a keybind to the UserConfig
    config = UserConfig()
    keybind = ("ctrl", "s")
    action = lambda: print("Save")
    config.key_binds[keybind] = action
    assert keybind in config.key_binds
    assert config.key_binds[keybind] == action


def test_user_config_remove_keybind():
    # Test removing a keybind from the UserConfig
    config = UserConfig()
    keybind = ("ctrl", "s")
    action = lambda: print("Save")
    config.key_binds[keybind] = action
    del config.key_binds[keybind]
    assert keybind not in config.key_binds
