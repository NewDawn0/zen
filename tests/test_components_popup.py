import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from components.popup import *

# Mock the global TEXT variable
TEXT = ""


class Callback:
    def _get_popup_text(self, text: str) -> None:
        self.text = text

    def _remove(self) -> None:
        self.text = ""


callback = Callback()


def test_popup_init():
    # Test the initialization of the PopUp class
    popup = PopUp("Test Text", None)
    assert popup._text == "Test Text"
    assert popup._callback is None


def test_popup_compose():
    # Test the compose method of the PopUp class
    popup = PopUp("Test Text", None)
    compose_result = list(popup.compose())
    assert len(compose_result) == 2
    assert isinstance(compose_result[0], Static)
    assert isinstance(compose_result[1], Enter)


def test_enter_init():
    # Test the initialization of the Enter class
    enter = Enter(None)
    assert enter._callback is None


def test_enter_on_key():
    # Test the _on_key method of the Enter class
    enter = Enter(callback)
    enter.text = ""
    enter._on_key(events.Key(key="enter", character=""))
    assert callback.text == ""
