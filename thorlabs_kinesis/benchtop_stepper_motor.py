"Bindings for Thorlabs Benchtop Stepper Motor DLL"
from ctypes import (
    Structure,
    cdll,
    c_bool,
    c_short,
    c_int,
    c_uint,
    c_int16,
    c_char,
    c_byte,
    c_long,
    POINTER,
    CFUNCTYPE,
)

from thorlabs_kinesis._utils import (
    c_word,
    c_dword,
    bind
)

lib = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.StepperMotor.dll")


# enum FT_Status
FT_OK = c_short(0x00)
FT_InvalidHandle = c_short(0x01)
FT_DeviceNotFound = c_short(0x02)
FT_DeviceNotOpened = c_short(0x03)
FT_IOError = c_short(0x04)
FT_InsufficientResources = c_short(0x05)
FT_InvalidParameter = c_short(0x06)
FT_DeviceNotPresent = c_short(0x07)
FT_IncorrectDevice = c_short(0x08)
FT_Status = c_short

# enum MOT_MotorTypes
MOT_NotMotor = c_int(0)
MOT_DCMotor = c_int(1)
MOT_StepperMotor = c_int(2)
MOT_BrushlessMotor = c_int(3)
MOT_CustomMotor = c_int(100)
MOT_MotorTypes = c_int

# enum MOT_TravelModes
MOT_TravelModeUndefined = c_int(0x00)
MOT_Linear = c_int(0x01)
MOT_Rotational = c_int(0x02)
MOT_TravelModes = c_int

# enum MOT_TravelDirection
MOT_TravelDirectionUndefined = c_short(0x00)
MOT_Forwards = c_short(0x01)
MOT_Reverse = c_short(0x02)
MOT_TravelDirection = c_short

# enum MOT_HomeLimitSwitchDirection
MOT_LimitSwitchDirectionUndefined = c_short(0x00)
MOT_ReverseLimitSwitch = c_short(0x01)
MOT_ForwardLimitSwitch = c_short(0x04)
MOT_HomeLimitSwitchDirection = c_short

# enum MOT_DirectionSense
MOT_Normal = c_short(0x00)
MOT_Backwards = c_short(0x01)
MOT_DirectionSense = c_short

# enum MOT_JogModes
MOT_JogModeUndefined = c_short(0x00)
MOT_Continuous = c_short(0x01)
MOT_SingleStep = c_short(0x02)
MOT_JogModes = c_short

# enum MOT_StopModes
MOT_StopModeUndefined = c_short(0x00)
MOT_Immediate = c_short(0x01)
MOT_Profiled = c_short(0x02)
MOT_StopModes = c_short

# enum MOT_ButtonModes
MOT_ButtonModeUndefined = c_word(0x00)
MOT_JogMode = c_word(0x01)
MOT_Preset = c_word(0x02)
MOT_ButtonModes = c_word

# enum MOT_LimitSwitchModes
MOT_LimitSwitchModeUndefined = c_word(0x00)
MOT_LimitSwitchIgnoreSwitch = c_word(0x01)
MOT_LimitSwitchMakeOnContact = c_word(0x02)
MOT_LimitSwitchBreakOnContact = c_word(0x03)
MOT_LimitSwitchMakeOnHome = c_word(0x04)
MOT_LimitSwitchBreakOnHome = c_word(0x05)
MOT_PMD_Reserved = c_word(0x06)
MOT_LimitSwitchIgnoreSwitchSwapped = c_word(0x81)
MOT_LimitSwitchMakeOnContactSwapped = c_word(0x82)
MOT_LimitSwitchBreakOnContactSwapped = c_word(0x83)
MOT_LimitSwitchMakeOnHomeSwapped = c_word(0x84)
MOT_LimitSwitchBreakOnHomeSwapped = c_word(0x85)
MOT_LimitSwitchModes = c_word

# enum MOT_LimitSwitchSWModes
MOT_LimitSwitchSWModeUndefined = c_word(0x00)
MOT_LimitSwitchIgnored = c_word(0x01)
MOT_LimitSwitchStopImmediate = c_word(0x02)
MOT_LimitSwitchStopProfiled = c_word(0x03)
MOT_LimitSwitchIgnored_Rotational = c_word(0x81)
MOT_LimitSwitchStopImmediate_Rotational = c_word(0x82)
MOT_LimitSwitchStopProfiled_Rotational = c_word(0x83)
MOT_LimitSwitchSWModes = c_word

# enum MOT_LimitsSoftwareApproachPolicy
DisallowIllegalMoves = c_int16(0)
AllowPartialMoves = c_int16(1)
AllowAllMoves = c_int16(2)
MOT_LimitsSoftwareApproachPolicy = c_int16

# enum MOT_PID_LoopMode
MOT_PIDLoopModeDisabled = c_word(0x00)
MOT_PIDOpenLoopMode = c_word(0x01)
MOT_PIDClosedLoopMode = c_word(0x02)
MOT_PID_LoopMode = c_word

# enum MOT_MovementModes
LinearRange = c_int(0x00)
RotationalUnlimited = c_int(0x01)
RotationalWrapping = c_int(0x02)
MOT_MovementModes = c_int

# enum MOT_MovementDirections
Quickest = c_int(0x00)
Forwards = c_int(0x01)
Reverse = c_int(0x02)
MOT_MovementDirections = c_int


class TLI_DeviceInfo(Structure):
    _fields_ = [("typeID", c_dword),
                ("description", (65 * c_char)),
                ("serialNo", (9 * c_char)),
                ("PID", c_dword),
                ("isKnownType", c_bool),
                ("motorType", MOT_MotorTypes),
                ("isPiezoDevice", c_bool),
                ("isLaser", c_bool),
                ("isCustomType", c_bool),
                ("isRack", c_bool),
                ("maxChannels", c_short)]


class TLI_HardwareInformation(Structure):
    _fields_ = [("serialNumber", c_dword),
                ("modelNumber", (8 * c_char)),
                ("type", c_word),
                ("firmwareVersion", c_dword),
                ("notes", (48 * c_char)),
                ("deviceDependantData", (12 * c_byte)),
                ("hardwareVersion", c_word),
                ("modificationState", c_word),
                ("numChannels", c_short)]


class MOT_VelocityParameters(Structure):
    _fields_ = [("minVelocity", c_int),
                ("acceleration", c_int),
                ("maxVelocity", c_int)]


class MOT_JogParameters(Structure):
    _fields_ = [("mode", MOT_JogModes),
                ("stepSize", c_uint),
                ("velParams", MOT_VelocityParameters),
                ("stopMode", MOT_StopModes)]


class MOT_HomingParameters(Structure):
    _fields_ = [("direction", MOT_TravelDirection),
                ("limitSwitch", MOT_HomeLimitSwitchDirection),
                ("velocity", c_uint),
                ("offsetDistance", c_uint)]


class MOT_LimitSwitchParameters(Structure):
    _fields_ = [("clockwiseHardwareLimit", MOT_LimitSwitchModes),
                ("anticlockwiseHardwareLimit", MOT_LimitSwitchModes),
                ("clockwisePosition", c_dword),
                ("anticlockwisePosition", c_dword),
                ("softLimitMode", MOT_LimitSwitchSWModes)]


class MOT_PowerParameters(Structure):
    _fields_ = [("restPercentage", c_word),
                ("movePercentage", c_word)]


class MOT_JoystickParameters(Structure):
    _fields_ = [("lowGearMaxVelocity", c_dword),
                ("highGearMaxVelocity", c_dword),
                ("lowGearAcceleration", c_dword),
                ("highGearAcceleration", c_dword),
                ("directionSense", MOT_TravelDirection)]


class MOT_PIDLoopEncoderParams(Structure):
    _fields_ = [("loopMode", MOT_PID_LoopMode),
                ("proportionalGain", c_int),
                ("integralGain", c_int),
                ("differentialGain", c_int),
                ("PIDOutputLimit", c_int),
                ("PIDTolerance", c_int)]


TLI_BuildDeviceList = bind(lib, "TLI_BuildDeviceList", None, c_short)
TLI_GetDeviceListSize = bind(lib, "TLI_GetDeviceListSize", None, c_short)
# TLI_GetDeviceList  <- TODO: Implement SAFEARRAY first.
# TLI_GetDeviceListByType  <- TODO: Implement SAFEARRAY first.
# TLI_GetDeviceListByTypes  <- TODO: Implement SAFEARRAY first.
TLI_GetDeviceListExt = bind(lib, "TLI_GetDeviceListExt", [POINTER(c_char), c_dword], c_short)
TLI_GetDeviceListByTypeExt = bind(lib, "TLI_GetDeviceListByTypeExt", [POINTER(c_char), c_dword, c_int], c_short)
TLI_GetDeviceListByTypesExt = bind(lib, "TLI_GetDeviceListByTypesExt", [POINTER(c_char), c_dword, POINTER(c_int), c_int], c_short)
TLI_GetDeviceInfo = bind(lib, "TLI_GetDeviceInfo", [POINTER(c_char), POINTER(TLI_DeviceInfo)], c_short)

SBC_Open = bind(lib, "SBC_Open", [POINTER(c_char)], c_short)
SBC_Close = bind(lib, "SBC_Close", [POINTER(c_char)], c_short)
SBC_CheckConnection = bind(lib, "SBC_CheckConnection", [POINTER(c_char)], c_bool)
SBC_IsChannelValid = bind(lib, "SBC_IsChannelValid", [POINTER(c_char), c_short], c_bool)
SBC_MaxChannelCount = bind(lib, "SBC_MaxChannelCount", [POINTER(c_char), c_int])
SBC_Identify = bind(lib, "SBC_Identify", [POINTER(c_char), c_short])
SBC_GetHardwareInfo = bind(lib, "SBC_GetHardwareInfo", [POINTER(c_char), c_short, POINTER(c_char), c_dword, POINTER(c_word), POINTER(c_word), POINTER(c_char), c_dword, POINTER(c_dword), POINTER(c_word), POINTER(c_word)], c_short)
SBC_GetHardwareInfoBlock = bind(lib, "SBC_GetHardwareInfoBlock", [POINTER(c_char), c_short, POINTER(TLI_HardwareInformation)], c_short)
SBC_GetNumChannels = bind(lib, "SBC_GetNumChannels", [POINTER(c_char)], c_short)
SBC_GetFirmwareVersion = bind(lib, "SBC_GetFirmwareVersion", [POINTER(c_char), c_short], c_dword)
SBC_GetSoftwareVersion = bind(lib, "SBC_GetSoftwareVersion", [POINTER(c_char)])
SBC_LoadSettings = bind(lib, "SBC_LoadSettings", [POINTER(c_char), c_short], c_bool)
SBC_PersistSettings = bind(lib, "SBC_PersistSettings", [POINTER(c_char), c_short], c_bool)
SBC_SetCalibrationFile = bind(lib, "SBC_SetCalibrationFile", [POINTER(c_char), c_short, POINTER(c_char), c_bool])
SBC_IsCalibrationActive = bind(lib, "SBC_IsCalibrationActive", [POINTER(c_char), c_short], c_bool)
SBC_GetCalibrationFile = bind(lib, "SBC_GetCalibrationFile", [POINTER(c_char), c_short, POINTER(c_char), c_short], c_bool)
SBC_DisableChannel = bind(lib, "SBC_DisableChannel", [POINTER(c_char), c_short], c_short)
SBC_EnableChannel = bind(lib, "SBC_EnableChannel", [POINTER(c_char), c_short], c_short)
SBC_GetNumberPositions = bind(lib, "SBC_GetNumberPositions", [POINTER(c_char), c_short], c_int)
SBC_MoveToPosition = bind(lib, "SBC_MoveToPosition", [POINTER(c_char), c_short, c_int], c_short)
SBC_GetPosition = bind(lib, "SBC_GetPosition", [POINTER(c_char), c_short], c_int)
SBC_CanHome = bind(lib, "SBC_CanHome", [POINTER(c_char), c_short], c_bool)
SBC_NeedsHoming = bind(lib, "SBC_NeedsHoming", [POINTER(c_char), c_short], c_bool)
SBC_CanMoveWithoutHomingFirst = bind(lib, "SBC_CanMoveWithoutHomingFirst", [POINTER(c_char), c_short], c_bool)
SBC_Home = bind(lib, "SBC_Home", [POINTER(c_char), c_short, c_int], c_short)
SBC_ClearMessageQueue = bind(lib, "SBC_ClearMessageQueue", [POINTER(c_char), c_short, c_int], c_short)
SBC_RegisterMessageCallback = bind(lib, "SBC_RegisterMessageCallback", [POINTER(c_char), c_short, CFUNCTYPE(None, None)], c_short)
SBC_MessageQueueSize = bind(lib, "SBC_MessageQueueSize", [POINTER(c_char), c_short], c_int)
SBC_GetNextMessage = bind(lib, "SBC_GetNextMessage", [POINTER(c_char), c_short, POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
SBC_WaitForMessage = bind(lib, "SBC_WaitForMessage", [POINTER(c_char), c_short, POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
SBC_RequestHomingParams = bind(lib, "SBC_RequestHomingParams", [POINTER(c_char), c_short], c_short)
SBC_GetHomingVelocity = bind(lib, "SBC_GetHomingVelocity", [POINTER(c_char), c_short], c_uint)
SBC_SetHomingVelocity = bind(lib, "SBC_SetHomingVelocity", [POINTER(c_char), c_short, c_uint], c_short)
SBC_MoveRelative = bind(lib, "SBC_MoveRelative", [POINTER(c_char), c_short, c_int], c_short)
SBC_RequestJogParams = bind(lib, "SBC_RequestJogParams", [POINTER(c_char), c_short], c_short)
SBC_GetJogMode = bind(lib, "SBC_GetJogMode", [POINTER(c_char), c_short, POINTER(MOT_JogModes), POINTER(MOT_StopModes)], c_short)
SBC_SetJogMode = bind(lib, "SBC_SetJogMode", [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes], c_short)
SBC_GetJogStepSize = bind(lib, "SBC_GetJogStepSize", [POINTER(c_char), c_short], c_uint)
SBC_SetJogStepSize = bind(lib, "SBC_SetJogStepSize", [POINTER(c_char), c_short, c_uint], c_short)
SBC_GetJogVelParams = bind(lib, "SBC_GetJogVelParams", [POINTER(c_char), c_short, POINTER(c_int), POINTER(c_int)], c_short)
SBC_SetJogVelParams = bind(lib, "SBC_SetJogVelParams", [POINTER(c_char), c_short, c_int, c_int], c_short)
SBC_MoveJog = bind(lib, "SBC_MoveJog", [POINTER(c_char), c_short, MOT_TravelDirection], c_short)
SBC_RequestVelParams = bind(lib, "SBC_RequestVelParams", [POINTER(c_char), c_short], c_short)
SBC_GetVelParams = bind(lib, "SBC_GetVelParams", [POINTER(c_char), c_short, POINTER(c_int), POINTER(c_int)], c_short)
SBC_SetVelParams = bind(lib, "SBC_SetVelParams", [POINTER(c_char), c_short, c_int, c_int], c_short)
SBC_MoveAtVelocity = bind(lib, "SBC_MoveAtVelocity", [POINTER(c_char), c_short, MOT_TravelDirection], c_short)
SBC_SetDirection = bind(lib, "SBC_SetDirection", [POINTER(c_char), c_short, c_bool], c_short)
SBC_StopImmediate = bind(lib, "SBC_StopImmediate", [POINTER(c_char), c_short], c_short)
SBC_StopProfiled = bind(lib, "SBC_StopProfiled", [POINTER(c_char), c_short], c_short)
SBC_RequestBacklash = bind(lib, "SBC_RequestBacklash", [POINTER(c_char), c_short], c_short)
SBC_GetBacklash = bind(lib, "SBC_GetBacklash", [POINTER(c_char), c_short], c_long)
SBC_SetBacklash = bind(lib, "SBC_SetBacklash", [POINTER(c_char), c_short, c_long], c_short)
SBC_GetPositionCounter = bind(lib, "SBC_GetPositionCounter", [POINTER(c_char), c_short], c_long)
SBC_SetPositionCounter = bind(lib, "SBC_SetPositionCounter", [POINTER(c_char), c_short, c_long], c_short)

