"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)

from time import sleep

import sys 


from thorlabs_kinesis import KCube_DC_Servo as kdc
if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))

    if kdc.TLI_BuildDeviceList() == 0:
        if kdc.CC_Open(serial_no) == 0:
            acc = kdc.c_int()  # containers
            max_vel = kdc.c_int()

            kdc.CC_RequestVelParams(serial_no)
            sleep(0.2)
            err = kdc.CC_GetVelParams(serial_no, byref(acc), byref(max_vel))
            if err == 0:
                print("Acceleration: ", acc)
                print("Max Velocity: ", max_vel)

            else:
                print(f"Error getting velocity info. Error Code: {err}")

            move_to = 123456
            err = kdc.CC_MoveToPosition(serial_no, kdc.c_int(move_to))
            sleep(0.2)
            if err == 0:
                kdc.CC_RequestPosition(serial_no)
                sleep(0.2)
                pos = int(kdc.CC_GetPosition(serial_no))
                while not pos == move_to:
                    print(f"Current pos {pos} moving to {move_to}")
                    kdc.CC_RequestPosition(serial_no)
                    sleep(0.2)
                    pos = int(kdc.CC_GetPosition(serial_no))
                    sleep(0.2)

            kdc.CC_Close(serial_no)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
