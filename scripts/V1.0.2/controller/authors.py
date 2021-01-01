import csv
from scholarly import scholarly, ProxyGenerator
from  .keyword_manger import mark_line_as_done , get_next_keyword


pg = ProxyGenerator() 
pg.FreeProxies()
scholarly.use_proxy(pg)


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

    # filled_author = scholarly.fill(author)
    # print(filled_author)


def extract_authors():
    (index, word) = get_next_keyword()
    mark_line_as_done(index)
    author_generator = get_author_generator_from_keyword(word)
    register_authors(author_generator)

