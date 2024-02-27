# Import neccesary modules
import threading

from zen.utils.globals.config import CONFIG


# Class to handle key chording functionality
class KeyChorder:
    def __init__(self):
        # Initialize variables
        self.keys: list[str] = []
        self.timeout = CONFIG.key_chord_timeout
        self.lock = threading.Lock()
        self.timer = None

        # Dictionary to map keys for normalization
        self.repl_map = {
            "space": "spc",
            "escape": "esc",
            "left_parenthesis": "(",
            "right_parenthesis": ")",
            "left_square_bracket": "[",
            "right_square_bracket": "]",
            "left_curly_bracket": "{",
            "right_curly_bracket": "}",
            "backspace": "bspc",
        }

    # Add a key to the pressed keys list
    def add(self, key: str) -> None:
        self.keys.append(self._normalize(key))
        with self.lock:
            if self.timer:
                self.timer.cancel()
            self.timer = threading.Timer(0.5, self.clear_keys)
            self.timer.start()

    # Clear the pressed keys list
    def clear_keys(self):
        with self.lock:
            self.keys = []

    # Try to execute a key combination
    def try_exec(self) -> int:
        keys = tuple(self.keys)
        length = len(self.keys)
        if fn := CONFIG.key_binds.get(keys):
            with self.lock:
                self.keys = []  # Clear keys
            fn()
            return length
        return 0  # Zero indicates an error

    # Get the current list of pressed keys
    def get(self) -> list[str]:  # TODO: AUTOREMOVE
        with self.lock:
            return self.keys

    # Normalize the provided key
    def _normalize(self, key: str) -> str:
        return self.repl_map.get(key) or key
