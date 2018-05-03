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
                             [
                                 {
                                     "adopted": "TRUE",
                                     "adopted_since": "2012",
                                     "age (years)": "5",
                                     "birth": {
                                         "day": "11",
                                         "month": "April",
                                         "year": "2011"
                                     },
                                     "name": "Tommy",
                                     "weight (kg)": "3.6"
                                 },
                                 {
                                     "adopted": "FALSE",
                                     "adopted_since": "N/A",
                                     "age (years)": "2",
                                     "birth": {
                                         "day": "6",
                                         "month": "May",
                                         "year": "2015"
                                     },
                                     "name": "Clara",
                                     "weight (kg)": "8.2"
                                 },
                                 {
                                     "adopted": "TRUE",
                                     "adopted_since": "2017",
                                     "age (years)": "6",
                                     "birth": {
                                         "day": "21",
                                         "month": "August",
                                         "year": "2011"
                                     },
                                     "name": "Catnip",
                                     "weight (kg)": "3.3"
                                 },
                                 {
                                     "adopted": "TRUE",
                                     "adopted_since": "2018",
                                     "age (years)": "3",
                                     "birth": {
                                         "day": "18",
                                         "month": "January",
                                         "year": "2015"
                                     },
                                     "name": "Ciel",
                                     "weight (kg)": "3.1"
                                 }
                             ]
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
