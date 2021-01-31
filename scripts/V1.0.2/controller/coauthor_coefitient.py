import csv
from scholarly import scholarly, ProxyGenerator
from keyword_manger import mark_line_as_done, get_next_keyword
from csv_manager import write_author, insert_co_authering, get_authors_dataframe, update_authors_dataframe, update_last_scrapped_author_id_coauthoring
from datetime import datetime
import os 


# get unique time for author file name
now = datetime.now().time()  # time object
print("now =", now)

# get unique time for author file name (used when scrapping authors based on the co-authors relationship)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

author_file_name_output = 'author_nbpubs_'+str(now).replace(' ', '_')+'.csv'
AUTHORS_CSV_FILE_OUTPUT_WITH_NBPUBS = os.path.join(
    'scripts', 'V1.0.2', 'datasets','authors','authors_nbpubs', author_file_name_output)
# create the file if is does not exist
print(AUTHORS_CSV_FILE_OUTPUT_WITH_NBPUBS)
os.makedirs(os.path.dirname(
    AUTHORS_CSV_FILE_OUTPUT_WITH_NBPUBS), exist_ok=True)

PUBLICATIONS_FOLDER_INPUT = 'scripts/V1.0.2/datasets/articles/articles.csv'

ARTICLES_INPUT_FOLDER = 'scripts/V1.0.2/datasets/articles'
AUTHORS_INPUT_FOLDER = 'scripts/V1.0.2/datasets/authors'
AUTHORS_OUTPUT_FOLDER = 'scripts/V1.0.2/datasets/authors_nbpubs'



def get_number_pubs_authors(scholar_id):
    """
        Gets the number of publications of an author based on the dataset of the project
    """
    


def get_articles_files_list(directory_in_str):
    file_list = []
    directory = os.fsencode(directory_in_str)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            file_list.append(filename)
            continue
        else:
            continue
    return file_list



"""
### the following seciton adds the missing columns to the publications csv files
"""


def add_columns_to_authors():
    files_list = get_authors_files_list(AUTHORS_INPUT_FOLDER)
    for file in files_list:
        add_columns_to_publications_file(file)


def add_columns_to_author_file(file_name):
    file_path = os.path.join(AUTHORS_INPUT_FOLDER, file_name)
    df = pd.read_csv(file_path)
    df["nb_pubs"] = 0
    df.to_csv(file_path, index=False)


add_columns_to_authors()