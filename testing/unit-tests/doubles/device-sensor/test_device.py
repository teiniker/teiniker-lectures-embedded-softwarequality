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


def test_config_sensor_calls_sensor_configuration(mocker):
    # Setup
    sensor = mocker.Mock(spec=Sensor)
    device = Device(sensor)
    # Exercise
    device.config_sensor(1, 0)
    # Verify
    sensor.set_gain.assert_called_with(1)
    sensor.set_offset.assert_called_with(0)


def test_get_temperature_returns_sensor_value(mocker):
    # Setup
    sensor = mocker.Mock(spec=Sensor)
    device = Device(sensor)
    sensor.read_temperature_value.return_value = 24.71
    # Exercise
    temp = device.get_temperature()
    # Verify
    assert temp == pytest.approx(24.71, abs=0.01)


def test_get_temperature_raises_device_error_on_sensor_error(mocker):
    # Setup
    sensor = mocker.Mock(spec=Sensor)
    device = Device(sensor)
    sensor.read_temperature_value.side_effect = SensorError()
    # Exercise and Verify
    with pytest.raises(DeviceError):
        device.get_temperature()
