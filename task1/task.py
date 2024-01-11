import csv
import json
import argparse
from jsonpath_ng import parse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name_of_def', type=str, choices=['csv', 'json'], help='Input name of def (csv or json)')
    parser.add_argument('value', nargs='+', type=str, help='Input row/column number or JSONPath example - $.str.str1')
    args = parser.parse_args()
    return args


def csv_reader(row, column):
    filename = "example.csv"
    f = open(filename, 'r')
    csv_file = csv.reader(f)
    csv_table = [[item for item in line] for line in csv_file]
    return csv_table[row][column]


def json_reader(jpath):
    filename = 'example.json'
    f = open(filename, 'r')
    json_data = json.load(f)
    jsonpath_expression = parse(jpath)
    match = jsonpath_expression.find(json_data)
    return match[0].value


def main():
    args = arg_parser()
    if args.name_of_def == 'csv':
        row, column = map(int, args.value)
        print(csv_reader(row, column))
    else:
        jpath = args.value[0]
        print(json_reader(jpath))


if __name__ == "__main__":
    main()
