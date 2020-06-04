import argparse
import json
from hone.hone import Hone
from hone.utils import csv_utils, json_utils

DELMITERS_HELP_MESSAGE = f"Override the default delimiters for generating a nested structure from column names. [DELIMITERS] must be a Python-compatible list of strings. The default value is {Hone.DEFAULT_DELIMITERS}."
SCHEMA_HELP_MESSAGE = "Manually specify the schema that defines the structure of the generated JSON, instead of having it automatically generated. [SCHEMA] must be a valid JSON object encoded as a string."
CSV_FILEPATH_HELP_MESSAGE = "Specify the filepath for the file to read CSV data from. To read from standard input, use a dash (\"-\") as the value"
JSON_FILEPATH_HELP_MESSAGE = "Specify the filepath for the file to output JSON data to. To write to standard output, use a dash (\"-\") as the value."

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delimiters',  type=list, help=DELMITERS_HELP_MESSAGE, nargs="?", default=Hone.DEFAULT_DELIMITERS)
    parser.add_argument('-s', '--schema',  type=json.loads, help=SCHEMA_HELP_MESSAGE, nargs="?", default=None)
    parser.add_argument('csv_filepath', type=str, help=CSV_FILEPATH_HELP_MESSAGE)
    parser.add_argument('json_filepath', type=str, help=JSON_FILEPATH_HELP_MESSAGE)
    return parser.parse_args()

def main():
    args = get_args()
    hone = Hone(delimiters=args.delimiters)
    json_struct = hone.convert(args.csv_filepath, schema=args.schema)
    json_utils.output_json(json_struct, args.json_filepath)
