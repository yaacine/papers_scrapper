import csv
from scholarly import scholarly, ProxyGenerator
from keyword_manger import mark_line_as_done, get_next_keyword
from csv_manager import write_author, insert_co_authering, get_authors_dataframe, update_authors_dataframe, update_last_scrapped_author_id_coauthoring
from datetime import datetime
import os 




def get_number_pubs_authors(scholar_id):
    """
        Gets the number of publications of an author based on the dataset of the project
    """
