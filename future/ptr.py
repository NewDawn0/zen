from typing import Any
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


# A poor mans pointer using mutble encapsulation
class Pointer(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        return self._value

    def set(self, value: T) -> None:
        self._value = value

    def __call__(self, value: T) -> None:
        self.set(value)

    def deref(self) -> "Pointer[T]":
        return Pointer(self._value)

    def __repr__(self) -> str:
        return f"Pointer({self._value})"


# Overrides the bitshift operator to create a pointer
class _Deref:
    def __and__(self, other: T) -> Pointer[T]:
        return Pointer(other)


class _Ref:
    def __mul__(self, other: Pointer[T]) -> T:
        return other.get()


o = _Ref()
_ = _Deref()

# Usage
# value = "Hello world"
# print(value, type(value))  # Hello world <class 'str'>
# ptr = _ & value
# print(ptr, type(ptr))  # Pointer(Hello world) <class 'utils.ptr.Pointer'>
# ptr("Nice day") # or ptr.set("Nice day")
# print(ptr, type(ptr))  # Pointer(Nice day) <class 'utils.ptr.Pointer'>
# value = o * ptr
# print(value, type(value))  # Nice day <class 'str'>
