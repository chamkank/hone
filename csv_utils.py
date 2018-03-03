"""
Simple methods for processing CSV files
"""


class CSVUtils:
    def __init__(self, csv_filepath):
        self.filepath = csv_filepath

    def get_column_names(self):
        f = open(self.filepath, 'r')
        cols = self.parse_row(f.readline())
        f.close()
        return cols

    def get_data_rows(self):
        data_rows = []
        f = open(self.filepath, 'r')
        row = f.readline()
        while True:
            row = f.readline()
            if row != '':
                data_rows += self.parse_row(f.readline())
            else:
                break
        f.close()
        return data_rows[:-1]

    @staticmethod
    def parse_row(row):
        row = row[:-1].split(',')
        cells = [cell.strip(' ') for cell in row]
        return cells
