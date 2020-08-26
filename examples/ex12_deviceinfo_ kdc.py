"Sample code to get information about connected controllers."
from ctypes import (
    c_char_p,
    byref,
)

import sys 

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
