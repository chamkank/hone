import os
import unittest
from hone import hone

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "small_cats_dataset.csv")
csv_B_path = os.path.join(dirname, "data", "comma_test.csv")


class TestHone(unittest.TestCase):
    def test_nest_small_csv(self):
        tn_A = hone.Hone()
        result = tn_A.convert(csv_A_path)
        self.assertListEqual(result,
                             [{'adopted_since': '2018', 'adopted': 'TRUE',
                               'birth': {'year': '2015', 'month': 'January', 'day': '18'}, 'weight (kg)': '3.1',
                               'age (years)': '3', 'name': 'Ciel'}, {'adopted_since': '2018', 'adopted': 'TRUE',
                                                                     'birth': {'year': '2015', 'month': 'January',
                                                                               'day': '18'}, 'weight (kg)': '3.1',
                                                                     'age (years)': '3', 'name': 'Ciel'},
                              {'adopted_since': '2018', 'adopted': 'TRUE',
                               'birth': {'year': '2015', 'month': 'January', 'day': '18'}, 'weight (kg)': '3.1',
                               'age (years)': '3', 'name': 'Ciel'}, {'adopted_since': '2018', 'adopted': 'TRUE',
                                                                     'birth': {'year': '2015', 'month': 'January',
                                                                               'day': '18'}, 'weight (kg)': '3.1',
                                                                     'age (years)': '3', 'name': 'Ciel'}]
                             )
    def test_get_schema(self):
        tn_A = hone.Hone()
        result = tn_A.get_schema(csv_A_path)
        self.assertDictEqual(result, {'adopted_since': 'adopted_since', 'adopted': 'adopted',
                                      'birth': {'year': 'birth year', 'month': 'birth month', 'day': 'birth day'},
                                      'weight (kg)': 'weight (kg)', 'age (years)': 'age (years)', 'name': 'name'})
    def test_nest_comma_csv(self):
        tn_B = hone.Hone()
        result = tn_B.convert(csv_B_path)
        self.assertListEqual(result, [{'beep': '2', 'test"",""ing': '1'}])


if __name__ == '__main__':
    unittest.main()
