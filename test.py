import thorlabs_kinesis as tk

from ctypes import (
    c_short,
    c_char_p,
    byref,
)
# import sys
# sys.path.insert(0, "C:\\Program Files\\ThorLabs\\Kinesis")
# for p in sys.path:
#     print(p)

import os
os.environ['PATH'] = "C:\\Program Files\\ThorLabs\\Kinesis" + ";" + os.environ['PATH']
print(os.environ['PATH'])

from thorlabs_kinesis import kcube_dcservo as kcdc


kcdc.CC_Open(c_char_p(bytes("27504851", "utf-8")))
kcdc.CC_CanHome(c_char_p(bytes("27504851", "utf-8")))
print(int(kcdc.CC_GetJogVelParams(c_char_p(bytes("27504851", "utf-8")))))
print(int(kcdc.CC_GetPosition(c_char_p(bytes("27504851", "utf-8")))))
#kcdc.CC_Home(c_char_p(bytes("27504851", "utf-8")))