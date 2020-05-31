import argparse
from hone.hone import Hone
from hone.utils import csv_utils, json_utils


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_filepath')
    parser.add_argument('json_filepath')
    return parser.parse_args()

def main():
    args = get_args()
    hone = Hone()
    json_struct = hone.convert(args.csv_filepath)
    json_utils.output_json(json_struct, args.json_filepath)
