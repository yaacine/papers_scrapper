import csv
from scholarly import scholarly, ProxyGenerator
import json
import psycopg2


# authors = []
# authors.append('Byung Kyu Kim') this one is done

authors = [
    'Antti Rajala', 
    'Nancy Worth', 
    'Mubarek Tamiru Gemtessa', 
    'Muhammad Ikram (M.Ikram), Ph.D.',
    'Federico Flego',
    'Ronald C Kessler',
    'Tom Maniatis',
    'Dr. JoAnn E. Manson'
]
csv_columns = ['id','abstract','author','cites','cites_id','journal','number','pages','publisher','title','url','volume','year']
csv_file = "datasets/articles_part10.csv"
counter=100000
for author_name in authors:
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
            writer.writeheader()

            # Retrieve the author's data, fill-in, and print
            search_query = scholarly.search_author(author_name)
            author = next(search_query).fill()

            # Take a closer look at the first publication
            pubs = author.publications
            dict_data = []
            
            for idx,pub in enumerate(pubs):
                pub_filled = pub.fill()
                print(pub_filled)
                pub_filled.bib['id']= idx
                dict_data.append(pub_filled.bib)
                writer.writerow(pub_filled.bib)
                counter += counter
                
    except IOError:
        print("I/O error")
        
    

  
    
