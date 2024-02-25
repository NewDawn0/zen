# Import necessary modules
from os.path import exists
from os.path import splitext

from textual import events
from textual.app import ComposeResult
from textual.widgets import Static
from textual.widgets import TabbedContent
from textual.widgets import TextArea
from textual.widgets.text_area import LanguageDoesNotExist

from api.colours import COLOURS
from components.popup import PopUp
from utils.ft import lookup
from utils.globals.bufs import BUF_NAME_TO_TEXT_BUF_DICT
from utils.globals.bufs import CURR_BUF
from utils.globals.keys import KEYS

# All hail the spaghetti code that follows

TEXT_BUF_TO_BUF_NAME_DICT = {}


class BufManagerWrapper(Static):
    def __init__(self, bufs: set[str], *args, **kwargs):
        # Initialize BufManagerWrapper with a set of buffers
        self._bufs = set(bufs)
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        # Compose the BufManager
        yield BufManager(self._bufs)

    def _quit(self):
        # Remove buffer and handle exceptions
        self.children[0].remove()
        try:
            if CURR_BUF:
                self._bufs.remove(CURR_BUF)
            elif buf := BUF_NAME_TO_TEXT_BUF_DICT.get(CURR_BUF or ""):
                self._bufs.remove(buf)
        except:  # noqa: E722
            self.notify(
                f"Unable to kill buffer: {CURR_BUF}\n Active buffers are {', '.join(self._bufs)}",
                severity="error",
            )
        if len(self._bufs) > 0:
            self.mount(BufManager(self._bufs))

    def _open(self, fname: str | None = None) -> None:
        # Open a buffer or display a popup for a new buffer
        if fname and fname != "":
            self._remount(fname)
        else:
            self.mount(PopUp("New buffer name", self))

    def _remount(self, fname: str) -> None:
        # Remount a buffer
        self._bufs = set({fname, *self._bufs})  # Head insert
        self.children[0].remove()
        self.mount(BufManager(self._bufs))

    def _get_popup_text(self, text: str):
        # Get text for the popup
        self._remount(text)


class BufManager(Static):
    def __init__(self, bufs: set[str], *args, **kwargs):
        # Initialize BufManager with a set of buffers
        self._bufs = set(bufs)
        super().__init__(*args, **kwargs)

    def _save(self) -> None:
        # Save the current buffer
        if buf := BUF_NAME_TO_TEXT_BUF_DICT.get(CURR_BUF or ""):
            buf._save()
        self.notify(
            f"Sucessfully saved {CURR_BUF}\n",
        )

    def compose(self) -> ComposeResult:
        # Compose the buffer manager
        global CURR_BUF
        CURR_BUF = list(self._bufs)[0]
        self.tabbed = TabbedContent
        with self.tabbed(*self._bufs):
            for buf in self._bufs:
                yield TextBufWrapper(buf, name=buf)


class TextBuf(TextArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _on_focus(self, event: events.Focus) -> None:
        # Handle focus event
        global CURR_BUF
        CURR_BUF = TEXT_BUF_TO_BUF_NAME_DICT.get(self)._fname
        return super()._on_focus(event)

    def _on_key(self, event: events.Key) -> None:
        # Handle key event
        global CURR_BUF
        CURR_BUF = TEXT_BUF_TO_BUF_NAME_DICT.get(self)._fname
        auto_chars = {
            "{": "{}",
            "(": "()",
            "[": "[]",
            "'": "''",
            '"': '""',
        }
        optional_char = auto_chars.get(event.character or "")
        KEYS.add(str(event.key))
        if optional_char:
            self.insert(optional_char)
            self.move_cursor_relative(columns=-1)
            event.prevent_default()
            self._key_cleanup(KEYS.try_exec())
        elif event.is_printable:
            self.insert(event.character or "")
            event.prevent_default()
            self._key_cleanup(KEYS.try_exec())

    def _key_cleanup(self, amount: int) -> None:
        # Clean up keys
        if amount > 0:
            for _ in range(amount):
                self.action_delete_left()

    def _get_text(self) -> str:
        # Get the text
        return self.text


class TextBufWrapper(Static):
    def __init__(self, fname: str, *args, **kwargs):
        # Initialize TextBufWrapper with a filename
        self._fname = fname
        self._load()
        super().__init__(*args, **kwargs)

    def _on_focus(self, event: events.Focus) -> None:
        # Handle focus event
        global CURR_BUF
        CURR_BUF = self._fname
        return super()._on_focus(event)

    def compose(self) -> ComposeResult:
        # Compose the TextBufWrapper
        global TEXT_BUF_TO_BUF_NAME_DICT, BUF_NAME_TO_TEXT_BUF_DICT
        self.buf = TextBuf.code_editor(language=None, text=self._text)
        self.buf.register_theme(COLOURS._mk_theme())
        self.buf.theme = "theme"
        try:
            self.buf.language = self._ftype
        except LanguageDoesNotExist:
            self.notify(
                f"{self._fname}: No TreeSitter syntaxes set for language {self._ftype}",
                severity="error",
            )
        TEXT_BUF_TO_BUF_NAME_DICT[self.buf] = self
        BUF_NAME_TO_TEXT_BUF_DICT[self._fname] = self
        yield self.buf

    def _save(self):
        # Save the buffer
        txt = self.buf._get_text()
        with open(self._fname, "w", encoding="utf-8") as f:
            f.write(txt)

    def _get_ft(self):
        # Get file type
        _, ext = splitext(self._fname)
        self._ftype = lookup(ext[1:])

    def _load(self):
        # Load the buffer
        if not exists(self._fname):
            with open(self._fname, "w+", encoding="utf-8") as f:
                pass
        with open(self._fname, "r", encoding="utf-8") as f:
            self._text = f.read()
        self._get_ft()
