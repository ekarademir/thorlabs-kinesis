"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)
import sys 


from thorlabs_kinesis import KCube_DC_Servo as kdc


if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))

    if kdc.CC_Open(serial_no) == 0:

        hw_info = kdc.TLI_HardwareInformation()  # container for hw info
        err = kdc.CC_GetHardwareInfoBlock(serial_no, byref(hw_info))
        if err == 0:
            print("Serial No: ", hw_info.serialNumber)
            print("Model No: ", hw_info.modelNumber)
            print("Firmware Version: ", hw_info.firmwareVersion)
            print("Number of  Channels: ", hw_info.numChannels)
            print("Type: ", hw_info.type)
        else:
            print(f"Error getting HW Info Block. Error Code: {err}")

        kdc.CC_Close(serial_no)
