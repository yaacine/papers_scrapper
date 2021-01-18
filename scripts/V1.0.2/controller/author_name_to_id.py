import csv
from scholarly import scholarly, ProxyGenerator
from csv_manager import write_author, insert_co_authering, write_publication, get_authors_dataframe, update_authors_dataframe, insert_citation, get_publications_dataframe, update_publications_dataframe, update_last_scrapped_author_id
import time
from datetime import datetime
import os

# get unique time for author file name
now = datetime.now().time()  # time object
print("now =", now)

# get unique time for author file name (used when scrapping authors based on the co-authors relationship)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

publication_file_name_output = 'articles'+str(now).replace(' ', '_')+'.csv'
PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS = os.path.join(
    'scripts', 'V1.0.2', 'datasets', 'clean_articles', publication_file_name_output)
# create the file if is does not exist
print(PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS)
os.makedirs(os.path.dirname(PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS), exist_ok=True)

PUBLICATIONS_CSV_FILE_INPUT = 'scripts/V1.0.2/datasets/articles/articles3.csv'

ARTICLES_INPUT_FOLDER= 'scripts/V1.0.2/datasets/articles'
ARTICLES_OUTPUT_FOLDER= 'scripts/V1.0.2/datasets/clean_articles'

def publication_author_name_to_id(publication_row):
    """
        This method takes the old publication row and outputs the new row with the authors id array
    """
    authors_array_names = publication_row['authors'].split('|')
    authors_array_ids= []
    for author_name in authors_array_names:
        (status_code, scholar_id) = get_id_of_author(author_name)
        if status_code==0: # if success (no stopIterator happened)
            authors_array_ids.append(scholar_id)
            
        else:
            authors_array_ids.append('')
    publication_row['author_ids'] = (' | ').join(authors_array_ids)
    publication_row['got_author_ids'] = 1
    return publication_row


def get_id_of_author(author_name):
    """
        This method takes the author name [eventually clean the name] and returns his id 
    """
    status_code= 0 #  return this status code to know if the action succeeded or not 
    try:
        search_query = scholarly.search_author(author_name)
        author = next(search_query)
        scholar_id = author['scholar_id']
        status_code = 1
    except StopIteration as identifier:
        print('stopIterator while getting the id of the author : ' +author_name)
        status_code= 2
    
    return status_code, scholar_id


def get_author_ids_for_file(input_file_name):
    """
        This method takes the articles file_name as an input 
        and creates the output files that contains the ids of the authors
    """
    # create the output file
    PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS =  os.path.join(ARTICLES_OUTPUT_FOLDER, input_file_name) 
    open(PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS, 'w')

    df = get_publications_dataframe(input_file_name)
    for index, row in df.iterrows():
        if row['got_author_ids'] == 0:
            new_row = publication_author_name_to_id(row)
            df.at[index, 'got_author_ids'] = 1
            update_authors_dataframe(PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS, df)

   

def get_articles_files_list(directory_in_str):
    file_list =[]
    directory = os.fsencode(directory_in_str)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            file_list.append(filename)
            continue
        else:
            continue
    return file_list


def get_ids():
    files_list = get_articles_files_list(ARTICLES_FOLDER)
    for file in files_list:
        get_author_ids_for_file(file)
        pass