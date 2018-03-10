from utils import csv_utils


class TableNest:
    def __init__(self):
        self.delimit_chars = [' ', '_', ',']

    def tablenest(self, column_names):
        structure = self.get_nested_structure(column_names)
        if len(structure) > 1:
            for k, v in structure.items():
                if v != {}:
                    structure[k] = self.tablenest(v)
        return structure

    '''
    Returns optimal structure for nested JSON based on list of column names.
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
    control = TableNest()
    print(control.get_valid_splits("birth date __date"))
    print(control.tablenest(['name', 'age (years)', 'weight (kg)', 'birth day',
                             'birth month', 'birth year', 'adopted', 'adopted_since']))
