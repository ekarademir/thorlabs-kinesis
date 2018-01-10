"Sample code to get information about connected controllers."
from ctypes import (
    c_short,
    c_int,
    c_char_p,
    byref,
)
from time import sleep

from thorlabs_kinesis import benchtop_stepper_motor as bsm


if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)
    milliseconds = c_int(100)

    if bsm.SBC_Open(serial_no) == 0:
        bsm.SBC_StartPolling(serial_no, channel, milliseconds)
        bsm.SBC_ClearMessageQueue(serial_no, channel)

        if bsm.SBC_Home(serial_no, channel) == 0:
            while True:
                current_pos = int(bsm.SBC_GetPosition(serial_no, channel))
                if current_pos == 0:
                    print("At home.")
                    break
                else:
                    print(f"Homing...{current_pos}")

                sleep(0.2)

        bsm.SBC_StopPolling(serial_no, channel)
        bsm.SBC_Close(serial_no)
