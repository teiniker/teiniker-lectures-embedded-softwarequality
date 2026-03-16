from enum import Enum
from typing import Protocol

class MeasurementError(Exception):
    pass

class DeviceError(Exception):
    pass

class MODE(Enum):
    DCV = 1
    ACV = 2
    DCI = 3
    ACI = 4
    RES = 5


class Device(Protocol):
    def set_measurement_mode(self, mode: str) -> None:
        ...

    def set_measurement_range(self, range_value: float) -> None:
        ...

    def get_measurement_value(self) -> float:
        ...


class Multimeter:
    def __init__(self, device: Device) -> None:
        self.device = device
        self.mode_dictionary = {
                MODE.DCV: "dc_v",
                MODE.ACV: "ac_v",
                MODE.DCI: "dc_i",
                MODE.ACI: "ac_i",
                MODE.RES: "res"
            }

    def set_mode(self, mode: MODE) -> None:
        self.device.set_measurement_mode(self.mode_dictionary.get(mode))

    def set_range(self, range_value: float) -> None:
        self.device.set_measurement_range(range_value)

    def measure(self)-> float:
        try:
            return self.device.get_measurement_value()
        except DeviceError as ex:
            raise MeasurementError('Can not perform measurement!') from ex
