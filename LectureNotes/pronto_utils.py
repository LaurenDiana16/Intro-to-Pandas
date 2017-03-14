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
