import argparse
import duckdb

ADVISORS_FILE_LOCATION = "./input_data/advisors.csv"
COMMODITIES_FILE_LOCATION = "./input_data/commodities.csv"
COUNTRIES_FILE_LOCATION = "./input_data/countries.csv"
EXPORT_WINS_FILE_LOCATION = "./input_data/export_wins.csv"

OUTPUT_DIRECTORY = "./output/most_valuable_export_wins.csv"


def load_and_query_data(top: int):
    advisors = duckdb.read_csv(ADVISORS_FILE_LOCATION)
    commodities = duckdb.read_csv(COMMODITIES_FILE_LOCATION)
    countries = duckdb.read_csv(COUNTRIES_FILE_LOCATION)
    export_wins = duckdb.read_csv(EXPORT_WINS_FILE_LOCATION)

    get_most_valuable_export_wins(export_wins)


def get_most_valuable_export_wins(export_wins):
    sql = "SELECT * FROM export_wins"
    return duckdb.sql(sql).show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--top', required=False, default=3)
    args = vars(parser.parse_args())

    load_and_query_data(args['top'])
