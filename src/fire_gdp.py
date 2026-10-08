import csv

def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)

    if query_column is not None and query_value is not None:
        column_index = get_column_index(header, query_column)
        rows = [row for row in rows if row[column_index] == query_value]

    if return_header:
        return header, rows
    return rows

def get_column_index(header, column_name):
    try:
        return header.index(column_name)
    except ValueError:
        return None

def get_fire_gdp_year_data(co2_file, gdp_file, country):
    co2_header, co2_rows = get_data(
        co2_file,
        query_column="Area",
        query_value=country,
        return_header=True
    )

    gdp_header, gdp_rows = get_data(
        gdp_file,
        query_column="Country",
        query_value=country,
        return_header=True
    )

    fire_index = get_column_index(co2_header, "Forest fires")
    results = []

    for row in co2_rows:
        year = row[get_column_index(co2_header, "Year")]
        fire = row[fire_index]

        if fire == "":
            continue

        if year not in gdp_header:
            continue

        gdp_index = get_column_index(gdp_header, year)
        gdp = gdp_rows[0][gdp_index]

        if gdp == "":
            continue

        results.append([
            int(year),
            float(fire),
            float(gdp)
        ])

    return results
