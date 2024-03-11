import sqlalchemy
from assertpy import assert_that


def test_database_query():
    engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    connection = engine.connect()
    sql = "SELECT * FROM users;"
    result = connection.execute(sqlalchemy.text(sql))
    for user in result:
        assert_that(user[0]).is_equal_to(1)
