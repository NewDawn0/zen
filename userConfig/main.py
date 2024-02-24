# Prelude insipred by Rust's use crate::prelude::*
from api.prelude import *


# Automatically called on app load
def main() -> UserConfig:
    # Initializes and returns a UserConfig object with predefined key bindings.
    config = UserConfig()
    config.key_binds = {
        # Type of lamba is fn(Cursor|None, Cursor|None) -> Any
        # Altough the return type is ignored
        ("spc", "e"): lambda: BUILTINS.toggle_widget(FileTree),
        ("ctrl+i", "spc", "i"): lambda: BUILTINS.notify(
            "Zen, built with textual by NewDawn0"
        ),
        ("ctrl+o", "spc", "o"): lambda: open_browser(),
        ("Z", "Z"): lambda: BUILTINS.quit(),
        ("spc", "w"): lambda: BUILTINS.save_buf(),
        ("spc", "q"): lambda: BUILTINS.quit_buf(),
        ("spc", "o"): lambda: BUILTINS.open_buf(),
    }
    return config


# RVal will be ignored
import subprocess


def open_browser():
    # Opens the Firefox browser using subprocess on Mac.
    # Tested on Mac, Only works on mac due to the open command being mac specific
    BUILTINS.notify("Opening firefox")
    subprocess.call(["open", "-a", "firefox"])
