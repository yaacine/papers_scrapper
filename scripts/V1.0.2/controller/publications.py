import csv
from scholarly import scholarly, ProxyGenerator
from .keyword_manger import mark_line_as_done, get_next_keyword
from .csv_manager import  write_author, insert_co_authering, write_publication, get_authors_dataframe, update_authors_dataframe, insert_citation , get_publications_dataframe, update_publications_dataframe

PUBLICATIONS_CSV_FILE = 'scripts/V1.0.2/datasets/articles/articles2.csv'
AUTHORS_CSV_FILE = 'scripts/V1.0.2/datasets/authors/authors.csv'
CITATIONS_CSV_FILE = 'scripts/V1.0.2/datasets/citations/citations.csv'

# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)


def get_papers_for_author(author_id):
    author = scholarly.search_author_id(author_id)
    filled_publications = scholarly.fill(author, ['publications'])

    publications_list = filled_publications['publications']
    print("TYPE  =>>>")
    print(type(publications_list))

    for publication in publications_list:
        scholarly.pprint(publication)
        filled_publication = scholarly.fill(publication)
        # register_coauthering(author_id , filled_author['scholar_id'])
        print(filled_publication)
        print(type(filled_publication))
        mydict = publication_to_dict(filled_publication)
        print('dictionary ===>')
        print(mydict)
        write_publication(mydict, PUBLICATIONS_CSV_FILE)


def extract_papers_from_authors():
    # TODO: define this function that goes throughout the fetched authors and
    # gets the coauthors
    df = get_authors_dataframe(AUTHORS_CSV_FILE)
    for index, row in df.iterrows():
        if row['got_publications'] == 0:
            print(row['got_publications'])
            try:
                get_papers_for_author(row['scholar_id'])
            except Exception as identifier:
                row['got_publications'] = 1               
                update_authors_dataframe(df)
    row['got_publications'] = 1               
    update_authors_dataframe(df)


def get_papers_from_paper_citations(paper_title: str):
    """
        gets the papers that cited the paper given as a parameter
        it registers the found papers in articles folder and registres the citation 
        relationship in the citations folder 
    """
    target_paper_generator = scholarly.search_pubs(paper_title)     # search by title as a keyword
    target_paper = next(target_paper_generator)     # get the first result
    print(target_paper)
    print('##########################')
    publications_generator = scholarly.citedby(target_paper)
    while True:
        publication = next(publications_generator)
        filled_publication = scholarly.fill(publication)
        mydict = publication_to_dict(filled_publication)
        print('dictionary ===>')
        print(mydict)
        write_publication(mydict, PUBLICATIONS_CSV_FILE)
        print("=====>target")
        print(target_paper['citedby_url'] )
        print("=====>sourcce")
        print(mydict['citedby_url'])
        register_citation(target_paper['citedby_url'] , mydict['citedby_url'])

        break
    pass



def extract_papers_from_citations():
    # TODO: define this function that goes throughout the fetched authors and
    # gets the coauthors
    df = get_publications_dataframe(PUBLICATIONS_CSV_FILE)
    for index, row in df.iterrows():
        if row['got_citations'] == 0:
            print(row['got_citations'])
            get_papers_from_paper_citations(row['title'])
            row['got_citations'] = 1
    update_publications_dataframe(df)

def register_citation(cited_paper, paper):
    """
        register a coauthering between two authors by ids
    """
    insert_citation(cited_paper, paper,CITATIONS_CSV_FILE )
    


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
        publication_dict['publisher'] = publication['bib']['publisher'].replace(
            ',', '.')
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
        publication_dict['author_id'] = ' | '.join(publication['author_id'])
    else:
        publication_dict['author_id'] = ''
    if 'eprint_url' in publication.keys():
        publication_dict['eprint_url'] = publication['eprint_url']
    else:
        publication_dict['eprint_url'] = ''
    publication_dict['got_citations'] = 0
    # if 'cites_per_year' in publication.keys(): publication_dict['cites_per_year'] = ' | '.join('='.join((key,val)) for (key,val) in publication['cites_per_year'] )
    # else: publication_dict['cites_per_year'] =''
    return publication_dict
