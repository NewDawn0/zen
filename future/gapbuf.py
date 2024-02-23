from utils.cursor import Cursor
from utils.undo_redo import Action
from utils.undo_redo import ActionType
from utils.undo_redo import TreeNode


# All hail the spaghetti code
# Uses fast list concat by replacing lists
class ListBuf:
    def __init__(self, text: str = "") -> None:
        self._buf = list(text)
        self._root = TreeNode(None, None)
        self._current = self._root

    def _cursor_to_pos(self, cursor: Cursor) -> int:
        lines = "".join(self._buf).split("\n")
        if cursor.line > len(lines):
            return len(self._buf)
        col = min(
            cursor.col, len(lines[cursor.line]) if cursor.line < len(lines) else 0
        )
        pos = sum(len(line) + 1 for line in lines[: cursor.line])
        pos += col
        return self._ajust(pos)

    def _insert(self, text: str, pos: int) -> None:
        self._buf[pos:pos] = list(text)

    def _remove(self, start: int, end: int) -> None:
        del self._buf[start:end]

    def insert(self, text: str, pos: Cursor) -> None:
        start = self._cursor_to_pos(pos)
        # Add the action to the undo tree
        self._current.add(ActionType(Action.Remove, start, start + len(text)))
        self._current = self._current.children[-1]
        # Execute the action
        self._insert(text, start)

    def remove(self, start: Cursor, end: Cursor) -> None:
        start = self._cursor_to_pos(start)
        end = self._cursor_to_pos(end)
        if start > end:
            start, end = end, start
        # Add the action to the undo tree
        end += 1
        self._current.add(
            ActionType(Action.Insert, "".join(self._buf[start:end]), start)
        )
        self._current = self._current.children[-1]
        self._remove(start, end)

    def replace(self, text: str, pos: Cursor) -> None:
        pos = self._cursor_to_pos(pos)
        amount = pos + len(text) - len(self._buf)
        is_extended = bool(amount > 0)
        prev_txt = ""  # Initalize variable
        if not is_extended:
            prev_txt = "".join(self._buf[pos : pos + len(text)])
        else:
            prev_txt = "".join(self._buf[pos : pos + len(text) - amount])
            self._buf.extend([None] * amount)
        self._current.add(ActionType(Action.Replace, pos, pos + len(text), prev_txt))
        self._current = self._current.children[-1]
        print("PREV:", prev_txt)
        self._buf[pos : pos + len(text)] = list(text)

    # Takes ptr to number and modifies it
    def _ajust(self, index: int) -> int:
        return min(max(0, index), len(self._buf))

    def __repr__(self) -> str:
        return "".join(self._buf)

    def undo(self, amount: int = 1) -> None:
        amount = max(1, amount)
        for _ in range(amount):
            if self._current.parent:
                self._exec_action()
                self._current = self._current.parent
            else:
                print("Nothing to undo")

    def redo(self, amount: int = 1):
        amount = max(1, amount)
        for _ in range(amount):
            if self._current.children:
                self._current = self._current.children[-1]
                self._exec_action()
            else:
                print("Nothing to redo")

    def _exec_action(self):
        a = self._current.action
        if a is not None:
            match a.action:
                case Action.Remove:
                    self._remove(a.arg1, a.arg2)
                case Action.Insert:
                    self._insert(a.arg1, a.arg2)
                case Action.Replace:
                    # Replace uses delete and insert as replace could have resized
                    # Args | int start, int end, char* text |
                    self._remove(a.arg1, a.arg2)
                    self._insert(a.arg3, a.arg1)
        else:
            # Todo maybe add better error or signals IDK
            print("Nothing to do")


# buf = ListBuf("Hello World!")
# print(buf)
# buf.remove(Cursor(0, 6), Cursor(0, 11))
# print(buf)
# buf.undo()
# print(buf)
# buf.insert("cruel ", Cursor(0, 6))
# print(buf)
# buf.replace("niice ", Cursor(0, 6))
# print(buf)
# buf.undo()
# print(buf)
