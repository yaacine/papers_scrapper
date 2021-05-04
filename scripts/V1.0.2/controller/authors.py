import csv
from scholarly import scholarly, ProxyGenerator
from .keyword_manger import mark_line_as_done, get_next_keyword
from .csv_manager import write_author, insert_co_authering, get_authors_dataframe, update_authors_dataframe, update_last_scrapped_author_id_coauthoring
from datetime import datetime
import os 

# get unique time for author file name
now = datetime.now().time()  # time object
print("now =", now)

# get unique time for author file name (used when scrapping authors based on the co-authors relationship)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

fine_name_output_authors= 'authors' +str(now).replace(' ','_')+'.csv'
AUTHORS_CSV_FILE_OUTPUT =os.path.join('scripts','V1.0.2','datasets','authors', fine_name_output_authors) 
#create the file if is does not exist
os.makedirs(os.path.dirname(AUTHORS_CSV_FILE_OUTPUT), exist_ok=True)

fine_name_output_coauthors= 'authors' +str(current_time).replace(' ','_')+'.csv'
AUTHORS_CSV_FILE_OUTPUT_COAUTHORS = os.path.join('scripts','V1.0.2','datasets','authors', fine_name_output_coauthors) 
#create the file if is does not exist
os.makedirs(os.path.dirname(AUTHORS_CSV_FILE_OUTPUT_COAUTHORS), exist_ok=True)


# the file from where to start scrapping coauthering relationship
AUTHORS_CSV_FILE_INPUT_COAUTHORS = 'scripts/V1.0.2/datasets/authors/authors2021-01-11_16:32:32.669588.csv'
CO_AUTHORING_FILE = 'scripts/V1.0.2/datasets/co_authoring/coauthor4.csv'
COUNTER_CONFIG_FILE = 'scripts/V1.0.2/datasets/counter.ini'
"""
 #############################
 Extract authors from keywords
 #############################
"""


def get_author_generator_from_keyword(keyword):
    """
        This method gets a generator of the authors with a keyword
    """
    author_gen = scholarly.search_keyword(keyword)
    return author_gen


def register_authors_from_generator(author_generator):
    """
        This method goes throught the author generator and gets all
        the authors and registre them in the authors dataset
    """
    # create the file
    open(AUTHORS_CSV_FILE_OUTPUT ,'w')
    while True:
        author = next(author_generator)
        filled_author = scholarly.fill(author, ['indices'])
        mydict = filled_author_to_dict(filled_author)
        write_author(mydict, AUTHORS_CSV_FILE_OUTPUT)


def extract_authors():
    while True:
        try:
            (index, word) = get_next_keyword()
            mark_line_as_done(index)
            print("Getting authors of keyword: "+ word)
            author_generator = get_author_generator_from_keyword(word)
            register_authors_from_generator(author_generator)
        except StopIteration:
            print("Stop Iterator happened for word" + word)
            continue


"""
 #############################
 Extract authors from coauthors
 #############################
"""


def extract_coauthors():
    # TODO: define this function that goes throughout the fetched authors and gets the coauthors
    open(AUTHORS_CSV_FILE_OUTPUT_COAUTHORS,'w')
    df = get_authors_dataframe(AUTHORS_CSV_FILE_INPUT_COAUTHORS)
    for index, row in df.iterrows():
        if row['got_coauthors'] == 0:
            print("Getting co_authors of author :" + row['scholar_id'])
            df.at[index, 'got_coauthors'] = 1
            update_authors_dataframe(AUTHORS_CSV_FILE_INPUT_COAUTHORS, df)
            update_last_scrapped_author_id_coauthoring(
                COUNTER_CONFIG_FILE, row['scholar_id'])
            try:
                extract_coauthors_by_id(row['scholar_id'])
            except Exception as identifier:
                print("An exception happened while getting co-authors of : "+ row['scholar_id'])
                print(identifier)
                update_authors_dataframe(AUTHORS_CSV_FILE_INPUT_COAUTHORS, df)
    update_authors_dataframe(AUTHORS_CSV_FILE_INPUT_COAUTHORS, df)


def extract_coauthors_by_id(author_id):
    """
        extracts the co-authors of the currently existing authors in the dataset
    """
    # create the output file

    
    author = scholarly.search_author_id(author_id)
    filled_coauthors = scholarly.fill(author, ['coauthors'])

    coauthors_list = filled_coauthors['coauthors']
    for author in coauthors_list:
        filled_author = scholarly.fill(author, ['indices'])
        register_coauthering(author_id, filled_author['scholar_id'])
        print(filled_author)
        mydict = filled_author_to_dict(filled_author)
        write_author(mydict, AUTHORS_CSV_FILE_OUTPUT_COAUTHORS)


def register_coauthering(author_id1, author_id2):
    """
        register a coauthering between two authors by ids
    """
    insert_co_authering(author_id1, author_id2, CO_AUTHORING_FILE)


def filled_author_to_dict(author):
    """
        transforms a filled author object to a dict
    """

    author_dict: dict = {}

    if 'affiliation' in author.keys():
        author_dict['affiliation'] = author['affiliation']
    else:
        author_dict['affiliation'] = ''
    if 'email_domain' in author.keys():
        author_dict['email'] = author['email_domain']
    else:
        author_dict['email_domain'] = ''
    if 'citedby' in author.keys():
        author_dict['citedby'] = author['citedby']
    else:
        author_dict['citedby'] = ''
    if 'scholar_id' in author.keys():
        author_dict['scholar_id'] = author['scholar_id']
    else:
        author_dict['scholar_id'] = ''
    if 'filled' in author.keys():
        author_dict['filled'] = author['filled']
    else:
        author_dict['filled'] = ''
    if 'interests' in author.keys():
        author_dict['interests'] = ('|').join(author['interests'])
    else:
        author_dict['interests'] = ''
    if 'name' in author.keys():
        author_dict['name'] = author['name']
    else:
        author_dict['name'] = ''
    if 'url_picture' in author.keys():
        author_dict['url_picture'] = author['url_picture']
    else:
        author_dict['url_picture'] = ''
    if 'citedby5y' in author.keys():
        author_dict['citedby5y'] = author['citedby5y']
    else:
        author_dict['citedby5y'] = ''
    if 'hindex' in author.keys():
        author_dict['hindex'] = author['hindex']
    else:
        author_dict['hindex'] = ''
    if 'hindex5y' in author.keys():
        author_dict['hindex5y'] = author['hindex5y']
    else:
        author_dict['hindex5y'] = ''
    if 'i10index' in author.keys():
        author_dict['i10index'] = author['i10index']
    else:
        author_dict['i10index'] = ''
    if 'i10index5y' in author.keys():
        author_dict['i10index5y'] = author['i10index5y']
    else:
        author_dict['i10index5y'] = ''
    author_dict['got_publications'] = 0
    author_dict['got_coauthors'] = 0
    return author_dict


def check_author_exists(author_id):
    """
        Check if the author exists in the csv file 
    """
    pass


def insert_authors(author):
    """
        insert the author to the  csv file 
    """

    pass


def author_to_dict(author):
    """
        transforms an author object to a dict
    """
    author_dict: dict = {}

    if hasattr(author, 'affiliation'):
        author_dict['affiliation'] = author.affiliation
    if hasattr(author, 'email'):
        author_dict['email'] = author.email
    if hasattr(author, 'citedby'):
        author_dict['citedby'] = author.citedby
    if hasattr(author, 'id'):
        author_dict['scholar_id'] = author.id
    if hasattr(author, 'filled'):
        author_dict['filled'] = author.filled
    if hasattr(author, 'interests'):
        author_dict['interests'] = ('|').join(author.interests)
    if hasattr(author, 'name'):
        author_dict['name'] = author.name
    if hasattr(author, 'url_picture'):
        author_dict['url_picture'] = author.url_picture
    author_dict['got_publications'] = 0
    author_dict['got_coauthors'] = 0
    return author_dict
