# Import neccesary modules
import threading

from zen.utils.globals.config import CONFIG


# Class to handle key chording functionality
class KeyChorder:
    def __init__(self, timeout=0.5):
        # Initialize variables
        self.pressed_key: list[str] = []
        self.timeout = timeout
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
        self.pressed_key.append(self._normalize(key))
        self._reset_timer()

    # Try to execute a key combination
    def try_exec(self) -> int:
        keys = tuple(self.pressed_key)
        length = len(self.pressed_key)
        if fn := CONFIG.key_binds.get(keys):
            self.pressed_key.clear()  # Clear keys
            fn()
            return length
        return 0  # Zero indicates an error

    # Reset the timer for key chord timeout
    def _reset_timer(self) -> None:
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.timeout, self.clear)
        self.timer.start()

    # Clear the pressed keys list
    def clear(self) -> None:  # TODO: AUTOREMOVE
        self.pressed_key.clear()

    # Get the current list of pressed keys
    def get(self) -> list[str]:  # TODO: AUTOREMOVE
        return self.pressed_key

    # Normalize the provided key
    def _normalize(self, key: str) -> str:
        return self.repl_map.get(key) or key
