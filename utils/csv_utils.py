"""
Simple methods for processing CSV files
"""

from contextlib import contextmanager

class CSVUtils:
    def __init__(self, csv_filepath):
        self.filepath = csv_filepath

    # Parses and returns first row of CSV (column names)
    def get_column_names(self):
        with self.open_csv() as f:
            cols = self.parse_row(f.readline())
        return cols

    # Returns parsed rows of CSV (excluding column names)
    def get_data_rows(self):
        data_rows = []
        with self.open_csv() as f:
            f.readline()  # discard column names
            while True:
                row = f.readline()
                if row != '':
                    data_rows.append(self.parse_row(row))
                else:
                    break
        return data_rows

    # Open CSV in given mode (default is read mode)
    @contextmanager
    def open_csv(self, mode='r'):
        f = open(self.filepath, mode, encoding='utf-8-sig')
        try:
            yield f
        finally:
            f.close()

    # Parse given row (list of cells)
    @staticmethod
    def parse_row(row):
        row = row[:-1]
        cells = []

        quote_flag = False
        split_index = 0
        i = 0

        # parse rows
        while i < len(row):
            c = row[i]
            if c == '"':
                quote_flag = not quote_flag
            elif c == ',':
                if not quote_flag:
                    cells.append(row[split_index:i])
                    split_index = i+1
            i += 1

        # add last cell in row
        if split_index != len(row)-1:
            cells.append(row[split_index:])

        cells = [cell.strip(' "') for cell in cells]
        return cells
