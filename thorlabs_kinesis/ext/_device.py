"Device related objects."
from collections import namedtuple

__all__ = [
    "serial_prefix"
]

Device = namedtuple("Device", ["module", "type", "prefix"])
MotorEncoderSettings = namedtuple("MotorEncoderSettings",
                                  ["position",
                                   "velocity",
                                   "acceleration"])

serial_prefix = {
    73: Device(None, "Benchtop Brushless Motor", ""),
    22: Device(None, "Benchtop NanoTrak", ""),
    41: Device(None, "Benchtop Piezo (1 channel)", ""),
    71: Device(None, "Benchtop Piezo (3 channel)", ""),
    40: Device("benchtop_stepper_motor", "Benchtop Stepper Motor (1 channel)", "SBC"),  # noqa: E501
    70: Device("benchtop_stepper_motor", "Benchtop Stepper Motor (3 channel)", "SBC"),  # noqa: E501
    37: Device(None, "Filter Flipper", ""),
    47: Device(None, "Filter Wheel", ""),
    28: Device(None, "KCube Brushless Motor", ""),
    27: Device(None, "KCube DC Servo", ""),
    97: Device(None, "KCube Inertial Motor", ""),
    56: Device(None, "KCube LaserSource", ""),
    57: Device(None, "KCube NanoTrak", ""),
    29: Device(None, "KCube Piezo", ""),
    68: Device(None, "KCube Solenoid", ""),
    26: Device(None, "KCube Stepper Motor", ""),
    45: Device("integrated_stepper_motors", "Long Travel Stage", "ISC"),
    55: Device("integrated_stepper_motors", "Cage Rotator", "ISC"),
    46: Device("integrated_stepper_motors", "LabJack 490", "ISC"),
    49: Device("integrated_stepper_motors", "LabJack 050", "ISC"),
    52: Device(None, "Modular NanoTrak", ""),
    51: Device(None, "Modular Piezo", ""),
    50: Device(None, "Modular Stepper Motor", ""),
    67: Device(None, "TCube Brushless Motor", ""),
    83: Device(None, "TCube DC Servo", ""),
    65: Device(None, "TCube Inertial Motor", ""),
    86: Device(None, "TCube LaserSource", ""),
    64: Device(None, "TCube LaserDiode", ""),
    82: Device(None, "TCube NanoTrak", ""),
    89: Device(None, "TCube Quad", ""),
    85: Device(None, "TCube Solenoid", ""),
    80: Device(None, "TCube Stepper Motor", ""),
    84: Device(None, "TCube Strain Gauge", ""),
    87: Device(None, "TCube TEC", ""),
    24: Device(None, "Vertical Stage", ""),
}

motor_encoder_lib = {
    "HS DRV001 8mm": MotorEncoderSettings(546100, 29320310, 6008),
}


def expand_device(serial_no: str) -> Device:
    """Expand name and module related to device by checking first two numbers
    of the serial_no.
    """
    return serial_prefix[int(serial_no[:2])]


def device_to_real_units(motor_type: str,
                         dev: int, dimension: str="position") -> float:
    """Converts given device units [steps] to real units [mm]. Dimension can be
    'position', 'velocity', or 'acceleration'.

    >>> device_to_real_units("HS DRV001 8mm", 546100)
    1.0

    >>> device_to_real_units("HS DRV001 8mm", 1.0, "position")
    1.8311664530305805e-06

    >>> device_to_real_units("HS DRV001 8mm", 1.0, "velocity")
    3.410605140259431e-08

    >>> device_to_real_units("HS DRV001 8mm", 1.0, "acceleration")
    0.00016644474034620507

    >>> device_to_real_units("HS DRV001 8mm", 1.0, "Acceleration")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert given dimension.

    >>> device_to_real_units("HS DRV001 8mm", 1.0, "Non existent")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert given dimension.

    >>> device_to_real_units("Non existent", 1.0, "acceleration")
    Traceback (most recent call last):
        ...
    ValueError: Can't find given motor encoder.
    """
    motor_enc = motor_encoder_lib.get(motor_type, None)

    if motor_enc is None:
        raise ValueError("Can't find given motor encoder.")

    scale = getattr(motor_enc, dimension, None)

    if scale is None:
        raise TypeError("Can't convert given dimension.")

    return dev / scale


def real_to_device_units(motor_type: str,
                         real: float, dimension: str="position") -> int:
    """Converts given real units [mm] to encoder steps. Dimension can be
    'position', 'velocity', or 'acceleration'.

    >>> real_to_device_units("HS DRV001 8mm", 1.0)
    546100

    >>> real_to_device_units("HS DRV001 8mm", 1.0, "position")
    546100

    >>> real_to_device_units("HS DRV001 8mm", 1.0, "velocity")
    29320310

    >>> real_to_device_units("HS DRV001 8mm", 1.0, "acceleration")
    6008

    >>> real_to_device_units("HS DRV001 8mm", 1.0, "Acceleration")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert given dimension.

    >>> real_to_device_units("HS DRV001 8mm", 1.0, "Non existent")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert given dimension.

    >>> real_to_device_units("Non existent", 1.0, "acceleration")
    Traceback (most recent call last):
        ...
    ValueError: Can't find given motor encoder.
    """

    motor_enc = motor_encoder_lib.get(motor_type, None)

    if motor_enc is None:
        raise ValueError("Can't find given motor encoder.")

    scale = getattr(motor_enc, dimension, None)

    if scale is None:
        raise TypeError("Can't convert given dimension.")

    return round(real * scale)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
