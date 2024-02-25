from typing import get_type_hints
from typing import Type
from typing import TypeVar

T = TypeVar("T")


# Acts as a mutable dataclass
def nullable_struct(cls: Type[T]) -> Type[T]:
    # Constructor to create nullable structure
    def __init__(self, **kwargs):
        markers = get_type_hints(cls)
        defaults = {k: v for k, v in cls.__dict__.items() if not k.startswith("__")}
        for name, _type in markers.items():
            if name in kwargs:
                setattr(self, name, kwargs.get(name))
            elif name in defaults:
                setattr(self, name, defaults.get(name))
            else:
                setattr(self, name, kwargs.get(name))  # Sets it to None

    # Useful dunder methods for nullable structure
    # Representation for string output
    def __str__(self) -> str:
        args = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({args})"

    def __repr__(self) -> str:
        return str(self)

    # Comparison of nullable structures
    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    # Set the dunder methods for the class
    setattr(cls, "__init__", __init__)
    setattr(cls, "__str__", __str__)
    setattr(cls, "__repr__", __repr__)
    setattr(cls, "__eq__", __eq__)
    return cls


def struct(check_type: bool = True):
    def _struct(cls: Type[T]) -> Type[T]:
        # Constructor to create structure
        def __init__(self, *args, **kwargs):
            markers = get_type_hints(cls)
            defaults = {k: v for k, v in cls.__dict__.items() if not k.startswith("__")}
            for i, (name, _type) in enumerate(markers.items()):
                if i < len(args):
                    if check_type:
                        _check_type(args[i], _type)
                    setattr(self, name, args[i])
                if name in kwargs:
                    if check_type:
                        _check_type(kwargs.get(name), _type)
                    setattr(self, name, kwargs.get(name))
                elif name in defaults:
                    if check_type:
                        _check_type(defaults.get(name), _type)
                    setattr(self, name, defaults.get(name))
                else:
                    raise TypeError(
                        f"Missing required argument {name} of type {_type}"
                    )  # Sets it to None

        # Private helper method to check type
        def _check_type(item, _type):
            if not isinstance(item, _type):
                raise TypeError(f"Expected {_type}, got {type(item)}")

        # Useful dunder methods for structure
        # Representation for string output
        def __str__(self) -> str:
            args = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
            return f"{self.__class__.__name__}({args})"

        def __repr__(self) -> str:
            return str(self)

        # Comparison of structures
        def __eq__(self, other) -> bool:
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__
            return NotImplemented

        # Set the dunder methods for the class
        setattr(cls, "__init__", __init__)
        setattr(cls, "__str__", __str__)
        setattr(cls, "__repr__", __repr__)
        setattr(cls, "__eq__", __eq__)
        return cls

    return _struct
