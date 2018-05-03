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
    print("Converting CSV file...")
    json_struct = hone.convert(args.csv_filepath)
    print("Saving JSON file...")
    json_utils.save_json(json_struct, args.json_filepath)
    print("Conversion complete! JSON written to", args.json_filepath)