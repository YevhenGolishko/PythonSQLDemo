from sqlalchemy import table, select, column, desc


def test_sql_builder():
    _table = table("users")
    q = select("*", _table)
    print(q)


def test_query():
    _table = table("users")
    r = select("*", _table).where(*[column("id") == 1]).order_by(desc(column("id")))
    print(r)