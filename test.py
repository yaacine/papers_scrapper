import csv
from scholarly import scholarly, ProxyGenerator
import json
import psycopg2


authors = []
authors.append('Byung Kyu Kim')
authors.append('Steven A Cholewiak')
authors.append('Jan Feijen')
authors.append('PWM Blom')
authors.append('Katharina Landfester')
authors.append('Kurt Kremer')
authors.append('Qiang Fu')

csv_columns = ['id','abstract','author','cites','cites_id','journal','number','pages','publisher','title','url','volume','year']
csv_file = "Articles.csv"
counter=0
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
        
    

  
    
