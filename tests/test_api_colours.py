import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from api.colours import *


def test_colours_initialization():
    # Test that the color values are correctly set
    assert COLOURS.bg == "#141b1e"
    assert COLOURS.light_bg == "#232a2d"
    assert COLOURS.red == "#e57474"
    assert COLOURS.green == "#8ccf7e"
    assert COLOURS.yellow == "#e5c76b"
    assert COLOURS.blue == "#67b0e8"
    assert COLOURS.magenta == "#c47fd5"
    assert COLOURS.cyan == "#6cbfbf"
    assert COLOURS.light_gray == "#b3b9b8"
    assert COLOURS.white == "#dadada"
    assert COLOURS.win_border == COLOURS.magenta
    assert COLOURS.fg == COLOURS.white
    assert COLOURS.menu_bg == COLOURS.bg
    assert COLOURS.file_name == COLOURS.fg
    assert COLOURS.file_ext == COLOURS.light_gray
    assert COLOURS.dir_name == COLOURS.blue


def test_mk_theme():
    # Test that _mk_theme returns a TextAreaTheme object with the expected styles
    theme = COLOURS._mk_theme()
    assert isinstance(theme, TextAreaTheme)
    assert theme.name == "theme"
    assert theme.base_style == Style(color=COLOURS.fg, bgcolor=COLOURS.bg)
    assert theme.gutter_style == Style(color=COLOURS.light_gray)
    assert theme.cursor_style == Style(color=COLOURS.bg, bgcolor=COLOURS.fg)
    assert theme.cursor_line_style == Style(bgcolor=COLOURS.light_bg)
    assert theme.cursor_line_gutter_style == Style(
        color=COLOURS.red, bgcolor=COLOURS.bg, bold=True
    )
    assert theme.bracket_matching_style == Style(
        bgcolor=COLOURS.green, bold=True, underline=True
    )
    assert theme.selection_style == Style(bgcolor=COLOURS.light_gray)
    # Add more assertions for the syntax_styles dictionary as needed
