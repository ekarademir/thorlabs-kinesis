"Sample code for absolute movement."
from ctypes import (
    c_int,
    c_char_p,
)
import sys 
for path in ["C:\\Users\\Mikroskop Admin\\Documents\\transfersystem_i2a\\thorlabs-kinesis"]:
    if path not in sys.path:
        sys.path.append(path)
from time import sleep

from thorlabs_kinesis import integrated_stepper_motors as ism


if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))
    milliseconds = c_int(100)

    if ism.TLI_BuildDeviceList() == 0:
        err = ism.ISC_Open(serial_no)
        if err == 0:
            print("Starting polling ", ism.ISC_StartPolling(serial_no, milliseconds))
            print("Clearing message queue ", ism.ISC_ClearMessageQueue(serial_no))
            sleep(0.2)

            move_to = 1000000
            print("Setting Absolute Position ", ism.ISC_SetMoveAbsolutePosition(serial_no, c_int(move_to)))
            sleep(0.2)

            print(f"Moving to {move_to}", ism.ISC_MoveAbsolute(serial_no))
            sleep(0.2)
            pos = int(ism.ISC_GetPosition(serial_no))
            sleep(0.2)
            print(f"Current pos: {pos}")
            while not pos == move_to:
                sleep(0.2)
                pos = int(ism.ISC_GetPosition(serial_no))
                print(f"Current pos: {pos}")

            print("Stopping polling ", ism.ISC_StopPolling(serial_no))
            print("Closing connection ", ism.ISC_Close(serial_no))
        else:
            print(f"Can't open. Error: {err}")
