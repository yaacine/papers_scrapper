import csv
from scholarly import scholarly, ProxyGenerator
from .keyword_manger import mark_line_as_done, get_next_keyword
from .csv_manager import write_author, insert_co_authering, write_publication


PUBLICATIONS_CSV_FILE = 'scripts/V1.0.2/datasets/articles/articles.csv'


def get_papers_for_author(author_id):
    author = scholarly.search_author_id(author_id)
    filled_publications =  scholarly.fill(author , ['publications']) 
    
    publications_list = filled_publications['publications']
    print("TYPE  =>>>")
    print (type(publications_list))
   
    for publication in publications_list:
        scholarly.pprint(publication)
        filled_publication = scholarly.fill(publication)
        # register_coauthering(author_id , filled_author['scholar_id'])
        print(filled_publication)
        print(type(filled_publication))
        mydict = publication_to_dict(filled_publication)
        print('dictionary ===>')
        print (mydict)
        write_publication(mydict, PUBLICATIONS_CSV_FILE)


        break


def publication_to_dict(publication):
    publication_dict= {}
    if 'title' in publication['bib'].keys(): publication_dict['title'] = publication['bib']['title'] 
    else: publication_dict['title'] =''
    if 'pub_year' in publication['bib'].keys(): publication_dict['pub_year'] = publication['bib']['pub_year'] 
    else: publication_dict['pub_year'] =''
    if 'author' in publication['bib'].keys(): publication_dict['author'] = publication['bib']['author'] 
    else: publication_dict['author'] =''
    if 'volume' in publication['bib'].keys(): publication_dict['volume'] = publication['bib']['volume'] 
    else: publication_dict['volume'] =''
    if 'publisher' in publication['bib'].keys(): publication_dict['publisher'] = publication['bib']['publisher'] 
    else: publication_dict['publisher'] =''
    if 'abstract' in publication['bib'].keys(): publication_dict['abstract'] = publication['bib']['abstract'] 
    else: publication_dict['abstract'] =''
    if 'filled' in publication.keys(): publication_dict['filled'] = publication['filled'] 
    else: publication_dict['filled'] =''
    if 'author_pub_id' in publication.keys(): publication_dict['author_pub_id'] = publication['author_pub_id'] 
    else: publication_dict['author_pub_id'] =''
    if 'num_citations' in publication.keys(): publication_dict['num_citations'] = publication['num_citations'] 
    else: publication_dict['num_citations'] =''
    if 'pub_url' in publication.keys(): publication_dict['pub_url'] = publication['pub_url'] 
    else: publication_dict['pub_url'] =''
    if 'cites_id' in publication.keys(): publication_dict['cites_id'] = publication['cites_id'] 
    else: publication_dict['cites_id'] =''
    if 'citedby_url' in publication.keys(): publication_dict['citedby_url'] = publication['citedby_url'] 
    else: publication_dict['citedby_url'] =''
    if 'eprint_url' in publication.keys(): publication_dict['eprint_url'] = publication['eprint_url'] 
    else: publication_dict['eprint_url'] =''
    # if 'cites_per_year' in publication.keys(): publication_dict['cites_per_year'] = ' | '.join('='.join((key,val)) for (key,val) in publication['cites_per_year'] ) 
    # else: publication_dict['cites_per_year'] =''
    return publication_dict