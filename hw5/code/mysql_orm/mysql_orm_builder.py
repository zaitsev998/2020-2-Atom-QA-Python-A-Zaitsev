from random import randint
from faker import Faker
from models import Base, LogRecord
from mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine
        self.create_log()

    def create_log(self):
        if not self.engine.dialect.has_table(self.engine, 'access_log'):
            Base.metadata.tables['access_log'].create(self.engine)

    def add_log_record(self, ip, datetime, timezone, method, url, http_version, status_code, size, referer, user_agent):

        log_record = LogRecord(
            ip=ip,
            datetime=datetime,
            timezone=timezone,
            method=method,
            url=url,
            http_version=http_version,
            status_code=status_code,
            size=size,
            referer=referer,
            user_agent=user_agent
        )

        self.connection.session.add(log_record)
        self.connection.session.commit()
        return log_record
