"Sample code to get hardware information."
from ctypes import (
    c_short,
    c_char_p,
    byref,
)

from thorlabs_kinesis import benchtop_stepper_motor as bsm
if __name__ == "__main__":
    serial_no = c_char_p(bytes("40875459", "utf-8"))
    channel = c_short(1)

    if bsm.TLI_BuildDeviceList() == 0:
        if bsm.SBC_Open(serial_no, channel) == 0:
            homing_inf = bsm.MOT_HomingParameters()  # container

            print("Setting homing vel ", bsm.SBC_SetHomingVelocity(serial_no, channel, bsm.c_uint(10000)))

            bsm.SBC_RequestHomingParams(serial_no, channel)
            err = bsm.SBC_GetHomingParamsBlock(serial_no, channel, byref(homing_inf))
            if err == 0:
                print("Direction: ", homing_inf.direction)
                print("Limit Sw: ", homing_inf.limitSwitch)
                print("Velocity: ", homing_inf.velocity)
                print("Offset Dist: ", homing_inf.offsetDistance)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")

            power_inf = bsm.MOT_PowerParameters()  # container

            bsm.SBC_RequestPowerParams(serial_no, channel)
            err = bsm.SBC_GetPowerParams(serial_no, channel, byref(power_inf))
            if err == 0:
                print("Rest percentage: ", power_inf.restPercentage)
                print("Move percentage: ", power_inf.movePercentage)

            else:
                print(f"Error getting Homing Info Block. Error Code: {err}")

            bsm.SBC_Close(serial_no, channel)
        else:
            print("Can't open connection.")
    else:
        print("Can't build device list")
