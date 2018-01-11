"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)

from thorlabs_kinesis import integrated_stepper_motors as ism
if __name__ == "__main__":
    serial_no = c_char_p(bytes("45875474", "utf-8"))
    channel = c_short(1)

    if ism.TLI_BuildDeviceList() == 0:
        if ism.ISC_Open(serial_no) == 0:
            hw_info = ism.TLI_HardwareInformation()  # container for hw info
            err = ism.ISC_GetHardwareInfoBlock(serial_no, byref(hw_info))
            if err == 0:
                print("Serial No: ", hw_info.serialNumber)
                print("Model No: ", hw_info.modelNumber)
                print("Firmware Version: ", hw_info.firmwareVersion)
                print("Number of  Channels: ", hw_info.numChannels)
                print("Type: ", hw_info.type)
            else:
                print(f"Error getting HW Info Block. Error Code: {err}")

            ism.ISC_Close(serial_no)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
