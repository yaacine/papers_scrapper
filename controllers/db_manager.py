from scholarly import scholarly
import json
import psycopg2

class db_manager(object):
    """
    docstring
    """
    
    def connect(self):
        """
        docstring
        """
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
            return connection , cursor
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        # finally:
        #     #closing database connection.
        #     if (connection):
        #         cursor.close()
        #         connection.close()
        #         print("PostgreSQL connection is closed"
        pass


    def insert_publication(self, publication):
        """
        docstring
        """
        pass

    def find_publication(self, publication_id):
        """
        docstring
        """
        pass

    def get_publication(self, publication_id):
        """
        docstring
        """
        pass

    def delete_publicaiton(self, publication_id):
        """
        docstring
        """
        pass

    pass