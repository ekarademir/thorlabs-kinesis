"Utility functions."
from ctypes import (
    CDLL,
    CFUNCTYPE,
    c_ushort,
    c_ulong,
)
from typing import (
    Any,
    List,
)

c_word = c_ushort
c_dword = c_ulong


def bind(lib: CDLL, func: str,
         argtypes: List[Any]=None, restype: Any=None) -> CFUNCTYPE:
    _func = getattr(lib, func, null_function)
    _func.argtypes = argtypes
    _func.restype = restype

    return _func


def null_function():
    pass


__all__ = [
    bind,
    null_function,
    c_word,
    c_dword,
]
