import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from components.text_buffer import *


def test_text_buf_wrapper_save():
    filename = "tests/test_file.txt"
    initial_content = "Initial content"
    expected_content = "New content"

    # Create TextBufWrapper with initial content
    text_buf_wrapper = TextBufWrapper(filename)
    text_buf_wrapper._text = initial_content

    # Save the buffer
    # assert text_buf_wrapper.
    text_buf_wrapper.buf = TextBuf.code_editor(language=None, text=initial_content)
    text_buf_wrapper._save()

    # Read the file content
    with open(filename, "r") as file:
        saved_content = file.read()

    assert saved_content == initial_content  # Content should remain the same initially

    # Update the buffer content
    text_buf_wrapper.buf.text = expected_content

    # Save the buffer again
    text_buf_wrapper._save()

    # Read the file content again
    with open(filename, "r") as file:
        saved_content = file.read()

    assert saved_content == expected_content  # Content should be updated after saving
    os.remove("tests/test_file.txt")
