"Sample code for getting some parameters."
from ctypes import (
    c_int,
    c_char_p,
    byref,
)
import sys 


from thorlabs_kinesis import KCube_DC_Servo as kdc


if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))
    milliseconds = c_int(100)

    if kdc.CC_Open(serial_no) == 0:
        kdc.CC_StartPolling(serial_no, milliseconds)
        kdc.CC_ClearMessageQueue(serial_no)

        acceleration = c_int(0)
        max_velocity = c_int(0)

        print("Requesting velocity params ",
              kdc.CC_RequestVelParams(serial_no) == 0)
        kdc.CC_GetVelParams(serial_no,
                             byref(acceleration),
                             byref(max_velocity))
        print("Acc: ", acceleration)
        print("Max Vel:", max_velocity)

        kdc.CC_StopPolling(serial_no)
        kdc.CC_Close(serial_no)
