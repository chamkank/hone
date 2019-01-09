"""
Simple methods for processing CSV files
"""

from contextlib import contextmanager
import re

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

    def data_type_check(self, cell_data,column_names):
        # return data type, only checks for accountID, integer or string, boolean could be added
        accountid = re.compile("^[0-9]{12}$")
        number = re.compile("^\d+$")
        row = 0
        col = 0
        cell_type = []
        inner_array = []

        while row < len(cell_data):
            while col < (len(column_names)):
                if accountid.match(cell_data[row][col]):
                    inner_array.append('string')
                else:
                    if number.match(cell_data[row][col]):
                        inner_array.append('integer')
                    else:
                        inner_array.append('string')
                col += 1
            cell_type.append(inner_array)
            row += 1
        return cell_type

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
        if split_index != len(row):
            cells.append(row[split_index:])

        cells = [cell.strip(' "') for cell in cells]
        return cells
