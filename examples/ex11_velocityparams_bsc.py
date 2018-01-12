"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)

from time import sleep

from thorlabs_kinesis import benchtop_stepper_motor as bsm
if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)

    if bsm.TLI_BuildDeviceList() == 0:
        if bsm.SBC_Open(serial_no, channel) == 0:
            acc = bsm.c_int()  # containers
            max_vel = bsm.c_int()

            bsm.SBC_RequestVelParams(serial_no, channel)
            sleep(0.2)
            err = bsm.SBC_GetVelParams(serial_no, channel, byref(acc), byref(max_vel))
            if err == 0:
                print("Acceleration: ", acc)
                print("Max Velocity: ", max_vel)

            else:
                print(f"Error getting velocity info. Error Code: {err}")

            move_to = 0
            err = bsm.SBC_MoveToPosition(serial_no, channel, bsm.c_int(move_to))
            sleep(0.2)
            if err == 0:
                bsm.SBC_RequestPosition(serial_no, channel)
                sleep(0.2)
                pos = int(bsm.SBC_GetPosition(serial_no, channel))
                while not pos == move_to:
                    print(f"Current pos {pos} moving to {move_to}")
                    bsm.SBC_RequestPosition(serial_no, channel)
                    sleep(0.2)
                    pos = int(bsm.SBC_GetPosition(serial_no, channel))
                    sleep(0.2)

            bsm.SBC_Close(serial_no, channel)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
