from scholarly import scholarly, ProxyGenerator


# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Steven A Cholewiak')

author =next(search_query)
author_filled =scholarly.fill(author) 

scholarly.pprint(author)

print(author)

# Take a closer look at the first publication
publication =author["publications"][0]
pub =  scholarly.fill(publication)

# citations= pub.citedby()
citations_iterator= scholarly.citedby(pub)
i=0
while i<100:
    i+=1
    citations = next(citations_iterator)
    with open('citedby.txt', 'w+') as file:
        print(citations, file=file)



# print(pub)


# Which papers cited that publication?
# print([citation.bib['title'] for citation in pub.citedby])

# Free Proxy
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

# TOR internal proxy
# pg = ProxyGenerator()
# pg.Tor_Internal(tor_cmd = "tor")
# scholarly.use_proxy(pg)

search_query = scholarly.search_pubs('A Survey and Classification of Security and Privacy Research in Smart Healthcare Systems')
publication = next(search_query)
# print(publication)





# try:
#     connection = psycopg2.connect(user="tomee",
#                                 #   password="",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="pfe_dataset")

#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     print(connection.get_dsn_parameters(), "\n")
#     # Print PostgreSQL version
#     cursor.execute("SELECT version();")
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")

#     create_table_query = '''
#         CREATE TABLE IF NOT EXISTS publication
#                 (	ID VARCHAR(100) PRIMARY KEY NOT NULL,
#                     abstarct TEXT,
#                     author VARCHAR(200),
#                     author_id VARCHAR(200),
#                     cites INT,
#                     eprint VARCHAR(200),
#                     gsrank INT,
#                     journal VARCHAR(100),
#                     nbr INT,
#                     pages VARCHAR(100),
#                     publisher VARCHAR(100),
#                     title VARCHAR(200),
#                     url VARCHAR(200),
#                     venue VARCHAR(200),
#                     volume VARCHAR(200),
#                     pb_year VARCHAR(200)
            
#                 );     
#     '''
#     cursor.execute(create_table_query)
#     connection.commit()
#     print("Articles Table created successfully in PostgreSQL ")


#     q = """INSERT INTO article (article_id,abstarct,author,author_id,eprint,cites,gsrank,journal,nbr,pages,publisher,title,url,venue,volume,pb_year,) 
#          VALUES(%(bib["ID"])s, %(bib["abstract"])s, %(bib["author"])s, %(author_name)"""

#     cursor.execute(q, full_publication)
#     connection.commit()

# except (Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
