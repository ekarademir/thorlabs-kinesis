"Sample code for move absolute."
from ctypes import (
    c_short,
    c_int,
    c_char_p,
)
from time import sleep

from thorlabs_kinesis import benchtop_stepper_motor as bsm


if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)
    milliseconds = c_int(100)

    if bsm.TLI_BuildDeviceList() == 0:
        err = bsm.SBC_Open(serial_no, channel)
        if err == 0:
            print("Starting polling ", bsm.SBC_StartPolling(serial_no, channel, milliseconds))
            print("Clearing message queue ", bsm.SBC_ClearMessageQueue(serial_no, channel))
            sleep(0.2)

            move_to = 1000000
            print("Setting Absolute Position ", bsm.SBC_SetMoveAbsolutePosition(serial_no, channel, c_int(move_to)))
            sleep(0.2)

            print(f"Moving to {move_to}", bsm.SBC_MoveAbsolute(serial_no, channel))
            sleep(0.2)
            pos = int(bsm.SBC_GetPosition(serial_no, channel))
            sleep(0.2)
            print(f"Current pos: {pos}")
            while not pos == move_to:
                sleep(0.2)
                pos = int(bsm.SBC_GetPosition(serial_no, channel))
                print(f"Current pos: {pos}")

            print("Stopping polling ", bsm.SBC_StopPolling(serial_no, channel))
            print("Closing connection ", bsm.SBC_Close(serial_no, channel))
        else:
            print(f"Can't open. Error: {err}")
