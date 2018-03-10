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
        f.readline()  # discard column names
        while True:
            row = f.readline()
            if row != '':
                data_rows.append(self.parse_row(row))
            else:
                break
        f.close()
        return data_rows

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


if __name__ == '__main__':
    csv = CSVUtils("worldbank.csv")
    print(csv.get_column_names())
    print(csv.get_data_rows())
