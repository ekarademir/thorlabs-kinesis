# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:27:37 2020

@author: David Tebbe
"""

"Sample code to get information about connected controllers."
from ctypes import (
    c_char_p,
    byref,
)

import sys 
for path in ["C:\\Users\\Mikroskop Admin\\Documents\\transfersystem_i2a\\thorlabs-kinesis"]:
    #print(sys.path)
    if path not in sys.path:
        sys.path.append(path)

from thorlabs_kinesis import KCube_DC_Servo as kdc


if __name__ == "__main__":
    if kdc.TLI_BuildDeviceList() == 0:
        serial_no = c_char_p(bytes("27254142", "utf-8"))

        device_info = kdc.TLI_DeviceInfo()  # container for device info
        kdc.TLI_GetDeviceInfo(serial_no, byref(device_info))

        print("Description: ", device_info.description)
        print("Serial No: ", device_info.serialNo)
        print("Motor Type: ", device_info.motorType)
        print("USB PID: ", device_info.PID)
        print("Max Number of  Channels: ", device_info.maxChannels)
