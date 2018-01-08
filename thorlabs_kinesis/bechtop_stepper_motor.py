"Bindings for Thorlabs Benchtop Stepper Motor DLL"
from ctypes import (
    cdll,
    c_short,
    c_int,
    c_int16
)

from _utils import (
    c_word
)

lib = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.StepperMotor.dll")


# Values that represent FT_Status.
FT_OK = c_short(0x00)  # <OK - no error.
FT_InvalidHandle = c_short(0x01)  # <Invalid handle.
FT_DeviceNotFound = c_short(0x02)  # <Device not found.
FT_DeviceNotOpened = c_short(0x03)  # <Device not opened.
FT_IOError = c_short(0x04)  # <I/O error.
FT_InsufficientResources = c_short(0x05)  # <Insufficient resources.
FT_InvalidParameter = c_short(0x06)  # <Invalid parameter.
FT_DeviceNotPresent = c_short(0x07)  # <Device not present.
FT_IncorrectDevice = c_short(0x08)  # <Incorrect device.

# Values that represent THORLABSDEVICE_API.
MOT_NotMotor = c_int(0)
MOT_DCMotor = c_int(1)
MOT_StepperMotor = c_int(2)
MOT_BrushlessMotor = c_int(3)
MOT_CustomMotor = c_int(100)

# Values that represent Travel Modes.
MOT_TravelModeUndefined = c_int(0x00)  # <Undefined
MOT_Linear = c_int(0x01)  # <Linear travel, default units are millimeters
MOT_Rotational = c_int(0x02)  # <Rotational travel, default units are degrees

# Values that represent Travel Modes.
MOT_TravelDirectionUndefined = c_short(0x00)  # <Undefined
MOT_Forwards = c_short(0x01)  # <Move in a Forward direction
MOT_Reverse = c_short(0x02)  # <Move in a Backward / Reverse direction

# Values that represent Limit Switch Directions.
MOT_LimitSwitchDirectionUndefined = c_short(0x00)  # <Undefined
MOT_ReverseLimitSwitch = c_short(0x01)  # <Limit switch in forward direction
MOT_ForwardLimitSwitch = c_short(0x04)  # <Limit switch in reverse direction

# Values that represent Direction Type.
MOT_Normal = c_short(0x00)  # <Move / Jog direction is normal (clockwise).
MOT_Backwards = c_short(0x01)  # <Move / Jog direction is reversed (anti cw).

# Values that represent the motor Jog Modes.
MOT_JogModeUndefined = c_short(0x00)  # <Undefined
MOT_Continuous = c_short(0x01)  # <Continuous jogging
MOT_SingleStep = c_short(0x02)  # <Jog 1 step at a time

# Values that represent the motor Jog Modes.
MOT_StopModeUndefined = c_short(0x00)  # <Undefined
MOT_Immediate = c_short(0x01)  # <Stops immediate
MOT_Profiled = c_short(0x02)  # <Stops using a velocity profile

# Values that represent the motor Button Modes.
MOT_ButtonModeUndefined = c_word(0x00)  # <Undefined
MOT_JogMode = c_word(0x01)  # <Jog motor in correct direction for button
MOT_Preset = c_word(0x02)  # <Move to preset position

# Value that represent action to be taken when motor hits a limit switch.
MOT_LimitSwitchModeUndefined = c_word(0x00)  # <Undefined
MOT_LimitSwitchIgnoreSwitch = c_word(0x01)  # <Ignore limit switch
MOT_LimitSwitchMakeOnContact = c_word(0x02)  # <Switch makes on contact
MOT_LimitSwitchBreakOnContact = c_word(0x03)  # <Switch breaks on contact
MOT_LimitSwitchMakeOnHome = c_word(0x04)  # <Switch makes on contact when homing
MOT_LimitSwitchBreakOnHome = c_word(0x05)  # <Switch breaks on contact when homing
MOT_PMD_Reserved = c_word(0x06)  # <Reserved for PMD brushless servo controllers
MOT_LimitSwitchIgnoreSwitchSwapped = c_word(0x81)  # <Ignore limit switch (swapped)
MOT_LimitSwitchMakeOnContactSwapped = c_word(0x82)  # <Switch makes on contact (swapped)
MOT_LimitSwitchBreakOnContactSwapped = c_word(0x83)  # <Switch breaks on contact (swapped)
MOT_LimitSwitchMakeOnHomeSwapped = c_word(0x84)  # <Switch makes on contact when homing (swapped)
MOT_LimitSwitchBreakOnHomeSwapped = c_word(0x85)  # <Switch breaks on contact when homing (swapped)

# Value that represent action to be taken when motor hits a limit switch.
MOT_LimitSwitchSWModeUndefined = c_word(0x00)  # <Undefined
MOT_LimitSwitchIgnored = c_word(0x01)  # <Ignore limit switch
MOT_LimitSwitchStopImmediate = c_word(0x02)  # <Stop immediately when hitting limit switch
MOT_LimitSwitchStopProfiled = c_word(0x03)  # <Stop profiled when hitting limit switch
MOT_LimitSwitchIgnored_Rotational = c_word(0x81)  # <Ignore limit switch (rotational stage)
MOT_LimitSwitchStopImmediate_Rotational = c_word(0x82)  # <Stop immediately when hitting limit switch (rotational stage)
MOT_LimitSwitchStopProfiled_Rotational = c_word(0x83)  # <Stop profiled when hitting limit switch (rotational stage)

# Values that represent MOT_LimitsSoftwareApproachPolicy.
DisallowIllegalMoves = c_int16(0)  # <Disable any move outside travel range
AllowPartialMoves = c_int16(1)  # <Truncate all moves beyond limit to limit.
AllowAllMoves = c_int16(2)  # <Allow all moves, illegal or not

# Values that represent the Encoder PID Loop modes.
MOT_PIDLoopModeDisabled = c_word(0x00)  # <Disabled or Undefined
MOT_PIDOpenLoopMode = c_word(0x01)  # <Encoder is in open loop mode
MOT_PIDClosedLoopMode = c_word(0x02)  # <Encoder is in closed loop mode

# Values that represent DeviceMessageClass message types.
LinearRange = c_int(0x00)  # < Fixed Angular Range defined by MinPosition and MaxPosition
RotationalUnlimited = c_int(0x01)  # < Unlimited angle
RotationalWrapping = c_int(0x02)  # < Angular Range 0 to 360 with wrap around

# Values that represent DeviceMessageClass message types.
Quickest = c_int(0x00)  # < Uses the shortest travel between two angles
Forwards = c_int(0x01)  # < Only rotate in a forward direction
Reverse = c_int(0x02)  # < Only rotate in a backward direction
