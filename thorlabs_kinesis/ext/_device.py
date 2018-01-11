"Device related objects."

from collections import namedtuple

__all__ = [
    "serial_prefix"
]

Device = namedtuple("Device", ["module", "type"])

serial_prefix = {
    73: Device(None, "Benchtop Brushless Motor"),
    22: Device(None, "Benchtop NanoTrak"),
    41: Device(None, "Benchtop Piezo (1 channel)"),
    71: Device(None, "Benchtop Piezo (3 channel)"),
    40: Device("benchtop_stepper_motor", "Benchtop Stepper Motor (1 channel)"),
    70: Device("benchtop_stepper_motor", "Benchtop Stepper Motor (3 channel)"),
    37: Device(None, "Filter Flipper"),
    47: Device(None, "Filter Wheel"),
    28: Device(None, "KCube Brushless Motor"),
    27: Device(None, "KCube DC Servo"),
    97: Device(None, "KCube Inertial Motor"),
    56: Device(None, "KCube LaserSource"),
    57: Device(None, "KCube NanoTrak"),
    29: Device(None, "KCube Piezo"),
    68: Device(None, "KCube Solenoid"),
    26: Device(None, "KCube Stepper Motor"),
    45: Device("integrated_stepper_motors", "Long Travel Stage"),
    55: Device("integrated_stepper_motors", "Cage Rotator"),
    46: Device("integrated_stepper_motors", "LabJack 490"),
    49: Device("integrated_stepper_motors", "LabJack 050"),
    52: Device(None, "Modular NanoTrak"),
    51: Device(None, "Modular Piezo"),
    50: Device(None, "Modular Stepper Motor"),
    67: Device(None, "TCube Brushless Motor"),
    83: Device(None, "TCube DC Servo"),
    65: Device(None, "TCube Inertial Motor"),
    86: Device(None, "TCube LaserSource"),
    64: Device(None, "TCube LaserDiode"),
    82: Device(None, "TCube NanoTrak"),
    89: Device(None, "TCube Quad"),
    85: Device(None, "TCube Solenoid"),
    80: Device(None, "TCube Stepper Motor"),
    84: Device(None, "TCube Strain Gauge"),
    87: Device(None, "TCube TEC"),
    24: Device(None, "Vertical Stage"),
}


def expand_device(serial_no: str) -> Device:
    """Expand name and module related to device by checking first two numbers
    of the serial_no.
    """
    return serial_prefix[int(serial_no[:2])]
