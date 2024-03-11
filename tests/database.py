import logging

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database(object):

    def __init__(self, connection):
        self._connection = connection

    def execute(self, query):
        logging.info(f"About to execute query {query}")
        return self._connection.execute(query)
        # return self._connection.commit()

    def fetch_one(self, query):
        return self.execute(query).one()

    def fetch_all(self, query):
        return self.execute(query).all()
