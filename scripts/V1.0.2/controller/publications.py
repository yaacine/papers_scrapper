import csv
from scholarly import scholarly, ProxyGenerator
from .keyword_manger import mark_line_as_done, get_next_keyword
from .csv_manager import write_author, insert_co_authering, write_publication, get_authors_dataframe, update_authors_dataframe, insert_citation, get_publications_dataframe, update_publications_dataframe, update_last_scrapped_author_id
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
PUBLICATIONS_CSV_FILE_OUTPUT = ""
PUBLICATIONS_CSV_FILE_OUTPUT = os.path.join(
    'scripts', 'V1.0.2', 'datasets', 'articles', publication_file_name_output)
# create the file if is does not exist
print(PUBLICATIONS_CSV_FILE_OUTPUT)
os.makedirs(os.path.dirname(PUBLICATIONS_CSV_FILE_OUTPUT), exist_ok=True)

print('file created')

PUBLICATIONS_CSV_FILE_INPUT = 'scripts/V1.0.2/datasets/articles/articles2.csv'
# AUTHORS_CSV_FILE = 'scripts/V1.0.2/datasets/authors/authors3.csv'
AUTHORS_CSV_FILE = 'scripts/V1.0.2/datasets/authors/authors2021-01-11_16:32:32.669588.csv'
CITATIONS_CSV_FILE = 'scripts/V1.0.2/datasets/citations/citations.csv'
COUNTER_CONFIG_FILE = "scripts/V1.0.2/datasets/counter.ini"

<<<<<<< HEAD
NB_MAX_PAPERS_PER_AUTHOR = 25
NB_MAX_CITATIONS_PER_PAPERS = 10

=======
NB_MAX_PAPERS_PER_AUTHOR = 10
NB_MAX_CITATIONS_PER_PAPERS = 25
>>>>>>> cf396f1023d6d87937ea3fc55d51622a20c48966

def get_papers_for_author(author_id):
    '''
        Gets and registers the papers of an author
    '''
    print("getting paper for author " + author_id)
    author = scholarly.search_author_id(author_id)
    filled_publications = scholarly.fill(author, ['publications'])
    publications_list = filled_publications['publications']
    nbpubs_counter = 0
    for publication in publications_list:
        filled_publication = scholarly.fill(publication)
        mydict = tiny_publication_to_dict(filled_publication)
        write_publication(mydict, PUBLICATIONS_CSV_FILE_OUTPUT)
        nbpubs_counter += 1
        print("nbpubs_counter =====>")
        print(nbpubs_counter)
        if nbpubs_counter > NB_MAX_PAPERS_PER_AUTHOR:
            break


def extract_papers_from_authors():
    open(PUBLICATIONS_CSV_FILE_OUTPUT, 'w')
    # TODO: define this function that goes throughout the fetched authors andgets the papers
    df = get_authors_dataframe(AUTHORS_CSV_FILE)
    for index, row in df.iterrows():

        if row['got_publications'] == 0:
            print("Getting publications of author : " + row['scholar_id'])
            df.at[index, 'got_publications'] = 1
            update_authors_dataframe(AUTHORS_CSV_FILE, df)
            update_last_scrapped_author_id(COUNTER_CONFIG_FILE,
                                           row['scholar_id'])
            try:
                get_papers_for_author(row['scholar_id'])
            except Exception as identifier:
                print(identifier)
                row['got_publications'] = 1
                update_authors_dataframe(AUTHORS_CSV_FILE, df)
                raise identifier
    update_authors_dataframe(AUTHORS_CSV_FILE, df)


def get_papers_from_paper_citations(paper_title: str):
    """
        gets the papers that cited the paper given as a parameter
        it registers the found papers in articles folder and registres the citation 
        relationship in the citations folder 
    """

    target_paper_generator = scholarly.search_pubs(
        paper_title)  # search by title as a keyword

    print("=======> getting the rarget pater")
    target_paper = next(target_paper_generator)  # get the first result

    print('##########################')
    publications_generator = scholarly.citedby(target_paper)
    try:
        citations_count = 0
        # while citations_count <= NB_MAX_CITATIONS_PER_PAPERS:

        publication = next(publications_generator)
        # filled_publication = scholarly.fill(publication)
        mydict = publication_to_dict(publication)
        write_publication(mydict, PUBLICATIONS_CSV_FILE_OUTPUT)
        register_citation(
            target_paper['citedby_url'], mydict['citedby_url'])
        citations_count += 1
    except Exception as e:
        raise e


def extract_papers_from_citations():
    # TODO: define this function that goes throughout the fetched authors and
    # create the file
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    publication_file_name_output = 'citations_articles' + \
        str(now).replace(' ', '_')+'.csv'
    PUBLICATIONS_CSV_FILE_OUTPUT = os.path.join(
        'scripts', 'V1.0.2', 'datasets', 'articles', publication_file_name_output)
    os.makedirs(os.path.dirname(PUBLICATIONS_CSV_FILE_OUTPUT), exist_ok=True)

    open(PUBLICATIONS_CSV_FILE_OUTPUT, 'w')

    # gets the coauthors
    df = get_publications_dataframe(PUBLICATIONS_CSV_FILE_INPUT)
    for index, row in df.iterrows():
        if row['got_citations'] == 0:
            print(row['got_citations'])
            try:
                df.at[index, 'got_citations'] = 1
                get_papers_from_paper_citations(row['title'])
                update_publications_dataframe(PUBLICATIONS_CSV_FILE_INPUT, df)
            except Exception as e:
                print("====>>>> Exception raised ")
                update_publications_dataframe(PUBLICATIONS_CSV_FILE_INPUT, df)
                raise e
    update_publications_dataframe(PUBLICATIONS_CSV_FILE_INPUT, df)


def register_citation(cited_paper, paper):
    """
        register a coauthering between two authors by ids
    """
    insert_citation(cited_paper, paper, CITATIONS_CSV_FILE)


def publication_to_dict(publication):
    publication_dict = {}
    if 'title' in publication['bib'].keys():
        publication_dict['title'] = publication['bib']['title'].replace(
            ',', '.')
    else:
        publication_dict['title'] = ''

    if 'pub_year' in publication['bib'].keys():
        publication_dict['pub_year'] = publication['bib']['pub_year']
    else:
        publication_dict['pub_year'] = ''

    if 'author' in publication['bib'].keys():
        publication_dict['author'] = publication['bib']['author']
    else:
        publication_dict['author'] = ''

    if 'author_id' in publication['bib'].keys():
        publication_dict['author_id'] = publication['bib']['author_id']
    else:
        publication_dict['author_id'] = ''

    if 'volume' in publication['bib'].keys():
        publication_dict['volume'] = publication['bib']['volume']
    else:
        publication_dict['volume'] = ''

    if 'journal' in publication['bib'].keys():
        publication_dict['journal'] = publication['bib']['journal']
    else:
        publication_dict['journal'] = ''

    if 'number' in publication['bib'].keys():
        publication_dict['number'] = publication['bib']['number']
    else:
        publication_dict['number'] = ''

    if 'pages' in publication['bib'].keys():
        publication_dict['pages'] = publication['bib']['pages']
    else:
        publication_dict['pages'] = ''

    if 'publisher' in publication['bib'].keys():
        publication_dict['publisher'] = publication['bib'][
            'publisher'].replace(',', '.')
    else:
        publication_dict['publisher'] = ''

    if 'abstract' in publication['bib'].keys():
        publication_dict['abstract'] = publication['bib']['abstract'].replace(
            ',', '.')
    else:
        publication_dict['abstract'] = ''

    if 'filled' in publication.keys():
        publication_dict['filled'] = publication['filled']
    else:
        publication_dict['filled'] = ''

    if 'author_pub_id' in publication.keys():
        publication_dict['author_pub_id'] = publication['author_pub_id']
    else:
        publication_dict['author_pub_id'] = ''

    if 'num_citations' in publication.keys():
        publication_dict['num_citations'] = publication['num_citations']
    else:
        publication_dict['num_citations'] = ''
    if 'pub_url' in publication.keys():
        publication_dict['pub_url'] = publication['pub_url']
    else:
        publication_dict['pub_url'] = ''
    if 'cites_id' in publication.keys():
        publication_dict['cites_id'] = publication['cites_id']
    else:
        publication_dict['cites_id'] = ''
    if 'citedby_url' in publication.keys():
        publication_dict['citedby_url'] = publication['citedby_url']
    else:
        publication_dict['citedby_url'] = ''
    if 'author_id' in publication.keys():
        print("###########")
        print(publication['author_id'])
        publication_dict['author_id'] = ' | '.join(publication['author_id'])
    else:
        publication_dict['author_id'] = ''
    if 'eprint_url' in publication.keys():
        publication_dict['eprint_url'] = publication['eprint_url']
    else:
        publication_dict['eprint_url'] = ''
    publication_dict['got_citations'] = 0
    publication_dict['got_author_ids'] = 0
    publication_dict['author_ids'] = 0
    # if 'cites_per_year' in publication.keys(): publication_dict['cites_per_year'] = ' | '.join('='.join((key,val)) for (key,val) in publication['cites_per_year'] )
    # else: publication_dict['cites_per_year'] =''
    return publication_dict


def tiny_publication_to_dict(publication):
    publication_dict = {}
    if 'title' in publication['bib'].keys():
        publication_dict['title'] = publication['bib']['title'].replace(
            ',', '.')
    else:
        publication_dict['title'] = ''

    if 'pub_year' in publication['bib'].keys():
        publication_dict['pub_year'] = publication['bib']['pub_year']
    else:
        publication_dict['pub_year'] = ''

    if 'author' in publication['bib'].keys():
        publication_dict['author'] = publication['bib']['author']
    else:
        publication_dict['author'] = ''

    if 'volume' in publication['bib'].keys():
        publication_dict['volume'] = publication['bib']['volume']
    else:
        publication_dict['volume'] = ''

    if 'journal' in publication['bib'].keys():
        publication_dict['journal'] = publication['bib']['journal']
    else:
        publication_dict['journal'] = ''

    if 'number' in publication['bib'].keys():
        publication_dict['number'] = publication['bib']['number']
    else:
        publication_dict['number'] = ''

    if 'pages' in publication['bib'].keys():
        publication_dict['pages'] = publication['bib']['pages']
    else:
        publication_dict['pages'] = ''

    if 'publisher' in publication['bib'].keys():
        publication_dict['publisher'] = publication['bib'][
            'publisher'].replace(',', '.')
    else:
        publication_dict['publisher'] = ''

    if 'abstract' in publication['bib'].keys():
        publication_dict['abstract'] = publication['bib']['abstract'].replace(
            ',', '.')
    else:
        publication_dict['abstract'] = ''

    if 'filled' in publication.keys():
        publication_dict['filled'] = publication['filled']
    else:
        publication_dict['filled'] = ''

    if 'author_pub_id' in publication.keys():
        publication_dict['author_pub_id'] = publication['author_pub_id']
    else:
        publication_dict['author_pub_id'] = ''

    if 'num_citations' in publication.keys():
        publication_dict['num_citations'] = publication['num_citations']
    else:
        publication_dict['num_citations'] = ''

    if 'pub_url' in publication.keys():
        publication_dict['pub_url'] = publication['pub_url']
    else:
        publication_dict['pub_url'] = ''

    if 'cites_id' in publication.keys():
        publication_dict['cites_id'] = publication['cites_id']
    else:
        publication_dict['cites_id'] = ''

    if 'citedby_url' in publication.keys():
        publication_dict['citedby_url'] = publication['citedby_url']
    else:
        publication_dict['citedby_url'] = ''

    if 'gsrank' in publication.keys():
        publication_dict['gsrank'] = publication['gsrank']
    else:
        publication_dict['gsrank'] = ''

    if 'author_id' in publication.keys():

        publication_dict['author_id'] = ' | '.join(publication['author_id'])
    else:
        publication_dict['author_id'] = ''

    if 'eprint_url' in publication.keys():
        publication_dict['eprint_url'] = publication['eprint_url']
    else:
        publication_dict['eprint_url'] = ''

    publication_dict['got_citations'] = 0
    publication_dict['got_author_ids'] = 0
    publication_dict['author_ids'] = 0
    # if 'cites_per_year' in publication.keys(): publication_dict['cites_per_year'] = ' | '.join('='.join((key,val)) for (key,val) in publication['cites_per_year'] )
    # else: publication_dict['cites_per_year'] =''
    return publication_dict
