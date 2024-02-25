# Import necessary modules
from os import path
from pathlib import Path

# Import required classes and functions
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import DirectoryTree

# Import custom APIs and colors
from api.builtins import BUILTINS
from api.colours import COLOURS as C

# Define a container for displaying a file tree
class FileTree(Container):
    # CSS styles for the file tree container
    DEFAULT_CSS = f"""
    FileTree {{
        width: 30;
        height: 100%;
        dock: left;
        background: {C.menu_bg};
        border-right: solid {C.win_border};
    }}
    FileTree.-hidden {{
        display: none;
    }}
    """

    # Event handler for when a file is selected in the directory tree
    def on_directory_tree_file_selected(self, msg: DirectoryTree.FileSelected) -> None:
        # Open the selected file in a buffer
        BUILTINS.open_buf(str(msg.path))
        self.notify(str(msg.path))

    # Compose method to yield the styled directory tree
    def compose(self) -> ComposeResult:
        yield StyledTree(".")


# Subclass of DirectoryTree with custom styling
class StyledTree(DirectoryTree):
    def __init__(self, path: str, *args, **kwargs):
        super().__init__(path=path, *args, **kwargs)
        self.path = Path(path)
        self.guide_depth = 2
        self.show_guides = False

    # Key bindings for interacting with the styled tree
    BINDINGS = [
        ("enter", "select_cursor", "Select"),
        ("space", "select_cursor", "Toggle"),
        ("up", "cursor_up", "Cursor Up"),
        ("down", "cursor_down", "Cursor Down"),
        ("k", "cursor_up", "Cursor Up"),
        ("j", "cursor_down", "Cursor Down"),
    ]

    # CSS styles for the styled tree
    DEFAULT_CSS = f"""
    StyledTree {{
        padding-left: 1;
        layer: below;
        background: {C.menu_bg};
    }}
    StyledTree > .directory-tree--extension {{
        text-style: italic;
        color: {C.file_ext};
    }}
    StyledTree > .directory-tree--file {{
        text-style: none;
        color: {C.fg};
    }}
    StyledTree > .directory-tree--folder {{
        text-style: none;
        color: {C.dir_name};
    }}
    """
