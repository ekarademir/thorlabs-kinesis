"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)

from thorlabs_kinesis import benchtop_stepper_motor as bsm


if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)

    if bsm.SBC_Open(serial_no) == 0:
        print("Is channel valid ", bsm.SBC_IsChannelValid(serial_no, channel))

        hw_info = bsm.TLI_HardwareInformation()  # container for hw info
        err = bsm.SBC_GetHardwareInfoBlock(serial_no, channel, byref(hw_info))
        if err == 0:
            print("Serial No: ", hw_info.serialNumber)
            print("Model No: ", hw_info.modelNumber)
            print("Firmware Version: ", hw_info.firmwareVersion)
            print("Number of  Channels: ", hw_info.numChannels)
            print("Type: ", hw_info.type)
        else:
            print(f"Error getting HW Info Block. Error Code: {err}")

        bsm.SBC_Close(serial_no)
