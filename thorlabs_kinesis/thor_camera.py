import numpy as np
import time

import thorlabs_kinesis as tk

from ctypes import *

from thorlabs_kinesis._utils import (
    c_word,
    c_dword,
    bind
)

lib = cdll.LoadLibrary("uc480_64.dll")

class UC480_CAMERA_INFO(Structure):
    _fields_ = [("dwCameraID", c_dword),
                ("dwDeviceID", c_dword),
                ("dwSensorID", c_dword),
                ("dwInUse", c_dword),
                ("SerNo", c_char * 16),
                ("Model", c_char * 16),
                ("dwStatus", c_dword),
                ("dwReserved", c_dword * 15)]

class UC480_CAMERA_LIST(Structure):
    _fields_ = [("dwCount", c_int),
                ("uci", UC480_CAMERA_INFO)]

class CAMINFO(Structure):
    _fields_ = [("SerNo", c_char * 12),
                ("ID", c_char * 20),
                ("Version", c_char * 10),
                ("Date", c_char * 12),
                ("Select", c_char),
                ("Type", c_char)]

class IS_2D(Structure):
    _fields_ = [('s32X', c_int), ('s32Y', c_int)]

GetNumberOfCameras = bind(lib, "is_GetNumberOfCameras", [POINTER(c_int)], c_int)
GetCameraList = bind(lib, "is_GetCameraList", [POINTER(c_byte * 16)], c_int)
GetCameraInfo = bind(lib, "is_GetCameraInfo", [c_int, POINTER(CAMINFO)], c_int)

InitCamera = bind(lib, "is_InitCamera", [POINTER(c_int)], c_int)
SetDisplayMode = bind(lib, "is_SetDisplayMode", [POINTER(c_int), c_int], c_int)
PixelClock = bind(lib, "is_PixelClock", [c_int, c_uint, POINTER(c_uint), c_uint], c_int)
SetColorMode = bind(lib, "is_SetColorMode", [c_int, c_int], c_int)
SetExposure = bind(lib, "is_Exposure", [c_int, c_uint, POINTER(c_double), c_uint], c_int)
SetFrameRate = bind(lib, "is_SetFrameRate", [c_int, c_double, POINTER(c_double)])
AOI = bind(lib, "is_AOI", [c_int, c_uint, POINTER(IS_2D), c_uint], c_int)

FreeMemory = bind(lib, "is_FreeImageMem", [c_int, POINTER(c_ubyte * 1310720), c_int], c_int)
AllocateMemory = bind(lib, "is_SetAllocatedImageMem", [c_int, c_int, c_int, c_int, c_ubyte * 1310720, POINTER(c_int)], c_int)
SetImageMemory = bind(lib, "is_SetImageMem", [c_int, c_ubyte * 1310720, c_int], c_int)

StartCapture = bind(lib, "is_CaptureVideo", [c_int, c_int], c_int)
StopCapture = bind(lib, "is_StopLiveVideo", [c_int, c_int], c_int)

ExitCamera = bind(lib, "is_ExitCamera", [c_int], c_int)