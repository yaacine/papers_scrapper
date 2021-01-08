import csv
from scholarly import scholarly, ProxyGenerator
import controller.authors as author
import controller.publications as pubs


# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)



pg = ProxyGenerator() 
pg.Tor_Internal(tor_cmd = 'tor')
scholarly.use_proxy(pg)


# author.extract_authors()
print("hello")
pubs.extract_papers_from_authors()
print("salam")
# author.extract_coauthors()


