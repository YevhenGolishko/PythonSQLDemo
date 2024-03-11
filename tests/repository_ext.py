from sqlalchemy import select


class Repository(object):

    def __init__(self, db, table):
        self._table = table
        self._db = db

    def find_all(self):
        return self._db.fetch_all(select(self._table))

    def find_by_id(self, _id):
        query = select(self._table).where(self._table.id == _id)
        return self._db.fetch_one(query)[0]

    def insert(self, data):
        table = self._table(**data)
        self._db._connection.add(table)
        self._db._connection.commit()

