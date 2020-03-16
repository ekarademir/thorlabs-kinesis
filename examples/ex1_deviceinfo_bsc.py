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

from thorlabs_kinesis import benchtop_stepper_motor as bsm


if __name__ == "__main__":
    if bsm.TLI_BuildDeviceList() == 0:
        serial_no = c_char_p(bytes("27254142", "utf-8"))

        device_info = bsm.TLI_DeviceInfo()  # container for device info
        bsm.TLI_GetDeviceInfo(serial_no, byref(device_info))

        print("Description: ", device_info.description)
        print("Serial No: ", device_info.serialNo)
        print("Motor Type: ", device_info.motorType)
        print("USB PID: ", device_info.PID)
        print("Max Number of  Channels: ", device_info.maxChannels)
