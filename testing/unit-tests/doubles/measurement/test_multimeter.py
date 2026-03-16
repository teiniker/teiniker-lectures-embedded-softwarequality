import pytest

from multimeter import Device, DeviceError, MeasurementError, MODE, Multimeter


def test_multimeter_set_mode(mocker):
    # Setup
    device = mocker.Mock(spec=Device)
    multimeter = Multimeter(device)
    # Exercise
    multimeter.set_mode(MODE.DCV)
    # Verify
    device.set_measurement_mode.assert_called_with("dc_v")


def test_multimeter_set_range(mocker):
    # Setup
    device = mocker.Mock(spec=Device)
    multimeter = Multimeter(device)
    # Exercise
    multimeter.set_range(10)
    # Verify
    device.set_measurement_range.assert_called_with(10)


def test_multimeter_measurement(mocker):
    # Setup
    device = mocker.Mock(spec=Device)
    device.get_measurement_value.return_value = 5.0
    multimeter = Multimeter(device)
    # Exercise
    result = multimeter.measure()
    # Verify
    assert result == pytest.approx(5.0, abs=1e-3)


def test_multimeter_measurement_error(mocker):
    # Setup
    device = mocker.Mock(spec=Device)
    device.get_measurement_value.side_effect = DeviceError("Hardware problem!")
    multimeter = Multimeter(device)
    # Exercise & Verify
    with pytest.raises(MeasurementError):
        multimeter.measure()
