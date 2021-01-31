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

publication_file_name_output = 'articles'+str(now).replace(' ', '_')+'.csv'
PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS = os.path.join(
    'scripts', 'V1.0.2', 'datasets', 'clean_articles', publication_file_name_output)
# create the file if is does not exist
print(PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS)
os.makedirs(os.path.dirname(
    PUBLICATIONS_CSV_FILE_OUTPUT_WITH_IDS), exist_ok=True)

PUBLICATIONS_CSV_FILE_INPUT = 'scripts/V1.0.2/datasets/articles/articles.csv'

ARTICLES_INPUT_FOLDER = 'scripts/V1.0.2/datasets/articles'
ARTICLES_OUTPUT_FOLDER = 'scripts/V1.0.2/datasets/clean_articles'



def get_number_pubs_authors(scholar_id):
    """
        Gets the number of publications of an author based on the dataset of the project
    """
