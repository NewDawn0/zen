from utils.cursor import Cursor
from utils.undo_redo import Action
from utils.undo_redo import ActionType
from utils.undo_redo import TreeNode


# All hail the spaghetti code
# Uses fast list concat by replacing lists


class ListBuf:
    def __init__(self, text: str = "") -> None:
        self.__buf = list(text)
        self.__root = TreeNode(None, None)
        self.__rcurrent = self.__root

    # All "private" methods start with a double underscore
    # And all public start with a single underscore not to clash names with and accidentally override inherited stuff from textual.widgets.Static
    # Man why does Python lack good oop with acutal privates like any reasonable language like C++, Java, C# ...
    def __cursor_to_pos(self, cursor: Cursor) -> int:
        lines = "".join(self.__buf).split("\n")
        if cursor.line > len(lines):
            return len(self.__buf)
        col = min(
            cursor.col, len(lines[cursor.line]) if cursor.line < len(lines) else 0
        )
        pos = sum(len(line) + 1 for line in lines[: cursor.line])
        pos += col
        return self.__ajust(pos)

    def __insert(self, text: str, pos: int) -> None:
        self.__buf[pos:pos] = list(text)

    def __remove(self, start: int, end: int) -> None:
        del self.__buf[start:end]

    def _insert(self, text: str, pos: Cursor) -> None:
        start = self.__cursor_to_pos(pos)
        # Add the action to the undo tree
        self.__rcurrent.add(ActionType(Action.Remove, start, start + len(text)))
        self.__rcurrent = self.__rcurrent.children[-1]
        # Execute the action
        self.__insert(text, start)

    def _remove(self, start: Cursor, end: Cursor) -> None:
        start = self.__cursor_to_pos(start)
        end = self.__cursor_to_pos(end)
        if start > end:
            start, end = end, start
        # Add the action to the undo tree
        end += 1
        self.__rcurrent.add(
            ActionType(Action.Insert, "".join(self.__buf[start:end]), start)
        )
        self.__rcurrent = self.__rcurrent.children[-1]
        self.__remove(start, end)

    def _replace(self, text: str, pos: Cursor) -> None:
        pos = self.__cursor_to_pos(pos)
        amount = pos + len(text) - len(self.__buf)
        is_extended = bool(amount > 0)
        prev_txt = ""  # Initalize variable
        if not is_extended:
            prev_txt = "".join(self.__buf[pos : pos + len(text)])
        else:
            prev_txt = "".join(self.__buf[pos : pos + len(text) - amount])
            self.__buf.extend([None] * amount)
        self.__rcurrent.add(ActionType(Action.Replace, pos, pos + len(text), prev_txt))
        self.__rcurrent = self.__rcurrent.children[-1]
        self.__buf[pos : pos + len(text)] = list(text)

    # Takes ptr to number and modifies it
    def __ajust(self, index: int) -> int:
        return min(max(0, index), len(self.__buf))

    def __repr__(self) -> str:
        return "".join(self.__buf)

    def _undo(self, amount: int = 1) -> None:
        amount = max(1, amount)
        for _ in range(amount):
            if self.__rcurrent.parent:
                self.__exec_action()
                self.__rcurrent = self.__rcurrent.parent
            else:
                print("Nothing to undo")

    def _redo(self, amount: int = 1):
        amount = max(1, amount)
        for _ in range(amount):
            if self.__rcurrent.children:
                self.__rcurrent = self.__rcurrent.children[-1]
                self.__exec_action()
            else:
                print("Nothing to redo")

    def __exec_action(self):
        a = self.__rcurrent.action
        if a is not None:
            match a.action:
                case Action.Remove:
                    self.__remove(a.arg1, a.arg2)
                case Action.Insert:
                    self.__insert(a.arg1, a.arg2)
                case Action.Replace:
                    # Replace uses delete and insert as replace could have resized
                    # Args | int start, int end, char* text |
                    self.__remove(a.arg1, a.arg2)
                    self.__insert(a.arg3, a.arg1)
        else:
            # Todo maybe add better error or signals IDK
            print("Nothing to do")


buf = ListBuf("Hello World!")
print(buf)
buf._remove(Cursor(0, 6), Cursor(0, 11))
print(buf)
buf._undo()
print(buf)
buf._insert("cruel ", Cursor(0, 6))
print(buf)
buf._replace("niice ", Cursor(0, 6))
print(buf)
buf._undo()
print(buf)
