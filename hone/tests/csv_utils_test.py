import os
import unittest
from hone.utils import csv_utils

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "small_cats_dataset.csv")
csv_B_path = os.path.join(dirname, "data", "comma_test.csv")
small_csv = csv_utils.CSVUtils(csv_A_path)
comma_csv = csv_utils.CSVUtils(csv_B_path)


class TestCSVUtils(unittest.TestCase):
    def test_get_column_names(self):
        self.assertListEqual(small_csv.get_column_names(),
                             ['name', 'age (years)', 'weight (kg)', 'birth day', 'birth month', 'birth year',
                              'adopted', 'adopted_since'])
        self.assertListEqual(comma_csv.get_column_names(),
                             ['test"",""ing', 'beep'])

    def test_get_data_rows(self):
        self.assertListEqual(small_csv.get_data_rows(),
                             [['Tommy', '5', '3.6', '11', 'April', '2011', 'TRUE', '2012'],
                              ['Clara', '2', '8.2', '6', 'May', '2015', 'FALSE', 'N/A'],
                              ['Catnip', '6', '3.3', '21', 'August', '2011', 'TRUE', '2017'],
                              ['Ciel', '3', '3.1', '18', 'January', '2015', 'TRUE', '2018']])
        self.assertListEqual(comma_csv.get_data_rows(),
                             [['1', '2']])


if __name__ == '__main__':
    unittest.main()
