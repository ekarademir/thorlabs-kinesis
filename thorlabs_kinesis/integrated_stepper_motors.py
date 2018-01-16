"Bindings for Thorlabs Integrated Stepper Motor DLL"
# flake8: noqa
from ctypes import (
    Structure,
    cdll,
    c_bool,
    c_short,
    c_int,
    c_uint,
    c_int16,
    c_int32,
    c_char,
    c_byte,
    c_long,
    c_float,
    c_double,
    POINTER,
    CFUNCTYPE,
)

from thorlabs_kinesis._utils import (
    c_word,
    c_dword,
    bind
)

lib = cdll.LoadLibrary("Thorlabs.MotionControl.IntegratedStepperMotors.dll")


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


class MOT_ButtonParameters(Structure):
    _fields_ = [("buttonMode", MOT_ButtonModes),
                ("leftButtonPosition", c_int),
                ("rightButtonPosition", c_int),
                ("timeout", c_word),
                ("unused", c_word)]


class MOT_PotentiometerStep(Structure):
    _fields_ = [("thresholdDeflection", c_word),
                ("velocity", c_dword)]


class MOT_PotentiometerSteps(Structure):
    _fields_ = [("potentiometerStepParameters", (4 * MOT_PotentiometerStep))]


TLI_BuildDeviceList = bind(lib, "TLI_BuildDeviceList", None, c_short)
TLI_GetDeviceListSize = bind(lib, "TLI_GetDeviceListSize", None, c_short)
# TLI_GetDeviceList  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceList(SAFEARRAY** stringsReceiver);
# TLI_GetDeviceListByType  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceListByType(SAFEARRAY** stringsReceiver, int typeID);
# TLI_GetDeviceListByTypes  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceListByTypes(SAFEARRAY** stringsReceiver, int * typeIDs, int length);
TLI_GetDeviceListExt = bind(lib, "TLI_GetDeviceListExt", [POINTER(c_char), c_dword], c_short)
TLI_GetDeviceListByTypeExt = bind(lib, "TLI_GetDeviceListByTypeExt", [POINTER(c_char), c_dword, c_int], c_short)
TLI_GetDeviceListByTypesExt = bind(lib, "TLI_GetDeviceListByTypesExt", [POINTER(c_char), c_dword, POINTER(c_int), c_int], c_short)
TLI_GetDeviceInfo = bind(lib, "TLI_GetDeviceInfo", [POINTER(c_char), POINTER(TLI_DeviceInfo)], c_short)

ISC_Open = bind(lib, "ISC_Open", [POINTER(c_char)], c_short)
ISC_Close = bind(lib, "ISC_Close", [POINTER(c_char)])
ISC_CheckConnection = bind(lib, "ISC_CheckConnection", [POINTER(c_char)], c_bool)
ISC_Identify = bind(lib, "ISC_Identify", [POINTER(c_char)])
ISC_GetLEDswitches = bind(lib, "ISC_GetLEDswitches", [POINTER(c_char)], c_word)
ISC_SetLEDswitches = bind(lib, "ISC_SetLEDswitches", [POINTER(c_char), c_word], c_short)
ISC_GetHardwareInfo = bind(lib, "ISC_GetHardwareInfo", [POINTER(c_char), POINTER(c_char), c_dword, POINTER(c_word), POINTER(c_word), POINTER(c_char), c_dword, POINTER(c_dword), POINTER(c_word), POINTER(c_word)], c_short)
ISC_GetHardwareInfoBlock = bind(lib, "ISC_GetHardwareInfoBlock", [POINTER(c_char), POINTER(TLI_HardwareInformation)], c_short)
ISC_GetFirmwareVersion = bind(lib, "ISC_GetFirmwareVersion", [POINTER(c_char)], c_dword)
ISC_GetSoftwareVersion = bind(lib, "ISC_GetSoftwareVersion", [POINTER(c_char)], c_dword)
ISC_SetCalibrationFile = bind(lib, "ISC_SetCalibrationFile", [POINTER(c_char), POINTER(c_char), c_bool])
ISC_IsCalibrationActive = bind(lib, "ISC_IsCalibrationActive", [POINTER(c_char)], c_bool)
ISC_GetCalibrationFile = bind(lib, "ISC_GetCalibrationFile", [POINTER(c_char), POINTER(c_char), c_short], c_bool)
ISC_LoadSettings = bind(lib, "ISC_LoadSettings", [POINTER(c_char)], c_bool)
ISC_PersistSettings = bind(lib, "ISC_PersistSettings", [POINTER(c_char)], c_bool)
ISC_ResetStageToDefaults = bind(lib, "ISC_ResetStageToDefaults", [POINTER(c_char)], c_short)
ISC_DisableChannel = bind(lib, "ISC_DisableChannel", [POINTER(c_char)], c_short)
ISC_EnableChannel = bind(lib, "ISC_EnableChannel", [POINTER(c_char)], c_short)
ISC_GetNumberPositions = bind(lib, "ISC_GetNumberPositions", [POINTER(c_char)], c_int)
ISC_MoveToPosition = bind(lib, "ISC_MoveToPosition", [POINTER(c_char), c_int], c_short)
ISC_GetPosition = bind(lib, "ISC_GetPosition", [POINTER(c_char)], c_int)
ISC_CanHome = bind(lib, "ISC_CanHome", [POINTER(c_char)], c_bool)
ISC_NeedsHoming = bind(lib, "ISC_NeedsHoming", [POINTER(c_char)], c_bool)
ISC_CanMoveWithoutHomingFirst = bind(lib, "ISC_CanMoveWithoutHomingFirst", [POINTER(c_char)], c_bool)
ISC_Home = bind(lib, "ISC_Home", [POINTER(c_char)], c_short)
ISC_ClearMessageQueue = bind(lib, "ISC_ClearMessageQueue", [POINTER(c_char)])
ISC_RegisterMessageCallback = bind(lib, "ISC_RegisterMessageCallback", [POINTER(c_char), c_short, CFUNCTYPE(None)])
ISC_MessageQueueSize = bind(lib, "ISC_MessageQueueSize", [POINTER(c_char)], c_int)
ISC_GetNextMessage = bind(lib, "ISC_GetNextMessage", [POINTER(c_char), POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
ISC_WaitForMessage = bind(lib, "ISC_WaitForMessage", [POINTER(c_char), POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
ISC_RequestHomingParams = bind(lib, "ISC_RequestHomingParams", [POINTER(c_char)], c_short)
ISC_GetHomingVelocity = bind(lib, "ISC_GetHomingVelocity", [POINTER(c_char)], c_uint)
ISC_SetHomingVelocity = bind(lib, "ISC_SetHomingVelocity", [POINTER(c_char), c_uint], c_short)
ISC_MoveRelative = bind(lib, "ISC_MoveRelative", [POINTER(c_char), c_int], c_short)
# This is a typo in given header file. Typo is also persistent in CHM file. Correct one follows.
# SCC_RequestJogParams = bind(lib, "SCC_RequestJogParams", [POINTER(c_char)], c_short)
ISC_RequestJogParams = bind(lib, "ISC_RequestJogParams", [POINTER(c_char)], c_short)
ISC_GetJogMode = bind(lib, "ISC_GetJogMode", [POINTER(c_char), POINTER(MOT_JogModes), POINTER(MOT_StopModes)], c_short)
ISC_SetJogMode = bind(lib, "ISC_SetJogMode", [POINTER(c_char), MOT_JogModes, MOT_StopModes], c_short)
ISC_GetJogStepSize = bind(lib, "ISC_GetJogStepSize", [POINTER(c_char)], c_uint)
ISC_SetJogStepSize = bind(lib, "ISC_SetJogStepSize", [POINTER(c_char), c_uint], c_short)
ISC_GetJogVelParams = bind(lib, "ISC_GetJogVelParams", [POINTER(c_char),POINTER(c_int), POINTER(c_int)], c_short)
ISC_SetJogVelParams = bind(lib, "ISC_SetJogVelParams", [POINTER(c_char), c_int, c_int], c_short)
ISC_MoveJog = bind(lib, "ISC_MoveJog", [POINTER(c_char), MOT_TravelDirection], c_short)
ISC_RequestVelParams = bind(lib, "ISC_RequestVelParams", [POINTER(c_char)], c_short)
ISC_GetVelParams = bind(lib, "ISC_GetVelParams", [POINTER(c_char), POINTER(c_int), POINTER(c_int)], c_short)
ISC_SetVelParams = bind(lib, "ISC_SetVelParams", [POINTER(c_char), c_int, c_int], c_short)
ISC_MoveAtVelocity = bind(lib, "ISC_MoveAtVelocity", [POINTER(c_char), MOT_TravelDirection], c_short)
ISC_SetDirection = bind(lib, "ISC_SetDirection", [POINTER(c_char), c_bool])
ISC_StopImmediate = bind(lib, "ISC_StopImmediate", [POINTER(c_char)], c_short)
ISC_StopProfiled = bind(lib, "ISC_StopProfiled", [POINTER(c_char)], c_short)
ISC_RequestBacklash = bind(lib, "ISC_RequestBacklash", [POINTER(c_char)], c_short)
ISC_GetBacklash = bind(lib, "ISC_GetBacklash", [POINTER(c_char)], c_long)
ISC_SetBacklash = bind(lib, "ISC_SetBacklash", [POINTER(c_char), c_long], c_short)
ISC_GetPositionCounter = bind(lib, "ISC_GetPositionCounter", [POINTER(c_char)], c_long)
ISC_SetPositionCounter = bind(lib, "ISC_SetPositionCounter", [POINTER(c_char), c_long], c_short)
ISC_RequestLimitSwitchParams = bind(lib, "ISC_RequestLimitSwitchParams", [POINTER(c_char)], c_short)
ISC_GetLimitSwitchParams = bind(lib, "ISC_GetLimitSwitchParams", [POINTER(c_char), POINTER(MOT_LimitSwitchModes), POINTER(MOT_LimitSwitchModes), POINTER(c_uint), POINTER(c_uint), POINTER(MOT_LimitSwitchSWModes)], c_short)
ISC_SetLimitSwitchParams = bind(lib, "ISC_SetLimitSwitchParams", [POINTER(c_char), MOT_LimitSwitchModes, MOT_LimitSwitchModes, c_uint, c_uint, MOT_LimitSwitchSWModes], c_short)
ISC_GetSoftLimitMode = bind(lib, "ISC_GetSoftLimitMode", [POINTER(c_char)], MOT_LimitsSoftwareApproachPolicy)
ISC_SetLimitsSoftwareApproachPolicy = bind(lib, "ISC_SetLimitsSoftwareApproachPolicy", [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy])
ISC_RequestButtonParams = bind(lib, "ISC_RequestButtonParams", [POINTER(c_char)], c_short)
ISC_GetButtonParams = bind(lib, "ISC_GetButtonParams", [POINTER(c_char), POINTER(MOT_ButtonModes), POINTER(c_int), POINTER(c_int), POINTER(c_short)], c_short)
ISC_SetButtonParams = bind(lib, "ISC_SetButtonParams", [POINTER(c_char), MOT_ButtonModes, c_int, c_int], c_short)
ISC_RequestPotentiometerParams = bind(lib, "ISC_RequestPotentiometerParams", [POINTER(c_char)], c_short)
ISC_GetPotentiometerParams = bind(lib, "ISC_GetPotentiometerParams", [POINTER(c_char), c_short, POINTER(c_word), POINTER(c_dword)], c_short)
ISC_SetPotentiometerParams = bind(lib, "ISC_SetPotentiometerParams", [POINTER(c_char), c_short, c_word, c_dword], c_short)
ISC_GetVelParamsBlock = bind(lib, "ISC_GetVelParamsBlock", [POINTER(c_char), POINTER(MOT_VelocityParameters)], c_short)
ISC_SetVelParamsBlock = bind(lib, "ISC_SetVelParamsBlock", [POINTER(c_char), POINTER(MOT_VelocityParameters)], c_short)
ISC_SetMoveAbsolutePosition = bind(lib, "ISC_SetMoveAbsolutePosition", [POINTER(c_char), c_int], c_short)
ISC_RequestMoveAbsolutePosition = bind(lib, "ISC_RequestMoveAbsolutePosition", [POINTER(c_char)], c_short)
ISC_GetMoveAbsolutePosition = bind(lib, "ISC_GetMoveAbsolutePosition", [POINTER(c_char)], c_int)
ISC_MoveAbsolute = bind(lib, "ISC_MoveAbsolute", [POINTER(c_char)], c_short)
ISC_SetMoveRelativeDistance = bind(lib, "ISC_SetMoveRelativeDistance", [POINTER(c_char), c_int], c_short)
ISC_RequestMoveRelativeDistance = bind(lib, "ISC_RequestMoveRelativeDistance", [POINTER(c_char)], c_short)
ISC_GetMoveRelativeDistance = bind(lib, "ISC_GetMoveRelativeDistance", [POINTER(c_char)], c_int)
ISC_MoveRelativeDistance = bind(lib, "ISC_MoveRelativeDistance", [POINTER(c_char)], c_short)
ISC_GetHomingParamsBlock = bind(lib, "ISC_GetHomingParamsBlock", [POINTER(c_char), POINTER(MOT_HomingParameters)], c_short)
ISC_SetHomingParamsBlock = bind(lib, "ISC_SetHomingParamsBlock", [POINTER(c_char), POINTER(MOT_HomingParameters)], c_short)
ISC_GetJogParamsBlock = bind(lib, "ISC_GetJogParamsBlock", [POINTER(c_char), POINTER(MOT_JogParameters)], c_short)
ISC_SetJogParamsBlock = bind(lib, "ISC_SetJogParamsBlock", [POINTER(c_char), POINTER(MOT_JogParameters)], c_short)
ISC_GetLimitSwitchParamsBlock = bind(lib, "ISC_GetLimitSwitchParamsBlock", [POINTER(c_char), POINTER(MOT_LimitSwitchParameters)], c_short)
ISC_SetLimitSwitchParamsBlock = bind(lib, "ISC_SetLimitSwitchParamsBlock", [POINTER(c_char), POINTER(MOT_LimitSwitchParameters)], c_short)
ISC_GetButtonParamsBlock = bind(lib, "ISC_GetButtonParamsBlock", [POINTER(c_char), POINTER(MOT_ButtonParameters)], c_short)
ISC_SetButtonParamsBlock = bind(lib, "ISC_SetButtonParamsBlock", [POINTER(c_char), POINTER(MOT_ButtonParameters)], c_short)
ISC_GetPotentiometerParamsBlock = bind(lib, "ISC_GetPotentiometerParamsBlock", [POINTER(c_char), POINTER(MOT_PotentiometerSteps)], c_short)
ISC_SetPotentiometerParamsBlock = bind(lib, "ISC_SetPotentiometerParamsBlock", [POINTER(c_char), POINTER(MOT_PotentiometerSteps)], c_short)
ISC_RequestPowerParams = bind(lib, "ISC_RequestPowerParams", [POINTER(c_char)], c_short)
ISC_GetPowerParams = bind(lib, "ISC_GetPowerParams", [POINTER(c_char), POINTER(MOT_PowerParameters)], c_short)
ISC_SetPowerParams = bind(lib, "ISC_SetPowerParams", [POINTER(c_char), POINTER(MOT_PowerParameters)], c_short)
ISC_RequestBowIndex = bind(lib, "ISC_RequestBowIndex", [POINTER(c_char)], c_short)
ISC_GetBowIndex = bind(lib, "ISC_GetBowIndex", [POINTER(c_char)], c_short)
ISC_SetBowIndex = bind(lib, "ISC_SetBowIndex", [POINTER(c_char), c_short], c_short)
ISC_RequestTriggerSwitches = bind(lib, "ISC_RequestTriggerSwitches", [POINTER(c_char)], c_short)
ISC_GetTriggerSwitches = bind(lib, "ISC_GetTriggerSwitches", [POINTER(c_char)], c_byte)
ISC_SetTriggerSwitches = bind(lib, "ISC_SetTriggerSwitches", [POINTER(c_char), c_byte], c_short)
ISC_RequestPosition = bind(lib, "ISC_RequestPosition", [POINTER(c_char)], c_short)
ISC_RequestStatusBits = bind(lib, "ISC_RequestStatusBits", [POINTER(c_char)], c_short)
ISC_RequestStatus = bind(lib, "ISC_RequestStatus", [POINTER(c_char)], c_short)
ISC_GetStatusBits = bind(lib, "ISC_GetStatusBits", [POINTER(c_char)], c_dword)
ISC_StartPolling = bind(lib, "ISC_StartPolling", [POINTER(c_char), c_int], c_bool)
ISC_PollingDuration = bind(lib, "ISC_PollingDuration", [POINTER(c_char)], c_long)
ISC_StopPolling = bind(lib, "ISC_StopPolling", [POINTER(c_char)])
# ISC_TimeSinceLastMsgReceived <- TODO: ISC_API bool __cdecl ISC_TimeSinceLastMsgReceived(char const * serialNo, __int64 &lastUpdateTimeMS );
ISC_EnableLastMsgTimer = bind(lib, "ISC_EnableLastMsgTimer", [POINTER(c_char), c_bool, c_int32])
ISC_HasLastMsgTimerOverrun = bind(lib, "ISC_HasLastMsgTimerOverrun", [POINTER(c_char)], c_bool)
ISC_RequestSettings = bind(lib, "ISC_RequestSettings", [POINTER(c_char)], c_short)
ISC_GetStageAxisMinPos = bind(lib, "ISC_GetStageAxisMinPos", [POINTER(c_char)], c_int)
ISC_GetStageAxisMaxPos = bind(lib, "ISC_GetStageAxisMaxPos", [POINTER(c_char)], c_int)
ISC_SetStageAxisLimits = bind(lib, "ISC_SetStageAxisLimits", [POINTER(c_char), c_int, c_int], c_short)
ISC_SetMotorTravelMode = bind(lib, "ISC_SetMotorTravelMode", [POINTER(c_char), MOT_TravelModes], c_short)
ISC_GetMotorTravelMode = bind(lib, "ISC_GetMotorTravelMode", [POINTER(c_char)], MOT_TravelModes)
ISC_SetMotorParams = bind(lib, "ISC_SetMotorParams", [POINTER(c_char), c_long, c_long, c_float], c_short)
ISC_GetMotorParams = bind(lib, "ISC_GetMotorParams", [POINTER(c_char), POINTER(c_long), POINTER(c_long), POINTER(c_float)], c_short)
ISC_SetMotorParamsExt = bind(lib, "ISC_SetMotorParamsExt", [POINTER(c_char), c_double, c_double, c_double], c_short)
ISC_GetMotorParamsExt = bind(lib, "ISC_GetMotorParamsExt", [POINTER(c_char), POINTER(c_double), POINTER(c_double), POINTER(c_double)], c_short)
ISC_SetMotorVelocityLimits = bind(lib, "ISC_SetMotorVelocityLimits", [POINTER(c_char), c_double, c_double], c_short)
ISC_GetMotorVelocityLimits = bind(lib, "ISC_GetMotorVelocityLimits", [POINTER(c_char), POINTER(c_double), POINTER(c_double)], c_short)
ISC_ResetRotationModes = bind(lib, "ISC_ResetRotationModes", [POINTER(c_char)], c_short)
ISC_SetRotationModes = bind(lib, "ISC_SetRotationModes", [POINTER(c_char), MOT_MovementModes, MOT_MovementDirections], c_short)
ISC_SetMotorTravelLimits = bind(lib, "ISC_SetMotorTravelLimits", [POINTER(c_char), c_double, c_double], c_short)
ISC_GetMotorTravelLimits = bind(lib, "ISC_GetMotorTravelLimits", [POINTER(c_char), POINTER(c_double), POINTER(c_double)], c_short)
ISC_GetRealValueFromDeviceUnit = bind(lib, "ISC_GetRealValueFromDeviceUnit", [POINTER(c_char), c_int, POINTER(c_double), c_int], c_short)
ISC_GetDeviceUnitFromRealValue = bind(lib, "ISC_GetDeviceUnitFromRealValue", [POINTER(c_char), c_double, POINTER(c_int), c_int], c_short)
