import csv
from scholarly import scholarly, ProxyGenerator
import controller.authors as author
import controller.publications as pubs
import sys


print("Started connection to tor !")

# pg = ProxyGenerator()
# pg.Tor_Internal(tor_cmd='tor')
# scholarly.use_proxy(pg)


import time
from datetime import datetime
import os 

# get unique time for author file name
now = datetime.now().time() # time object
print("now =", now)

# get unique time for author file name (used when scrapping authors based on the co-authors relationship)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

publication_file_name_output='articles'+str(now).replace(' ','_')+'.csv'
PUBLICATIONS_CSV_FILE_OUTPUT =os.path.join('scripts','V1.0.2','datasets','articles', publication_file_name_output) 
#create the file if is does not exist
print(PUBLICATIONS_CSV_FILE_OUTPUT)
print(os.path.dirname(PUBLICATIONS_CSV_FILE_OUTPUT))
os.makedirs(os.path.dirname(PUBLICATIONS_CSV_FILE_OUTPUT), exist_ok=True)
print('file created')


print("Connection to tor done successfully !")


# if (len(sys.argv) < 2):
#     # TODO: replace this print with Exception
#     print("Number of argument is wrong")
# else:
#     scrap_type = sys.argv[1]
#     if scrap_type == "author":
#         author.extract_authors()
#     elif scrap_type == "coauthor":
#         author.extract_coauthors()
#     elif scrap_type == "publication":
#         pubs.extract_papers_from_authors()
#     elif scrap_type == "citation":
#         pubs.extract_papers_from_citations()
#     else:
#         # TODO: replace this print with Exception
#         print("Wrong parameter")


# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)



# # author.extract_authors()
# print("hello")
# pubs.extract_papers_from_authors()
# print("salam")
# # author.extract_coauthors()
