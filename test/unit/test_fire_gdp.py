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
        
class TestGetData(unittest.TestCase):

    def test_get_all_rows(self):
        file_name = "test/data/test_co2.csv"
        result = fire_gdp.get_data(file_name)
        expected = [
            ["Brazil", "2000", "100.5", "50"],
            ["Brazil", "2001", "110.0", "55"],
            ["Brazil", "2002", "", "60"],
            ["Canada", "2000", "20.0", "30"],
            ["Canada", "2001", "25.5", "35"]
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
