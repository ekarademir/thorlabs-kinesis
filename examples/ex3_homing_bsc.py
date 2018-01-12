"Sample code for homing."
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
        if bsm.SBC_Open(serial_no) == 0:
            sleep(1.0)
            bsm.SBC_StartPolling(serial_no, channel, milliseconds)
            bsm.SBC_ClearMessageQueue(serial_no, channel)
            sleep(1.0)

            err = bsm.SBC_Home(serial_no, channel)
            sleep(1.0)
            if err == 0:
                while True:
                    current_pos = int(bsm.SBC_GetPosition(serial_no, channel))
                    if current_pos == 0:
                        print("At home.")
                        break
                    else:
                        print(f"Homing...{current_pos}")

                    sleep(1.0)
            else:
                print(f"Can't home. Err: {err}")

            bsm.SBC_StopPolling(serial_no, channel)
            bsm.SBC_Close(serial_no)
        else:
            print("Can't open")
    else:
        print("Can't build device list.")
