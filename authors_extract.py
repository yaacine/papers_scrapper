import csv
from scholarly import scholarly, ProxyGenerator
import json
import psycopg2
import pandas as pd



# authors = []
# authors.append('Byung Kyu Kim') this one is done

authors = [
    #  'Michael Busch' 
    #  'Michael Busch'
    # 'Byung Kyu Kim' 
    # 'Jan Feijen',  
    # 'PWM Blom', 
    # 'Katharina Landfester',  # not found
    'Kurt Kremer', #  done partition 3
    'Qiang Fu' #  done partition 5
    'Carlo Dallapiccola', #  done partition 6
    # 'Francisco Matorras', #  done partiton 7
    # 'Haijun Yang',  # done
    # 'Martin Grunewald',  # done
    # 'Robert M Roser',  # done partition 8
    # 'Tamleek Ali Tanveer',  # done partition 9
    # 'HR Rao' , # 
    # 'stefan thor smith' ,  # done partition 12
    # 'Leroy Hood' , #  done in partition 13
    # 'Bernhard Schölkopf' , # done in partitoin 14
    # 'Ana Valeria Barros Castro' ,  # done in partition 15
    # 'Larry R Squire'  #  done in partition 16
    # 'Michael H Jones'  # done is partition 17
    # 'Henning Hermjakob'  #  done in partition 18
    # 'James C. Bezdek'  # done in partition 19
    # 'Eric Finkelstein'   # done in partition 20
    # 'Petre (Peter) Stoica'  # done in partition 21
    # 'Edmond K Kabagambe'   # done in partition 22
    # 'Stuart Kauffman'  # done in partition 23
    # 'Graesser' #  done in partition 24
    # 'Mark Handley' # done in partition 25
    #  'challal yacine' # done in partition 26
    # 'David Swofford'  # done in partition 27
    # 'Doug Soltis'
    # 'Jari Oksanen'
    # 'Paul D Ryan'
    # 'Stringer C'
    # 'Stephen M. Barnett'
    # 'David D. Breshears'



    # ## mehdi authors down ⬇️
    # # 'Prof. Dr. Hameed Ullah Khan' 
    # # 'Luis A. Nunes Amaral' 
    # # 'Nebojsa Nakicenovic' 
    # # 'Nikolaus Rajewsky' 
    # # 'Jeffrey Cohn' 
    # # 'Giovanni Santin' 
    # # 'Gerard Muyzer' 
    # # 'JP Casas' 
    # # 'Andrzej Cichocki' 
    # # 'Michael J. Black' 
    # # 'Simon B. Eickhoff' 
    # # 'James Randerson' 
    # # 'Harry J. Wang' 
    # # 'Sheldon Ross' 
    # # 'Stuart C Gordon' 
    # # 'Peter Cox' 
    # # 'Fred Hirsch' 
    # # 'Bev Law' 

    
]

csv_columns = ['id','name','email','hindex','hindex5y','i10index','i10index5y','interests','citedby','citedby5y','affiliation']
my_index = [0 ,1]
partition_str = input("Enter the partition number (mehdi should start from 1000 eg 1001,1002,1003 ...etc): ")
partition_number =int(partition_str)
counter = partition_number * 1000
# counter=5000
partition= str(round(counter/1000) ) 
csv_file = "datasets/authors/author_part"+partition_str+".csv"
all_authors_df = pd.DataFrame()

author_row= {}

for author_name in authors:
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
            writer.writeheader()

            # Retrieve the author's data, fill-in, and print
            search_query= None
            search_query = scholarly.search_author(author_name)

            author = next(search_query).fill()

            if hasattr(author, 'id'):author_row["id"]= author.id
            if hasattr(author, 'name'):author_row["name"]= author.email
            if hasattr(author, 'email'):author_row["email"]= author.email
            if hasattr(author, 'hindex'): author_row["hindex"]= author.hindex
            if hasattr(author, 'hindex5y'): author_row["hindex5y"]= author.hindex5y
            if hasattr(author, 'i10index'): author_row["i10index"]= author.i10index
            if hasattr(author, 'interests'): author_row["interests"]=  ' | '.join(author.interests)
            if hasattr(author, 'citedby'): author_row["citedby"]= author.citedby
            if hasattr(author, 'citedby5y'): author_row["citedby5y"]= author.citedby5y
            if hasattr(author, 'affiliation'): author_row["affiliation"]= author.affiliation

            writer.writerow(author_row)
            
            # with open('filled_author.txt', 'w') as file:
            #      print(filled_author, file=file)

            # with open('author.txt', 'w') as file:
            #      print(author, file=file)
            # Take a closer look at the first publication
            # pubs = author.publications
            # dict_data = []
            
            # for idx,pub in enumerate(pubs):
            #     pub_filled = pub.fill()
            #     print(pub_filled)
            #     pub_filled.bib['id']= idx+counter

            #     if hasattr(pub_filled, 'citations_link'):
            #         pub_filled.bib['citation_link']= pub_filled.citations_link

            #     if hasattr(pub_filled, 'id_citations'):
            #         pub_filled.bib['id_citations']= pub_filled.id_citations

            #     dict_data.append(pub_filled.bib)
            #     writer.writerow(pub_filled.bib)
                
    except IOError:
        print("I/O error")

