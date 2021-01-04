import csv
from scholarly import scholarly, ProxyGenerator
import controller.authors as author
import controller.publications as publications
# author.extract_authors()

# publications.get_papers_for_author("4Hme0r8AAAAJ")

# publications.get_papers_from_citations("Climate change 2007-the physical science basis: Working group I contribution to the fourth assessment report of the IPCC")
# author.extract_coauthors_sequencially("4Hme0r8AAAAJ")

# author.get_coauthors("8csgm4cAAAAJ")


author.extract_coauthors()
