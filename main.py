from scholarly import scholarly
import json
import psycopg2

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Steven A Cholewiak')
author = next(search_query).fill()
# json_result= json.dumps(author)
# print(json_result)

# # Print the titles of the author's publications
# print([pub.bib['title'] for pub in author.publications])

# # Take a closer look at the first publication
# pub = author.publications[0].fill()
# print(pub)

# # Which papers cited that publication?
# print([citation.bib['title'] for citation in pub.citedby])

search_query = scholarly.search_pubs(
    'Perception of physical stability and center of mass of 3D objects')
publication = next(search_query)
# print(publication)
full_publication = publication.fill()
print("ID is yacine  "+ full_publication.bib["ID"])
print("ID is yacine  "+ full_publication.bib["author_id"])

# # Set the json filename
# jsonFile = 'result.json'
# # Open a json file for writing json data
# with open(jsonFile, 'w') as fileHandler1:
#     json.dump(full_publication, fileHandler1, indent=None)

try:
    connection = psycopg2.connect(user="tomee",
                                #   password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pfe_dataset")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS article
                (	ID VARCHAR(100) PRIMARY KEY NOT NULL,
                    abstarct TEXT,
                    author VARCHAR(200),
                    author_id VARCHAR(200),
                    cites INT,
                    eprint VARCHAR(200),
                    gsrank INT,
                    journal VARCHAR(100),
                    nbr INT,
                    pages VARCHAR(100),
                    publisher VARCHAR(100),
                    title VARCHAR(200),
                    url VARCHAR(200),
                    venue VARCHAR(200),
                    volume VARCHAR(200),
                    pb_year VARCHAR(200)
            
                );     
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Articles Table created successfully in PostgreSQL ")


    q = """INSERT INTO article (article_id,abstarct,author,author_id,eprint,cites,gsrank,journal,nbr,pages,publisher,title,url,venue,volume,pb_year,) 
         VALUES(%(bib["ID"])s, %(bib["abstract"])s, %(bib["author"])s, %(bib["author_id"])s)"""

    cursor.execute(q, full_publication)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
