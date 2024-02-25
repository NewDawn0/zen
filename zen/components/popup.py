# Import necessary modules
from textual import events
from textual.widgets import Static
from textual.widgets import TextArea

from api.colours import COLOURS as C

# Initialize global variable
TEXT: str = ""


class PopUp(Static):
    # Define default CSS styles
    DEFAULT_CSS = f"""
    PopUp {{
        width: 30;
        height: 20%;
        dock: right;
        background: {C.menu_bg};
        border: solid {C.win_border};
    }}
    """

    def __init__(self, text: str, callback, *args, **kwargs):
        # Initialize PopUp with text and callback function
        self._text = text
        self._callback = callback
        super().__init__(*args, **kwargs)

    def compose(self):
        # Display text and Enter widget
        yield Static(self._text)
        yield Enter(self)

    def _remove(self) -> None:
        # Call callback function with entered text and remove PopUp
        self._callback._get_popup_text(TEXT)
        self.remove()


class Enter(TextArea):
    def __init__(self, callback, *args, **kwargs):
        # Initialize Enter widget with callback function
        self._callback = callback
        super().__init__(*args, **kwargs)
        self.focus()

    def _on_key(self, event: events.Key) -> None:
        global TEXT
        if event.key == "enter":
            # Capture entered text on Enter key press
            TEXT = self.text
            self._callback._remove()
