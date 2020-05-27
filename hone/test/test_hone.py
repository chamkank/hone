import os
import unittest
import json
from hone import hone
from hone.utils import test_utils

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "small_cats_dataset", "dataset.csv")
json_A_path = os.path.join(dirname, "data", "small_cats_dataset", "nested_dataset.json")
json_schema_A_path = os.path.join(dirname, "data", "small_cats_dataset", "nested_schema.json")
csv_B_path = os.path.join(dirname, "data", "comma_test", "dataset.csv")
json_B_path = os.path.join(dirname, "data", "comma_test", "nested_dataset.json")


class TestHone(unittest.TestCase):
    def test_nest_small_csv(self):
        h = hone.Hone()
        actualResult = h.convert(csv_A_path)
        expectedResult = test_utils.parse_json_file(json_A_path)
        self.assertListEqual(actualResult, expectedResult)
    def test_get_schema(self):
        h = hone.Hone()
        actualResult = h.get_schema(csv_A_path)
        expectedResult = test_utils.parse_json_file(json_schema_A_path)
        self.assertDictEqual(actualResult, expectedResult)
    def test_nest_comma_csv(self):
        h = hone.Hone()
        actualResult = h.convert(csv_B_path)
        expectedResult = test_utils.parse_json_file(json_B_path)
        self.assertListEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()
