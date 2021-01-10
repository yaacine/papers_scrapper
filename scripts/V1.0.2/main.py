import csv
from scholarly import scholarly, ProxyGenerator
import controller.authors as author
import controller.publications as pubs
import sys


print("Started connection to tor !")

pg = ProxyGenerator()
pg.Tor_Internal(tor_cmd='tor')
scholarly.use_proxy(pg)



print("Connection to tor done successfully !")


if (len(sys.argv) < 2):
    # TODO: replace this print with Exception
    print("Number of argument is wrong")
else:
    scrap_type = sys.argv[1]
    if scrap_type == "author":
        author.extract_authors()
    elif scrap_type == "coauthor":
        author.extract_coauthors()
    elif scrap_type == "publication":
        pubs.extract_papers_from_authors()
    elif scrap_type == "citation":
        pubs.extract_papers_from_citations()
    else:
        # TODO: replace this print with Exception
        print("Wrong parameter")


# # pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)
