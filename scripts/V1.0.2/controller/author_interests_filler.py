import csv
from scholarly import scholarly, ProxyGenerator
from keyword_manger import mark_line_as_done, get_next_keyword
from csv_manager import write_author, insert_co_authering, get_authors_dataframe, update_authors_dataframe, update_last_scrapped_author_id_coauthoring
from datetime import datetime
import os
import pandas as pd

"""
 #############################
 Extract the interests of the authors
 #############################
"""

AUTHORS_CSV_FILE_INPUT_INTERESTS = 'scripts/V1.0.2/datasets/authors/authors06:36:25.csv'

def extract_interests(input_output_file):
    df = get_authors_dataframe(input_output_file)
    print("file readed successfully")
    for index, row in df.iterrows():
        print('interest====>'+  str(row['interests']))
        if row['interests'] in ("", None) or pd.isna(row['interests']):
            print("Getting interests of author :" + row['scholar_id'])
            try:
                author = scholarly.search_author_id(row['scholar_id'])
                interests = '|'.join(author['interests'])
                print ("new interests ====>" + str(interests))
                #convert the type of interests into str
                df= df.astype({"interests": str})
                df.at[index, 'interests'] = interests
                print("new author line ====>" )
                print(df.at[index])
                update_authors_dataframe(input_output_file, df)
            except Exception as identifier:
                print(
                    "An exception happened while getting interests of : " + row['scholar_id'])
                print(identifier)
                update_authors_dataframe(input_output_file, df)
            update_authors_dataframe(input_output_file, df)


print("Started connection to tor !")

# pg = ProxyGenerator()
# pg.Tor_Internal(tor_cmd='tor')
# scholarly.use_proxy(pg)

print("Connection to tor done successfully !")

extract_interests(AUTHORS_CSV_FILE_INPUT_INTERESTS)