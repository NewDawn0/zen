from dataclasses import dataclass
from enum import Enum

class Action(Enum):
    Insert = 0
    Remove = 1
    Replace = 2


@dataclass
class ActionType:
    action: Action
    arg1: int
    arg2: int | str
    arg3: int | None = None


class TreeNode:
    def __init__(self, action: ActionType | None, parent) -> None:
        self.action = action
        self.parent = parent
        self.children = []

    def add(self, action: ActionType):
        node = TreeNode(action, self)
        self.children.append(node)
        return node

    def __repr__(self) -> str:
        return f"TreeNode(action={self.action})"


# class Editor:
#     def __init__(self, initial_text: str = ""):
#         self.root = TreeNode(initial_text)
#         self.current = self.root
#
#     def edit(self, text):
#         self.current = self.current.add(text)
#
#     def undo(self, amount: int = 1):
#         amount = max(1, amount)  # Normalize
#         for _ in range(amount):
#             if self.current.parent:
#                 self.current = self.current.parent
#
#     def redo(self, amount: int = 1):
#         amount = max(1, amount)  # Normalize
#         for _ in range(amount):
#             if self.current.children:
#                 self.current = self.current.children[-1]
#
#     def __repr__(self) -> str:
#         return self.current.text
#
#
# ed = Editor("Init")
# print(ed)
# ed.edit("Hello")
# print(ed)
# ed.edit("Hallo Welt")
# print(ed)
#
# ed.undo(2)
# print(ed)
# ed.redo(2)
# print(ed)
# ed.undo()
# print(ed)
