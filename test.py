import csv
from scholarly import scholarly, ProxyGenerator
import json
import psycopg2

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Steven A Cholewiak')
author = next(search_query).fill()


# Take a closer look at the first publication
pubs = author.publications
dict_data = []
csv_file = "test.csv"

for pub in pubs:
    pub_filled = pub.fill()
    print(pub_filled)
    dict_data.append(pub_filled.bib)

csv_columns = ['abstract','author','cites','cites_id','journal','number','pages','publisher','title','url','volume','year']

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")