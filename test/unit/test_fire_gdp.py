import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))

import fire_gdp 


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ["Country", "Year", "GDP"]
        result = fire_gdp.get_column_index(header, "Year")
        self.assertEqual(result, 1)

    def test_name_absent(self):
        header = ["Country", "Year", "GDP"]
        result = fire_gdp.get_column_index(header, "Population")
        self.assertIsNone(result)

    def test_empty_header(self):
        header = []
        result = fire_gdp.get_column_index(header, "Year")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
