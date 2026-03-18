
from typing import Protocol


class SensorError(Exception):
    pass

class DeviceError(Exception):
    pass


#TODO: Implement Sensor protocol


class Device:
    sensor: Sensor # ---[1]-> Sensor

    def __init__(self, sensor: Sensor) -> None:
        self.sensor = sensor

    def config_sensor(self, gain: float, offset: float) -> None:
        if gain < 1.0 or gain > 10.0:
            raise ValueError('Invalid gain value!')
        if offset < 0.0 or offset > 10.0:
            raise ValueError('Invalid offset value!')

        self.sensor.set_gain(gain)
        self.sensor.set_offset(offset)

    def get_temperature(self) -> float:
        try:
            return self.sensor.read_temperature_value()
        except SensorError as ex:
            raise DeviceError('Cannot get temperature!') from ex
