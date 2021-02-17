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

AUTHORS_CSV_FILE_INPUT_INTERESTS = 'scripts/V1.0.2/datasets/authors/authors20:39:17.csv'

# authors08:15:21.csv
# authors08:23:48.csv
# authors08:26:12.csv
# authors08:28:03.csv
# authors08:35:38.csv
# authors08:54:08.csv
# authors08:58:09.csv  
# authors09:08:50.csv  
# authors09:17:44.csv  
# authors09:32:01.csv  
# authors09:56:06.csv 
# authors12:46:13.csv 
# authors13:11:52.csv  
# authors13:55:51.csv 
# authors14:08:20.csv 
# authors14:52:50.csv 
# authors15:40:15.csv 
# authors15:28:07.csv 

# authors15:42:02.csv --> 1 done
# authors16:46:09.csv --> 2
# authors17:33:36.csv --> 3
# authors18:20:59.csv --> 4 done
# authors20:05:30.csv --> 5 done
# authors20:39:17.csv --> 5
# authors21:07:54.csv --> 6
# authors21:28:08.csv --> 7
# authors21:28:20.csv --> 8
# authors22:34:10.csv --> 9


def extract_interests(input_output_file):
    df = get_authors_dataframe(input_output_file)
    df = df.astype({"interests": str})
    df = df.astype({"url_picture": str})
    print("file readed successfully")
    for index, row in df.iterrows():
        print('interest====>' + str(row['interests']))
        if row['interests'] in ("", None, "nan") or pd.isna(row['interests']):
            print("Getting interests of author :" + row['scholar_id'])
            try:
                author = scholarly.search_author_id(row['scholar_id'])
                if 'interests' in author: interests = '|'.join(author['interests'])
                if 'url_picture' in author: url_picture = author['url_picture']

                df.at[index, 'interests'] = interests
                df.at[index, 'url_picture'] = url_picture
                update_authors_dataframe(input_output_file, df)
            except Exception as identifier:
                print(
                    "An exception happened while getting interests of : " + row['scholar_id'])
                df.at[index, 'interests'] = 'error'
                print(identifier.args)
                update_authors_dataframe(input_output_file, df)
            # update_authors_dataframe(input_output_file, df)


print("Started connection to tor !")

pg = ProxyGenerator()
pg.Tor_Internal(tor_cmd='tor')
scholarly.use_proxy(pg)

print("Connection to tor done successfully !")

extract_interests(AUTHORS_CSV_FILE_INPUT_INTERESTS)
