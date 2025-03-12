import unittest
from unittest.mock import Mock

from multimeter import Multimeter,MODE,MeasurementError,DeviceError

class MultimeterTest(unittest.TestCase):
    def test_multimeter_set_mode(self):
        # Setup
        device = Mock()  # Mock() replaces Device
        multimeter = Multimeter(device)

        # Exercise
        multimeter.set_mode(MODE.DCV)

        # Verify
        device.set_measurement_mode.assert_called_with("dc_v")

    def test_multimeter_set_range(self):
        # Setup
        device = Mock()  # Mock() replaces Device
        multimeter = Multimeter(device)

        # Exercise
        multimeter.set_range(10)

        # Verify
        device.set_measurement_range.assert_called_with(10)

    def test_multimeter_measurement(self):
        # Setup
        device = Mock()  # Mock() replaces Device
        device.get_measurement_value.return_value = 5.0
        multimeter = Multimeter(device)

        # Exercise
        result = multimeter.measure()

        # Verify
        self.assertAlmostEqual(5.0, result, 1e-3)

    def test_multimeter_measurement_error(self):
        # Setup
        device = Mock()  # Mock() replaces Device
        device.get_measurement_value.side_effect = DeviceError('Hardware problem!')
        multimeter = Multimeter(device)

        # Exercise & Verify
        with self.assertRaises(MeasurementError):
            multimeter.measure()

if __name__ == '__main__':
    unittest.main()
