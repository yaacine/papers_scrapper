import csv
from scholarly import scholarly, ProxyGenerator
from  .keyword_manger import mark_line_as_done , get_next_keyword
from csv_manager import *

# pg = ProxyGenerator() 
# pg.FreeProxies()
# scholarly.use_proxy(pg)


def get_author_generator_from_keyword(keyword):
    """
        This method gets a generator of the authors with a keyword
    """
    author_gen = scholarly.search_keyword(keyword)
    return author_gen


def get_list_coauthors(author_id):
    pass

def register_authors(author_generator):
    """
        This method goes throught the author generator and gets all 
        the authors and registre them in the authors dataset
    """

    while True:
        author = next(author_generator)
        print(author)
        print (type(author))
        mydict: dict = author_to_dict(author)
        
        print(mydict)
        break
    # filled_author = scholarly.fill(author)
    # print(filled_author)


def extract_authors():
    (index, word) = get_next_keyword()
    mark_line_as_done(index)
    author_generator = get_author_generator_from_keyword(word)
    register_authors(author_generator)
    


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


def get_coauthors(author_id):
    """
        get the list of coauthors of a given author by id 
    """
    pass


def author_to_dict(author):
    """
        transforms an author object to a dict
    """
    author_dict: dict ={}
    if hasattr(author, 'affiliation'): author_dict['affiliation'] = author.affiliation
    if hasattr(author, 'email'): author_dict['email'] = author.email
    if hasattr(author, 'citedby'): author_dict['citedby'] = author.citedby
    if hasattr(author, 'id'): author_dict['id'] = author.id
    if hasattr(author, 'filled'): author_dict['filled'] = author.filled
    if hasattr(author, 'interests'): author_dict['interests'] = ('|').join(author.interests)
    if hasattr(author, 'name'): author_dict['name'] = author.name
    if hasattr(author, 'url_picture'): author_dict['url_picture'] = author.url_picture

    return author_dict



def filled_author_to_dict(author):
    """
        transforms a filled author object to a dict
    """