import csv

def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    return rows

def get_column_index(header, column_name):
    try:
        return header.index(column_name)
    except ValueError:
        return None

def get_fire_gdp_year_data(co2_file, gdp_file, country):
    pass

