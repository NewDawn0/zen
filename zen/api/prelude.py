# Import necessary modules and objects
from typing import Callable
from typing import TypeAlias

from api.builtins import BUILTINS
from components.file_tree import FileTree
from utils.struct import nullable_struct

# Define type aliases for keybinds and actions
KEYBIND: TypeAlias = tuple[str, ...]
ACTION: TypeAlias = Callable[..., None]  # void ... (*args, **nargs)

# BUILTINS: Access to built-in functions
# FileTree: Component for displaying file tree

# UserConfig: User configuration settings
# key_binds: Dictionary of keybinds and corresponding actions


@nullable_struct
class UserConfig:
    key_binds: dict[KEYBIND, ACTION] = {}
