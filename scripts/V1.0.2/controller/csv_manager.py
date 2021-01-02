import csv
import pandas as pd
import os
from configparser import ConfigParser


def write_author(author_dict, file_name):
    next_index = get_next_author_index("scripts/V1.0.2/datasets/counter.ini")
    df = pd.DataFrame(author_dict, index=[next_index])
    # df.append(new_row, ignore_index=True)
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_author_index("scripts/V1.0.2/datasets/counter.ini")


def file_has_header(filename):
    sniffer = csv.Sniffer()
    sample_bytes = 1024
    file_empty = is_file_empty(filename)
    print("empty ===> " + str(file_empty))
    if file_empty:
        return False
    else:
        has_header = sniffer.has_header(open(filename).read(sample_bytes))
        return has_header


def is_file_empty(file_path):
    """ 
        Check if file is empty by confirming if its size is 0 bytes
    """
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0


def get_next_author_index(config_file_name):
    """
        It gets the next index in a given csv file 
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["AUTHORINFO"]
    last_index = authorinfo["last_index"]
    print(last_index)
    return int(last_index) + 1


def update_last_author_index(config_file_name):
    """
        It updtes the last index of the author 
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["AUTHORINFO"]
    last_index = authorinfo["last_index"]
    authorinfo["last_index"] = str(int(last_index) + 1)
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)
