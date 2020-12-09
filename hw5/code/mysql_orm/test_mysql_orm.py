import random
from datetime import datetime

import pytest
from mysql_orm.models import LogRecord
from mysql_orm.mysql_orm_client import MysqlOrmConnection
from mysql_orm.mysql_orm_builder import MysqlOrmBuilder
from faker import Faker
from tzlocal import get_localzone

local = get_localzone()
fake = Faker(locale='en_US')


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test_adding_log_record_orm(self):
        log_record = self.builder.add_log_record(ip=fake.ipv4(),
                                                 datetime=datetime.now(),
                                                 timezone=datetime.now(local).strftime('%z'),
                                                 method=fake.http_method(),
                                                 url=fake.url(),
                                                 http_version='HTTP/1.1',
                                                 status_code=random.choice(['200', '404', '500', '301']),
                                                 size=random.randint(0, 10000),
                                                 referer=fake.uri(),
                                                 user_agent=random.choice([fake.firefox(), fake.chrome(),
                                                                           fake.safari(), fake.internet_explorer(),
                                                                           fake.opera()])
                                                 )
        res = self.mysql.session.query(LogRecord).filter_by(id=log_record.id).all()
        assert (res[0].ip, res[0].datetime, res[0].timezone, res[0].method, res[0].url, res[0].http_version,
                res[0].status_code, res[0].size, res[0].referer, res[0].user_agent) == \
               (log_record.ip, log_record.datetime, log_record.timezone, log_record.method, log_record.url,
                log_record.http_version, log_record.status_code, log_record.size, log_record.referer,
                log_record.user_agent)
