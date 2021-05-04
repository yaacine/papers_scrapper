import csv
import pandas as pd
import os
from configparser import ConfigParser

COUNTER_CONFIG_FILE="scripts/V1.0.2/datasets/counter.ini"


def write_author(author_dict, file_name):
    # os.makedirs(os.path.dirname(file_name), exist_ok=True)
    next_index = get_next_author_index(COUNTER_CONFIG_FILE)
    array_of_single_author = [author_dict]
    df = pd.DataFrame(array_of_single_author, index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_author_index(COUNTER_CONFIG_FILE)


def write_publication(publication_dict, file_name):
    # os.makedirs(os.path.dirname(file_name), exist_ok=True)
    next_index = get_next_publication_index(
        COUNTER_CONFIG_FILE)
    array_of_single_publication = [publication_dict]
    print(array_of_single_publication)
    df = pd.DataFrame(array_of_single_publication, index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_publication_index(COUNTER_CONFIG_FILE)


def write_publication_with_ids(publication_dict, file_name):
    # os.makedirs(os.path.dirname(file_name), exist_ok=True)
    next_index = get_next_clean_publication_index_ids(
        COUNTER_CONFIG_FILE)

    # get the old index of the item to reuse the same one 
    old_index = publication_dict['Unnamed: 0.1']
    del publication_dict['Unnamed: 0.1']
    array_of_single_publication = [publication_dict]


    df = pd.DataFrame(array_of_single_publication, index=[old_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_clean_publication_index_ids(COUNTER_CONFIG_FILE)




def file_has_header(filename):
    sniffer = csv.Sniffer()
    sample_bytes = 2048
    file_empty = is_file_empty(filename)
    print("empty ===> " + str(file_empty))
    if file_empty:
        return False
    else:
        try:
            has_header = sniffer.has_header(open(filename).read(sample_bytes))
        except Exception as identifier:
            has_header = True
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

def get_next_clean_publication_index_ids(config_file_name):
    """
        It gets the next index in a given csv file
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
    last_index = authorinfo["last_index_ids"]
    print(last_index)
    return int(last_index) + 1
 

def get_next_citation_index(config_file_name):
    """
        It gets the next index in a given csv file
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["CITATIONINFO"]
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


def update_last_clean_publication_index_ids(config_file_name):
    """
        It updtes the last index of the author
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
    last_index = authorinfo["last_index_ids"]
    authorinfo["last_index_ids"] = str(int(last_index) + 1)
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)


def update_last_citation_index(config_file_name):
    """
        It updtes the last index of the author
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["CITATIONINFO"]
    last_index = authorinfo["last_index"]
    authorinfo["last_index"] = str(int(last_index) + 1)
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)



def get_last_scrapped_author_id(config_file_name):
    """
        It gets the scholar id of the last author to whom the papers have beed scrapped
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
    last_scholar_id = authorinfo["last_scrapped_author_id"]
    return last_scholar_id 


def update_last_scrapped_author_id(config_file_name, author_id):
    """
        It updates the scholar id of the last author to whom the papers have beed scrapped
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["PUBLICATIONINFO"]
    last_index = authorinfo["last_scrapped_author_id"]
    authorinfo["last_scrapped_author_id"] = author_id
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)

def get_last_scrapped_author_id_coauthoring(config_file_name):
    """
        It gets the scholar id of the last author to whom co_authors have beed scrapped
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["COAUTHORINFO"]
    last_scholar_id = authorinfo["last_scrapped_author_id_coauthering"]
    return last_scholar_id 


def update_last_scrapped_author_id_coauthoring(config_file_name, author_id):
    """
        It updates the scholar id of the last author to whom the coauthors have beed scrapped
    """
    config_object = ConfigParser()
    config_object.read(config_file_name)
    authorinfo = config_object["COAUTHORINFO"]
    last_index = authorinfo["last_scrapped_author_id_coauthering"]
    authorinfo["last_scrapped_author_id_coauthering"] = author_id
    with open(config_file_name, 'w') as conf:
        config_object.write(conf)





def remove_duplicates_authors(file_name):
    df_dirty = pd.read_csv(file_name)
    df_clean = df_dirty.drop_duplicates(subset=['scholar_id'])
    df_clean.to_csv(file_name, mode='w', header=True , index= False)


def insert_co_authering(id1, id2, file_name):
    next_index = get_next_coauthor_index(COUNTER_CONFIG_FILE)
    df = pd.DataFrame([{"author_1": id1, "author_2": id2}], index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_coauthor_index(COUNTER_CONFIG_FILE)


def insert_citation(cites_id1, cites_id2, file_name):
    """
        Insert citation relationship between two papers in the citations csv file
        Args:
            cites_id1 (str) : the cites id of the cited paper
            cites_id2 (str) : the cites id of the paper that cited the other paper
    """
    next_index = get_next_citation_index(COUNTER_CONFIG_FILE)
    df = pd.DataFrame([{
        "cited_paper": cites_id1,
        "source_paper": cites_id2
    }],
                      index=[next_index])
    needs_header = not file_has_header(file_name)
    print("needs header ===> " + str(needs_header))
    df.to_csv(file_name, mode='a', header=needs_header)
    update_last_citation_index(COUNTER_CONFIG_FILE)


def get_authors_dataframe(file_name):
    df = pd.read_csv(file_name)
    return df


def update_authors_dataframe(file_name, dataframe):
    # os.remove(file_name)
    dataframe.to_csv(file_name, mode='w', header=True , index= False)


def get_publications_dataframe(file_name):
    df = pd.read_csv(file_name)
    return df


def update_publications_dataframe(file_name, dataframe):
    dataframe.to_csv(file_name, mode='w', header=True , index= False)
