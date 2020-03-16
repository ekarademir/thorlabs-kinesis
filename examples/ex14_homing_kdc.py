"Sample code for homing."
from ctypes import (
    c_short,
    c_int,
    c_char_p,
)
from time import sleep
import sys 
for path in ["C:\\Users\\Mikroskop Admin\\Documents\\transfersystem_i2a\\thorlabs-kinesis"]:
    if path not in sys.path:
        sys.path.append(path)
from thorlabs_kinesis import KCube_DC_Servo as kdc


if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))
    milliseconds = c_int(100)

    if kdc.TLI_BuildDeviceList() == 0:
        if kdc.CC_Open(serial_no) == 0:
            sleep(1.0)
            kdc.CC_StartPolling(serial_no, milliseconds)
            kdc.CC_ClearMessageQueue(serial_no)
            sleep(1.0)

            err = kdc.CC_Home(serial_no)
            sleep(1.0)
            if err == 0:
                while True:
                    current_pos = int(kdc.CC_GetPosition(serial_no))
                    if current_pos == 0:
                        print("At home.")
                        break
                    else:
                        print(f"Homing...{current_pos}")

                    sleep(1.0)
            else:
                print(f"Can't home. Err: {err}")

            kdc.CC_StopPolling(serial_no)
            kdc.CC_Close(serial_no)
        else:
            print("Can't open")
    else:
        print("Can't build device list.")
