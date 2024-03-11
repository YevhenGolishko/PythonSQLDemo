import pytest
import sqlalchemy
from assertpy import assert_that
from sqlalchemy import select
from sqlalchemy.orm import Session

from tests.database import Database
from tests.pojo import Users
from tests.repository_ext import Repository


@pytest.fixture(scope="session")
def db():
    engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    # connection = engine.connect()
    connection = Session(bind=engine)
    yield Database(connection)
    connection.close()


def test_can_create_query_from_pojo():
    q = select(Users)
    print(q)


def test_can_find_user_by_pojo(db):
    users_repo = Repository(db, Users)
    users = users_repo.find_all()
    assert_that(len(users)).is_equal_to(4)


def test_can_get_user_pojo_by_id(db):
    users_repo = Repository(db, Users)
    user = users_repo.find_by_id(1)
    assert_that(user.first_name).is_equal_to('Ivan')


def test_can_insert_pojo(db):
    users_repo = Repository(db, Users)
    users_repo.insert({"first_name": "Sergey", "last_name": "Kutuzov", "age": 46})
