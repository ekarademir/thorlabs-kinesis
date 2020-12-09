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
                ("uci", UC480_CAMERA_INFO * 1)]

GetNumberOfCameras = bind(lib, "is_GetNumberOfCameras", [POINTER(c_int)], c_int)
GetCameraList = bind(lib, "is_GetCameraList", [POINTER(UC480_CAMERA_LIST)], c_int)

InitCamera = bind(lib, "is_InitCamera", [POINTER(c_int), POINTER(c_int)], c_int)
SetDisplayMode = bind(lib, "is_SetDisplayMode", [POINTER(c_int), c_int], c_int)
PixelClock = bind(lib, "is_PixelClock", [POINTER(c_int), c_int, POINTER(c_uint), c_uint], c_int)
SetColorMode = bind(lib, "is_SetColorMode", [POINTER(c_int), c_int], c_int)
SetExposure = bind(lib, "is_Exposure", [POITNER(c_int), 12, POITNER(c_double), c_uint], c_int)
SetFrameRate = bind(lib, "is_SetFrameRate", [POITNER(c_int), c_double, POINTER(c_double)])

FreeMemory = bind(lib, "is_FreeImageMem", [POITNER(c_int), POINTER(c_char), c_int], c_int)
AllocateMemory = bind(lib, "is_SetAllocatedImageMem", [POINTER(c_int), c_int, c_int, c_int, POINTER(c_char), POITNER(c_int)], c_int)
SetImageMemory = bind(lib, "is_SetImageMem", [POINTER(c_int), POITNER(c_char), c_int], c_int)

StartCapture = bind(lib, "is_CaptureVideo", [POINTER(c_int), c_int], c_int)
StopCapture = bind(lib, "is_StopLiveVideo", [POITNER(c_int), c_int], c_int)

ExitCamera = bind(lib, "is_ExitCamera", [POITNER(c_int)], c_int)