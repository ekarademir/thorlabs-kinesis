
import thorlabs_kinesis as tk

from ctypes import (
    Structure,
    cdll,
    c_bool,
    c_short,
    c_int,
    c_uint,
    c_int16,
    c_int32,
    c_char,
    c_byte,
    c_long,
    c_float,
    c_double,
    POINTER,
    CFUNCTYPE,
)

from thorlabs_kinesis._utils import (
    c_word,
    c_dword,
    bind
)

lib = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.DCServo.dll")
CC_Close = bind(lib, "CC_Close", [POINTER(c_char)], None)
CC_CanHome = bind(lib, "CC_Open", [POINTER(c_char)], c_bool)
CC_Open = bind(lib, "CC_Open", [POINTER(c_char)], c_short)
CC_GetJogVelParams = bind(lib, "CC_GetJogVelParams", [POINTER(c_char)], c_short)
CC_Home = bind(lib, "CC_Home", [POINTER(c_char)], c_short)
#KVS_GetPosition = bind(lib, "KVS_GetPosition", [POINTER(c_char)], c_int)
CC_GetPosition  = bind(lib, "CC_GetPosition", [POINTER(c_char)], c_int)