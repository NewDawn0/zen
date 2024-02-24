import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from utils.ft import *


def test_lookup_known_extension():
    # Test with a known extension
    ext = "py"
    expected = "python"
    assert lookup(ext) == expected


def test_lookup_unknown_extension():
    # Test with an unknown extension
    ext = "xyz"
    expected = None
    assert lookup(ext) == expected


def test_lookup_uppercase_extension():
    # Test with an uppercase extension
    ext = "PY"
    expected = "python"
    assert lookup(ext) == expected


def test_lookup_mixed_case_extension():
    # Test with a mixed case extension
    ext = "Py"
    expected = "python"
    assert lookup(ext) == expected


def test_lookup_empty_extension():
    # Test with an empty extension
    ext = ""
    expected = None
    assert lookup(ext) == expected


def test_lookup_with_dot():
    # Test with extension including a dot
    ext = ".py"
    expected = None
    assert lookup(ext) == expected


def test_lookup_with_dot_uppercase():
    # Test with extension including a dot and uppercase
    ext = ".PY"
    expected = None
    assert lookup(ext) == expected
