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
        column_structure = self.generate_full_structure(column_names)
        nested_json = self.populate_structure_with_data(column_structure, data_rows)
        return json.dumps(nested_json)

    '''
    Returns dictionary with given data rows fitted to given structure.
    '''

    def populate_structure_with_data(self, column_structure, data_rows):
        return {}  # TODO

    '''
    Returns dictionary with column names mapped to final JSON path in given structure
    
    >> map_structure_to_columns(['birth day', 'birth month'], 
                                {'birth':{'day':{}, 'month':{}})
    {'birth day':'birth.day', 'birth month': 'birth.month'}
    '''

    def map_structure_to_columns(self, structure, column_names):
        mapping = {}
        for col in column_names:
            if col in structure.keys():
                mapping[col] = col
                continue
            else:
                # TODO
        return mapping



    '''
    Generate recursively-nested JSON structure from column_names.
    '''

    def generate_full_structure(self, column_names):
        structure = self.get_nested_structure(column_names)
        if len(structure) > 1:
            for k, v in structure.items():
                if v != {}:
                    structure[k] = self.generate_full_structure(v)
        return structure

    '''
    Returns structure with maximum depth = 1 based on list of column names.
    '''

    def get_nested_structure(self, column_names):
        already_visited = []
        structure = {}
        sorted(column_names)
        for c1 in column_names:
            if c1 in already_visited:
                continue
            splits = self.get_valid_splits(c1)
            for split in splits:
                nodes = {split: []}
                for c2 in column_names:
                    if c2.startswith(split):
                        if split == c2:
                            break
                        else:
                            nodes[split].append(self.get_split_suffix(split, c2))
                            if c2 not in already_visited:
                                already_visited.append(c2)
                if len(nodes[split]) > 1:
                    structure[split] = nodes[split]
                else:
                    structure[c1] = {}
            if c1 not in already_visited:  # if column_name not nested
                structure[c1] = {}
        return structure

    '''
    Returns all valid splits for a given column name
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
        return list(set(splits))

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


if __name__ == '__main__':
    control = TableNest("/tests/data/small_cats_dataset")
    print(control.get_valid_splits("birth date __date"))
    column_names = {'name', 'age (years)', 'weight (kg)', 'birth day',
                             'birth month a', 'birth month b', 'birth year', 'adopted', 'adopted_since'}
    struct = control.generate_full_structure(column_names)
    print(control.map_structure_to_columns(struct, column_names))
