import http.client
import os
import unittest
from urllib.request import urlopen
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Add tests
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_error(self):
        url = f"{BASE_URL}/calc/add/abc/3"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    # Substract tests
    def test_api_substract_ok(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_error(self):
        url = f"{BASE_URL}/calc/substract/abc/3"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    # Multiply tests
    def test_api_multiply_ok(self):
        url = f"{BASE_URL}/calc/multiply/4/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_error(self):
        url = f"{BASE_URL}/calc/multiply/abc/3"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    # Divide tests
    def test_api_divide_ok(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/6/0"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    def test_api_divide_error(self):
        url = f"{BASE_URL}/calc/divide/abc/2"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    # Power tests
    def test_api_power_ok(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_error(self):
        url = f"{BASE_URL}/calc/power/abc/2"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

        # SQRT tests
    def test_get_sqrt_ok(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_get_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    def test_get_sqrt_invalid(self):
        url = f"{BASE_URL}/calc/sqrt/abc"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    # Log10 tests
    def test_get_log10_ok(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_get_log10_negative(self):
        url = f"{BASE_URL}/calc/log10/-1"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    def test_get_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))

    def test_get_log10_invalid(self):
        url = f"{BASE_URL}/calc/log10/abc"
        with self.assertRaises(Exception) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertTrue('400' in str(context.exception))