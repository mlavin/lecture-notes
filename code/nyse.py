import csv


def nyse():
    with open('nyse.csv') as f:
        yield from csv.DictReader(f)
