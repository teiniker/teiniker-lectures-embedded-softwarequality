import pytest
from device import Device, DeviceError, Sensor, SensorError


def test_config_sensor_invalid_gain(mocker):
    # Setup
    sensor = mocker.Mock(spec=Sensor)
    device = Device(sensor)
    # Exercise and Verify
    with pytest.raises(ValueError):
        device.config_sensor(-1, 0)


def test_config_sensor_invalid_offset(mocker):
    # Setup
    sensor = mocker.Mock(spec=Sensor)
    device = Device(sensor)
    # Exercise and Verify
    with pytest.raises(ValueError):
        device.config_sensor(1, -1)

# TODO: Implement more tests
