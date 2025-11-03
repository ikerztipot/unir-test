import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # SQRT tests
    def test_sqrt_positive(self):
        calc = Calculator()
        self.assertEqual(calc.sqrt(16), 4.0)
        self.assertEqual(calc.sqrt(2), pytest.approx(1.4142135623730951))
        self.assertEqual(calc.sqrt(0), 0.0)

    def test_sqrt_negative(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.sqrt(-1)
        self.assertEqual(str(context.exception), "Cannot calculate square root of a negative number")

    def test_sqrt_invalid_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.sqrt("16")
        self.assertEqual(str(context.exception), "Parameters must be numbers")

    #Log10 tests
    def test_log10_positive(self):
        calc = Calculator()
        self.assertEqual(calc.log10(100), 2.0)
        self.assertEqual(calc.log10(10), 1.0)
        self.assertEqual(calc.log10(1), 0.0)

    def test_log10_negative(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.log10(-1)
        self.assertEqual(str(context.exception), "Cannot calculate logarithm of zero or negative number")

    def test_log10_zero(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.log10(0)
        self.assertEqual(str(context.exception), "Cannot calculate logarithm of zero or negative number")

    def test_log10_invalid_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.log10("10")
        self.assertEqual(str(context.exception), "Parameters must be numbers")

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
