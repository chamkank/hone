import os
import unittest
import csv
from hone.utils import csv_utils, test_utils

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "small_cats_dataset", "dataset.csv")
column_names_A_path = os.path.join(dirname, "data", "small_cats_dataset", "column_names.csv")
data_rows_A_path = os.path.join(dirname, "data", "small_cats_dataset", "data_rows.csv")
csv_B_path = os.path.join(dirname, "data", "comma_test", "dataset.csv")
column_names_B_path = os.path.join(dirname, "data", "comma_test", "column_names.csv")
data_rows_B_path = os.path.join(dirname, "data", "comma_test", "data_rows.csv")


class TestCSVUtils(unittest.TestCase):
    def test_get_column_names(self):
        csv_utils.CSVUtils(column_names_A_path)
        actual_result_A = csv_utils.CSVUtils(csv_A_path).get_column_names()
        expected_result_A = test_utils.parse_csv_file(column_names_A_path)[0]
        actual_result_B = csv_utils.CSVUtils(csv_B_path).get_column_names()
        expected_result_B = test_utils.parse_csv_file(column_names_B_path)[0]
        self.assertListEqual(actual_result_B, expected_result_B)  
        self.assertListEqual(actual_result_A, expected_result_A)

    def test_get_data_rows(self):
        actual_result_A = csv_utils.CSVUtils(csv_A_path).get_data_rows()
        expected_result_A = test_utils.parse_csv_file(data_rows_A_path)
        actual_result_B = csv_utils.CSVUtils(csv_B_path).get_data_rows()
        expected_result_B = test_utils.parse_csv_file(data_rows_B_path)
        self.assertListEqual(actual_result_A, expected_result_A)
        self.assertListEqual(actual_result_B, expected_result_B)


if __name__ == '__main__':
    unittest.main()
