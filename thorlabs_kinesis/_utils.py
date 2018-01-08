"Utility functions."
from ctypes import (
    CDLL,
    c_uint16,
    c_uint32,
    c_int32,
)
from typing import (Any)

c_word = c_uint16
c_dword = c_uint32
c_long = c_int32


def bind(lib: CDLL, func: str, args: Any=None, returns: Any=None)->None:
    _func = getattr(lib, func, null_function)

    return _func


def null_function():
    pass


__all__ = [
    bind,
    null_function,
    c_word,
    c_dword,
    c_long,
]
