"Sample code for getting some parameters."
from ctypes import (
    c_short,
    c_int,
    c_char_p,
    byref,
)

from thorlabs_kinesis import benchtop_stepper_motor as bsm


if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)
    milliseconds = c_int(100)

    if bsm.SBC_Open(serial_no) == 0:
        bsm.SBC_StartPolling(serial_no, channel, milliseconds)
        bsm.SBC_ClearMessageQueue(serial_no, channel)

        acceleration = c_int(0)
        max_velocity = c_int(0)

        print("Requesting velocity params ",
              bsm.SBC_RequestVelParams(serial_no, channel) == 0)
        bsm.SBC_GetVelParams(serial_no, channel,
                             byref(acceleration),
                             byref(max_velocity))
        print("Acc: ", acceleration)
        print("Max Vel:", max_velocity)

        bsm.SBC_StopPolling(serial_no, channel)
        bsm.SBC_Close(serial_no)
