class Cursor:
    def __init__(self, line: int = 0, col: int = 0) -> None:
        self.line = line
        self.col = col

    @property
    def line(self) -> int:
        return self._line

    @line.setter
    def line(self, val: int) -> None:
        self._line = max(0, val)

    @property
    def col(self) -> int:
        return self._col

    @col.setter
    def col(self, val: int) -> None:
        self._col = max(0, val)

    def __repr__(self) -> str:
        return f"Cursor(line={self.line}, column={self.col})"
