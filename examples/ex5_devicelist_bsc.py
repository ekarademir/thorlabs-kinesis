"Sample code to receive list of devices."
from ctypes import (
    c_char_p,
)

from thorlabs_kinesis import benchtop_stepper_motor as bsm
from thorlabs_kinesis.ext import expand_device


if __name__ == "__main__":
    if bsm.TLI_BuildDeviceList() == 0:
        num_devs = int(bsm.TLI_GetDeviceListSize())
        print(f"There are {num_devs} devices.")

        receive_buffer = c_char_p(bytes(" " * 250, "utf-8"))
        buffer_size = bsm.c_dword(250)
        bsm.TLI_GetDeviceListExt(receive_buffer, buffer_size)

        serial_nos = receive_buffer.value.decode("utf-8").strip().split(',')

        for i, serial_no in enumerate(serial_nos):
            if len(serial_no) > 0:
                dev = expand_device(serial_no)
                print(f"{i + 1}. {serial_no} - {dev.type}")
