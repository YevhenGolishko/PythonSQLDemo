from sqlalchemy import table, select, column, insert

from tests.database import Database


class DatabaseRepository(object):

    def __init__(self, db: Database, table_name: str):
        self._db = db
        self._table_name = table_name

    def find_one_by_id(self, _id):
        name = self._table_name
        query = select("*", table(name)).where(column("id") == _id)
        return self._db.fetch_one(query)

    def find_by(self, order_by=None, **kwargs):
        clause = self.__to_criteria(**kwargs)
        query = select("*", table(self._table_name)).where(*clause).order_by(order_by)
        return self._db.fetch_all(query)

    def __to_criteria(self, **kwargs):
        res = []
        for k, v in kwargs.items():
            res.append(column(k) == v)
        return res

    def save(self, data: dict):
        cols = []
        for k in data.keys():
            cols.append(column(k))

        q = insert(table(self._table_name, *cols)).values(data)
        return self._db.execute(q)


class UserRepository(DatabaseRepository):

    def __init__(self, db: Database):
        super().__init__(db, "users")

    def get_all_users(self):
        _table = table(self._table_name)
        sql = select("*", _table)
        return self._db.fetch_all(sql)


class OrderRepository(DatabaseRepository):

    def __init__(self, db: Database):
        super().__init__(db, "orders")


