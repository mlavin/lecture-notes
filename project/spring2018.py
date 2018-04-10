"""
This assignement will walk you through gathering data for various
econmic indexes and calculating the correlation between them
using the daily returns.

The Federal Reserve Bank of St. Louis (FRED) makes various economic data
available for research: https://fred.stlouisfed.org/

Data from the site can be downloaded in various in a CSV format.
Below is the url for daily prices of contentional gasoline at New Your Harbor
(denoted by the symbol DGASNYH) from Jan 1, 2017 to Dec 31, 2017.
https://fred.stlouisfed.org/graph/fredgraph.csv?cosd=2017-01-01&coed=2017-12-31&id=DGASNYH

The data is returned in CSV (comma separated format) with the following columns:
Date, Price

The daily return is defined by:
    (P_n - P_n-1) / P_n-1
where P_n denotes the nth price and P_n-1 denotes the (n-1)th price. Here
n is ordered by date, ascending.

The function signatures for various steps of this process have been
given below. The names and parameters of these functions should not
be changed. You are free to write additional functions or classes as
needed. You are welcome to use any modules in the Python
standard library as well as NumPy, SciPy, and Matplotlib external
libraries. All code must run on Python 3.6.4.
"""


def build_request_url(symbol, start_date, end_date):
    """
    This function should take a symbol as a string
    along with the start and end dates as Python dates
    and return the FRED csv download url.
    """
    pass


def get_fred_data(url):
    """
    This function should take a url as returned by build_request_url
    and return a list of tuples with each tuple containing the
    date (as a Python date) and the price (as a float).
    """
    pass


def calculate_returns(data):
    """
    This function should take a list of tuples as returned by get_fred_data
    (date, price) and return the list of daily returns (date, return).

    Note: This list will have one less item than original list.
    """
    pass


def calculate_correlation(data):
    """
    This function should take a list containing two lists of the form
    returned by calculate_returns (list of date, return tuples) and
    return the correlation of the daily returns as defined above.
    """
    pass


def main():
    """
    This function should get the daily price data for the Dow Jows Industrial
    Average (DJIA) and the US/Euro exchange rate (DEXUSEU)
    for Jan 1, 2017 to Dec 31, 2017. Using that
    data it should calculate and print the correlation of the daily returns.
    """
    pass


if __name__ == "__main__":
    """
    When this module as run as a script it will call the main function.
    You should not modify this code.
    """
    main()
