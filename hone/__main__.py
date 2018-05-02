import argparse
from hone.hone import Hone, get_args
from hone.utils import csv_utils, json_utils

def main():
    args = get_args()
    hone = Hone()
    print("Converting CSV file...")
    json_struct = hone.convert(args.csv_filepath)
    print("Saving JSON file...")
    json_utils.save_json(json_struct, args.json_filepath)
    print("Conversion complete! JSON written to", args.json_filepath)

main()