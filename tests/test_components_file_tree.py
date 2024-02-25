from typing import Generator

from zen.components.file_tree import *


# Test the FileTree class
def test_file_tree_compose():
    file_tree = FileTree()
    result = file_tree.compose()
    assert isinstance(result, Generator)


# Test the StyledTree class
def test_styled_tree_init():
    styled_tree = StyledTree("test_path")
    assert styled_tree.path == Path("test_path")
    assert styled_tree.guide_depth == 2
    assert styled_tree.show_guides == False


def test_styled_tree_bindings():
    styled_tree = StyledTree("test_path")
    assert styled_tree.BINDINGS == [
        ("enter", "select_cursor", "Select"),
        ("space", "select_cursor", "Toggle"),
        ("up", "cursor_up", "Cursor Up"),
        ("down", "cursor_down", "Cursor Down"),
        ("k", "cursor_up", "Cursor Up"),
        ("j", "cursor_down", "Cursor Down"),
    ]
