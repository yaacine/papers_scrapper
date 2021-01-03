import csv
from scholarly import scholarly, ProxyGenerator
from  .keyword_manger import mark_line_as_done , get_next_keyword
from .csv_manager import write_author, insert_co_authering

# pg = ProxyGenerator() 
# pg.FreeProxies()
# scholarly.use_proxy(pg)

AUTHORS_CSV_FILE= 'scripts/V1.0.2/datasets/articles/authors2.csv'
CO_AUTHORING_FILE= 'scripts/V1.0.2/datasets/co_authoring/coauthor.csv'
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
    while True:
        author = next(author_generator)
        filled_author = scholarly.fill(author, ['indices'])
        mydict = filled_author_to_dict(filled_author)
        write_author(mydict , AUTHORS_CSV_FILE)



def extract_authors():
    (index, word) = get_next_keyword()
    mark_line_as_done(index)
    author_generator = get_author_generator_from_keyword(word)
    register_authors_from_generator(author_generator)
    




def extract_coauthors_sequencially(author_id):
    """
        extracts the co-authors of the currently existing authors in the dataset
    """
    author = scholarly.search_author_id(author_id)
    filled_coauthors =  scholarly.fill(author , ['coauthors']) 
    
    coauthors_list = filled_coauthors['coauthors']
    for author in coauthors_list:
        filled_author = scholarly.fill(author, ['indices'])
        register_coauthering(author_id , filled_author['scholar_id'])
        print(filled_author)
        mydict = filled_author_to_dict(filled_author)
        write_author(mydict , AUTHORS_CSV_FILE)
        




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


def register_coauthering(author_id1, author_id2):
    """
        register a coauthering between two authors by ids
    """
    insert_co_authering(author_id1, author_id2,CO_AUTHORING_FILE )
    


def author_to_dict(author):
    """
        transforms an author object to a dict
    """
    author_dict: dict ={}
    
    if hasattr(author, 'affiliation'): author_dict['affiliation'] = author.affiliation
    if hasattr(author, 'email'): author_dict['email'] = author.email
    if hasattr(author, 'citedby'): author_dict['citedby'] = author.citedby
    if hasattr(author, 'id'): author_dict['scholar_id'] = author.id
    if hasattr(author, 'filled'): author_dict['filled'] = author.filled
    if hasattr(author, 'interests'): author_dict['interests'] = ('|').join(author.interests)
    if hasattr(author, 'name'): author_dict['name'] = author.name
    if hasattr(author, 'url_picture'): author_dict['url_picture'] = author.url_picture
    author_dict['got_publications'] = 0
    author_dict['got_coauthors']= 0 
    return author_dict



def filled_author_to_dict(author):
    """
        transforms a filled author object to a dict
    """

    author_dict: dict ={}

    if 'affiliation' in author.keys(): author_dict['affiliation'] = author['affiliation'] 
    else: author_dict['affiliation'] =''
    if 'email_domain' in author.keys(): author_dict['email'] = author['email_domain']  
    else: author_dict['email_domain'] =''
    if 'citedby' in author.keys(): author_dict['citedby'] = author['citedby']  
    else: author_dict['citedby'] =''
    if 'scholar_id' in author.keys(): author_dict['scholar_id'] = author['scholar_id']  
    else: author_dict['scholar_id'] =''
    if 'filled' in author.keys(): author_dict['filled'] = author['filled'] 
    else: author_dict['filled'] =''
    if 'interests' in author.keys(): author_dict['interests'] = ('|').join(author['interests']) 
    else: author_dict['interests'] =''
    if 'name' in author.keys(): author_dict['name'] = author['name'] 
    else: author_dict['name'] =''
    if 'url_picture' in author.keys(): author_dict['url_picture'] = author['url_picture'] 
    else: author_dict['url_picture'] =''
    if 'citedby5y' in author.keys(): author_dict['citedby5y'] = author['citedby5y'] 
    else: author_dict['citedby5y'] =''
    if 'hindex' in author.keys(): author_dict['hindex'] = author['hindex'] 
    else: author_dict['hindex'] =''
    if 'hindex5y' in author.keys(): author_dict['hindex5y'] = author['hindex5y'] 
    else: author_dict['hindex5y'] =''
    if 'i10index' in author.keys(): author_dict['i10index'] = author['i10index'] 
    else: author_dict['i10index'] =''
    if 'i10index5y' in author.keys(): author_dict['i10index5y'] = author['i10index5y']
    else: author_dict['i10index5y'] =''
    author_dict['got_publications'] = 0
    author_dict['got_coauthors']= 0 
    return author_dict
