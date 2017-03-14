"""I am a file."""


from urllib.request import urlretrieve
import os


def download_if_needed(url, filename, force_download=False):
    """Download url to filename if filename does not exist"""

    if force_download or not os.path.exists(filename):
        print("Downloading file from {0} to {1}".format(url, filename))
        urlretrieve(url, filename)
    else:
        print("File {0} already exists; not downloading".format(filename))


def get_year_data(df, column_with_year, year):
    """Select data from a specified year from a dataframe."""

    if df.dtypes[column_with_year] == 'datetime64[ns]':
        return df[df.column_with_year.dt.year == year]
    else:
        print("Column with year is not a datetime64 object.")
