import csv
import pandas as pd
import os
from configparser import ConfigParser


def write_author(author_dict, file_name):
    # os.makedirs(os.path.dirname(file_name), exist_ok=True)
    next_index = get_next_author_index("scripts/V1.0.2/datasets/counter.ini")
    array_of_single_author = [author_dict]
    df = pd.DataFrame(array_of_single_author, index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_author_index("scripts/V1.0.2/datasets/counter.ini")


def write_publication(publication_dict, file_name):
    # os.makedirs(os.path.dirname(file_name), exist_ok=True)
    next_index = get_next_publication_index("scripts/V1.0.2/datasets/counter.ini")
    array_of_single_publication = [publication_dict]
    df = pd.DataFrame(array_of_single_publication, index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_publication_index("scripts/V1.0.2/datasets/counter.ini")

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


def get_next_coauthor_index(config_file_name):
    """
        It gets the next index in a given csv file
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["COAUTHORINFO"]
    last_index = authorinfo["last_index"]
    print(last_index)
    return int(last_index) + 1

def get_next_publication_index(config_file_name):
    """
        It gets the next index in a given csv file
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
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


def update_last_coauthor_index(config_file_name):
    """
        It updtes the last index of the author
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["COAUTHORINFO"]
    last_index = authorinfo["last_index"]
    authorinfo["last_index"] = str(int(last_index) + 1)
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)

def update_last_publication_index(config_file_name):
    """
        It updtes the last index of the author
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
    last_index = authorinfo["last_index"]
    authorinfo["last_index"] = str(int(last_index) + 1)
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)


def remove_duplicates_authors(file_name):
    df_dirty = pd.read_csv(file_name)
    df_clean = df_dirty.drop_duplicates(subset=['scholar_id'])


def insert_co_authering(id1, id2, file_name):
    next_index = get_next_coauthor_index("scripts/V1.0.2/datasets/counter.ini")
    df = pd.DataFrame([{"author_1": id1, "author_2": id2}], index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_coauthor_index("scripts/V1.0.2/datasets/counter.ini")
