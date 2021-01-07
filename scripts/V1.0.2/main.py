import csv
from scholarly import scholarly, ProxyGenerator
import controller.authors as author
import controller.publications as pubs


# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)



# pg = ProxyGenerator() 
# pg.Tor_Internal(tor_cmd = 'tor')
# scholarly.use_proxy(pg)


# author.extract_authors()
# pubs.get_papers_for_author("4Hme0r8AAAAJ")

pubs.extract_papers_from_authors()

# pubs.get_papers_from_paper_citations("Climate change 2007-the physical science basis: Working group I contribution to the fourth assessment report of the IPCC")
# author.extract_coauthors_sequencially("4Hme0r8AAAAJ")

# author.get_coauthors("8csgm4cAAAAJ")

# author.extract_coauthors()

# pubs.extract_papers_from_authors()
