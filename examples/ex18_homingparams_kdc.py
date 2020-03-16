"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)
import sys 
for path in ["C:\\Users\\Mikroskop Admin\\Documents\\transfersystem_i2a\\thorlabs-kinesis"]:
    if path not in sys.path:
        sys.path.append(path)

from thorlabs_kinesis import KCube_DC_Servo as kdc
if __name__ == "__main__":
    serial_no = c_char_p(bytes("27254142", "utf-8"))

    if kdc.TLI_BuildDeviceList() == 0:
        if kdc.CC_Open(serial_no) == 0:
            homing_inf = kdc.MOT_HomingParameters()  # container

            print("Setting homing vel ", kdc.CC_SetHomingVelocity(serial_no, kdc.c_uint(10000)))

            kdc.CC_RequestHomingParams(serial_no)
            err = kdc.CC_GetHomingParamsBlock(serial_no, byref(homing_inf))
            if err == 0:
                print("Direction: ", homing_inf.direction)
                print("Limit Sw: ", homing_inf.limitSwitch)
                print("Velocity: ", homing_inf.velocity)
                print("Offset Dist: ", homing_inf.offsetDistance)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")

            '''
            power_inf = kdc.MOT_PowerParameters()  # container

            kdc.CC_RequestPowerParams(serial_no)
            err = kdc.CC_GetPowerParams(serial_no, byref(power_inf))
            if err == 0:
                print("Rest percentage: ", power_inf.restPercentage)
                print("Move percentage: ", power_inf.movePercentage)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")
            '''
            kdc.CC_Close(serial_no)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
