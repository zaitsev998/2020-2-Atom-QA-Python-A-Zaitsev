import pytest
from mysql.mysql_client import MysqlConnection
from mysql_orm.mysql_orm_client import MysqlOrmConnection
from mysql.settings import USER, PASSWORD, DB_NAME, HOST, PORT, DB_NAME_ORM


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection(user=USER, password=PASSWORD, db_name=DB_NAME, host=HOST, port=PORT)


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user=USER, password=PASSWORD, db_name=DB_NAME_ORM, host=HOST, port=PORT)
