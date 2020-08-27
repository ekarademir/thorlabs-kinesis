"Sample code for move absolute."
from ctypes import (
    c_short,
    c_int,
    c_char_p,
)
from time import sleep
import sys 

from thorlabs_kinesis import KCube_DC_Servo as kdc


if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))
    milliseconds = c_int(100)

    if kdc.TLI_BuildDeviceList() == 0:
        err = kdc.CC_Open(serial_no)
        if err == 0:
            print("Starting polling ", kdc.CC_StartPolling(serial_no, milliseconds))
            print("Clearing message queue ", kdc.CC_ClearMessageQueue(serial_no))
            sleep(0.2)

            #move_to = 400000
            move_to = 123456
            print("Setting Absolute Position ", kdc.CC_SetMoveAbsolutePosition(serial_no, c_int(move_to)))
            sleep(0.2)

            print(f"Moving to {move_to}", kdc.CC_MoveAbsolute(serial_no))
            sleep(0.2)
            pos = int(kdc.CC_GetPosition(serial_no))
            sleep(0.2)
            print(f"Current pos: {pos}")
            while not pos == move_to:
                sleep(0.2)
                pos = int(kdc.CC_GetPosition(serial_no))
                print(f"Current pos: {pos}")

            print("Stopping polling ", kdc.CC_StopPolling(serial_no))
            print("Closing connection ", kdc.CC_Close(serial_no))
        else:
            print(f"Can't open. Error: {err}")
