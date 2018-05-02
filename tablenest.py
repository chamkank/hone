import json
from utils import csv_utils


class TableNest:
    def __init__(self, csv_filepath):
        self.delimit_chars = [' ', '_', ',']
        self.csv_filepath = csv_filepath
        self.csv = csv_utils.CSVUtils(self.csv_filepath)

    '''
    Returns nested JSON generated from given CSV file as string.
    '''

    def get_json_string(self):
        column_names = self.csv.get_column_names()
        data_rows = self.csv.get_data_rows()
        structure = self.generate_full_structure(column_names)
        nested_json = self.populate_structure_with_data(structure, column_names, data_rows)
        return json.dumps(nested_json)

    '''
    Perform automatic nesting
    '''
    def autonest(self):
        column_names = self.csv.get_column_names()
        data = self.csv.get_data_rows()
        column_struct = self.generate_full_structure(column_names)
        json_struct = self.populate_structure_with_data(column_struct, column_names, data)
        return json_struct
    '''
    Returns dictionary with given data rows fitted to given structure.
    '''

    def populate_structure_with_data(self, structure, column_names, data_rows):
        json_struct = []
        num_columns = len(column_names)
        mapping = self.get_leaves(structure)
        for row in data_rows:
            json_row, i = structure, 0
            while i < num_columns:
                cell = row[i]
                column_name = column_names[i]
                key_path = mapping[column_name]
                exec("json_row"+key_path+"="+"'"+cell+"'")
                i += 1
            json_struct.append(json_row)
        return json_struct
    '''
    Generate recursively-nested JSON structure from column_names.
    '''

    def generate_full_structure(self, column_names):
        visited = set()
        structure = {}
        sorted(column_names)
        column_names = column_names[::-1]
        for c1 in column_names:
            if c1 in visited:
                continue
            splits = self.get_valid_splits(c1)
            for split in splits:
                nodes = {split: {}}
                if split in column_names:
                    continue
                for c2 in column_names:
                    if c2 not in visited and self.is_valid_prefix(split, c2):
                        nodes[split][self.get_split_suffix(split, c2)] = c2
                if len(nodes[split].keys()) > 1:
                    structure[split] = self.get_nested_structure(nodes[split])
                    for val in nodes[split].values():
                        visited.add(val)
            if c1 not in visited:  # if column_name not nestable
                structure[c1] = c1
        return structure

    '''
    Generate nested JSON structure given parent structure generated from initial call to get_full_structure
    '''

    def get_nested_structure(self, parent_structure):
        column_names = list(parent_structure.keys())
        visited = set()
        structure = {}
        sorted(column_names, reverse=True)
        for c1 in column_names:
            if c1 in visited:
                continue
            splits = self.get_valid_splits(c1)
            for split in splits:
                nodes = {split: {}}
                if split in column_names:
                    continue
                for c2 in column_names:
                    if c2 not in visited and self.is_valid_prefix(split, c2):
                        nodes[split][self.get_split_suffix(split, c2)] = parent_structure[c2]
                        visited.add(c2)
                if len(nodes[split].keys()) > 1:
                    structure[split] = self.get_nested_structure(nodes[split])
            if c1 not in visited:  # if column_name not nestable
                structure[c1] = parent_structure[c1]
        return structure

    '''
    Get the leaf nodes of a nested structure and the path to those nodes.
    Ex: {"a":{"b":"c"}} => {"c":"['a']['b']"}
    '''

    def get_leaves(self, structure, path="", result={}):
        for key, value in structure.items():
            if type(value) is dict:
                self.get_leaves(value, path+"['"+key+"']", result)
            else:
                result[value] = path+"['"+key+"']"
        return result

    '''
    Merge two dictionaries and return the result.
    '''

    def merge_dictionaries(self, a, b):
        return {**a, **b}

    '''
    Returns all valid splits for a given column name in descending order by length
    '''

    def get_valid_splits(self, column_name):
        splits = []
        i = len(column_name) - 1
        while i >= 0:
            c = column_name[i]
            if c in self.delimit_chars:
                split = self.clean_split(column_name[0:i])
                splits.append(split)
            i -= 1
        return sorted(list(set(splits)), reverse=True)

    '''
    Returns string after split without delimiting characters.
    '''

    def get_split_suffix(self, split, column_name=""):
        suffix = column_name[len(split) + 1:]
        i = 0
        while i < len(suffix):
            c = suffix[i]
            if c not in self.delimit_chars:
                return suffix[i:]
            i += 1
        return suffix

    '''
    Returns split with no trailing delimiting characters.
    '''

    def clean_split(self, split):
        i = len(split) - 1
        while i >= 0:
            c = split[i]
            if c not in self.delimit_chars:
                return split[0:i + 1]
            i -= 1
        return split

    '''
    Returns true if str_a is a valid prefix of str_b
    '''

    def is_valid_prefix(self, prefix, base):
        if base.startswith(prefix):
            if base[len(prefix)] in self.delimit_chars:
                return True
        return False
