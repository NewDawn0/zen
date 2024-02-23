# Import necessary modules
from textual.app import App
from textual.notifications import SeverityLevel
from textual.widget import Widget

from utils.globals.bufs import BUF_NAME_TO_TEXT_BUF_DICT
from utils.globals.bufs import CURR_BUF


# Works via callbacks using a reference to WinMain from main
class Builtins:
    def __init__(self, app: App | None) -> None:
        self._app = app

    def notify(self, msg: str, severity: SeverityLevel = "information") -> None:
        # Notify with a message and severity level
        if app := self._app:
            app.notify(msg, severity=severity)

    def bell(self) -> None:
        # Trigger a bell notification
        if app := self._app:
            app.bell()

    def toggle_widget(self, widget: Widget) -> None:
        # Toggle the visibility of a widget by toggling a CSS class
        if app := self._app:
            app.query_one(widget).toggle_class("-hidden")

    def quit(self) -> None:
        # Exit the application
        if app := self._app:
            app.exit()

    def quit_buf(self) -> None:
        # Quit the current buffer
        if app := self._app:
            app.query_one("BufManagerWrapper")._quit()

    def save_buf(self) -> None:
        # Save the current buffer
        if app := self._app:
            app.query_one("BufManager")._save()

    def open_buf(self, file_name: str | None = None) -> None:
        # Open a buffer with a given file name
        if app := self._app:
            app.query_one("BufManagerWrapper")._open(file_name)


# Initialize the built-in functions with a None App
BUILTINS = Builtins(None)
