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
from thorlabs_kinesis import integrated_stepper_motors as ism
if __name__ == "__main__":
    serial_no = c_char_p(bytes("45875474", "utf-8"))
    channel = c_short(1)

    if ism.TLI_BuildDeviceList() == 0:
        if ism.ISC_Open(serial_no) == 0:
            homing_inf = ism.MOT_HomingParameters()  # container

            print("Setting homing vel ", ism.ISC_SetHomingVelocity(serial_no, ism.c_uint(100)))

            ism.ISC_RequestHomingParams(serial_no)
            err = ism.ISC_GetHomingParamsBlock(serial_no, byref(homing_inf))
            if err == 0:
                print("Direction: ", homing_inf.direction)
                print("Limit Sw: ", homing_inf.limitSwitch)
                print("Velocity: ", homing_inf.velocity)
                print("Offset Dist: ", homing_inf.offsetDistance)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")

            power_inf = ism.MOT_PowerParameters()  # container

            ism.ISC_RequestPowerParams(serial_no)
            err = ism.ISC_GetPowerParams(serial_no, byref(power_inf))
            if err == 0:
                print("Rest percentage: ", power_inf.restPercentage)
                print("Move percentage: ", power_inf.movePercentage)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")

            ism.ISC_Close(serial_no)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
