import argparse
from hone.hone import Hone
from hone.utils import csv_utils, json_utils

DELMITERS_HELP_MESSAGE = f"Override the default delimiters for generating a nested structure from column names. [DELIMITERS] must be a Python-compatible list of strings. The default value is {Hone.DEFAULT_DELIMITERS}."

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delimiters',  type=list, help=DELMITERS_HELP_MESSAGE, nargs="?", default=Hone.DEFAULT_DELIMITERS)
    parser.add_argument('csv_filepath')
    parser.add_argument('json_filepath')
    return parser.parse_args()

def main():
    args = get_args()
    hone = Hone(delimiters=args.delimiters)
    json_struct = hone.convert(args.csv_filepath)
    json_utils.output_json(json_struct, args.json_filepath)
