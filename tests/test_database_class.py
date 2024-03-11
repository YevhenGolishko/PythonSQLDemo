import pytest
import sqlalchemy
from assertpy import assert_that

from tests.database import Database
from tests.repository import UserRepository, OrderRepository


@pytest.fixture(scope="session")
def db():
    engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    connection = engine.connect()
    yield Database(connection)
    connection.close()


def test_database_query(db):
    user_repository = UserRepository(db)
    result = user_repository.get_all_users()
    assert_that(result[0][0]).is_equal_to(1)


def test_find_one_by_id(db):
    user_repository = UserRepository(db)
    result = user_repository.find_one_by_id(1)
    assert_that(result[1]).is_equal_to('Ivan')


def test_find_by(db):
    user_repository = UserRepository(db)
    result = user_repository.find_by(last_name="Popov", first_name="Petr")
    assert_that(len(result)).is_equal_to(1)
    assert_that(result[0][0]).is_equal_to(2)


def test_can_find_order_by_amount(db):
    order_repository = OrderRepository(db)
    order = order_repository.find_by(total_amount=300)
    assert_that(len(order)).is_equal_to(1)
    assert_that(order[0][0]).is_equal_to(3)


def test_can_add_new_user(db):
    user_repository = UserRepository(db)
    user_repository.save({"first_name": "Vasyl", "last_name": "Petrov", "age": 46})
