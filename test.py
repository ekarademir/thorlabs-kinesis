import thorlabs_kinesis as tk
import time
from ctypes import (
    c_short,
    c_char_p,
    byref,
    c_int,
)
# import sys
# sys.path.insert(0, "C:\\Program Files\\ThorLabs\\Kinesis")
# for p in sys.path:
#     print(p)

import os
os.environ['PATH'] = "C:\\Program Files\\ThorLabs\\Kinesis" + ";" + os.environ['PATH']
#print(os.environ['PATH'])

from thorlabs_kinesis import kcube_dcservo as kcdc

serialno = c_char_p(bytes("27504851", "utf-8"))

kcdc.CC_Open(serialno)
kcdc.CC_StartPolling(serialno,c_int(200))
kcdc.CC_ClearMessageQueue(serialno)
time.sleep(3)
# kcdc.CC_CanHome(c_char_p(bytes("27504851", "utf-8")))
print(int(kcdc.CC_GetJogVelParams(serialno)))
print(int(kcdc.CC_GetPosition(serialno)))
kcdc.CC_Home(serialno)
