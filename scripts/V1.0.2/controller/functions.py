import csv
from scholarly import scholarly, ProxyGenerator


def get_author_generator_from_keyword(keyword):
    scholarly.search_keyword