import csv

INVALID_STRING = 'n/a'


def get_symbol_info(filename):
    data = []
    with open(filename) as ticker_file:
        reader = csv.DictReader(ticker_file)
        for row in reader:
            symbol = row.get('Symbol', None)
            sector = row.get('Sector', None)
            industry = row.get('Industry', None)
            if (all([symbol, sector, industry]) and
                    sector != INVALID_STRING and
                    industry != INVALID_STRING):
                data.append((symbol, sector, industry))
    return data


def filter_by_industry(data, industry):
    return [x for x in data if x[2] == industry]


if __name__ == '__main__':
    symbols = get_symbol_info('nyse.csv')
    banks = filter_by_industry(symbols, 'Commercial Banks')
    print(len(banks))
