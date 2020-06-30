import os
os.environ['PATH'] = "C:\\Program Files\\ThorLabs\\Kinesis" + ";" + os.environ['PATH']
#print(os.environ['PATH'])

import thorlabs_kinesis as tk
import time
from ctypes import (
    c_short,
    c_char_p,
    byref,
    c_int,
    create_string_buffer,
)
from ctypes.wintypes import (
    DWORD,
)

from thorlabs_kinesis import kcube_dcservo as kcdc

if kcdc.TLI_BuildDeviceList() == 0:
    print("Device list built (no errors).")

    size = kcdc.TLI_GetDeviceListSize()
    print(size, "device(s) found.")

    serialnos = create_string_buffer(100)
    kcdc.TLI_GetDeviceListByTypeExt(serialnos, 100, 27)
    serialnos = list(filter(None, serialnos.value.decode("utf-8").split(',')))
    print("Serial #'s:", serialnos)

    # serialno = c_char_p(bytes("27504851", "utf-8"))

    # kcdc.CC_Open(serialno)
    # kcdc.CC_StartPolling(serialno, c_int(200))
    # kcdc.CC_ClearMessageQueue(serialno)
    # # time.sleep(3)
    # # homeable = bool(kcdc.CC_CanHome(serialno))
    # # print(homeable)
    # # print(int(kcdc.CC_GetJogVelParams(serialno)))
    # # print(int(kcdc.CC_GetPosition(serialno)))
    # # kcdc.CC_Home(serialno)
    # kcdc.CC_StopPolling(serialno)
    # kcdc.CC_Close(serialno)
