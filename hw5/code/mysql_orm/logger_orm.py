import os
from datetime import datetime

from mysql_orm_client import MysqlOrmConnection
from mysql_orm_builder import MysqlOrmBuilder
from settings import USER, PASSWORD, DB_NAME_ORM, HOST, PORT
import argparse

from sqlalchemy.exc import DataError, InvalidRequestError


class LoggerOrm:

    def __init__(self, log_file):
        self.mysql = MysqlOrmConnection(user=USER, password=PASSWORD, db_name=DB_NAME_ORM, host=HOST, port=PORT)
        self.builder = MysqlOrmBuilder(connection=self.mysql)
        self.log = os.path.abspath(log_file)
        self.parse_log()

    def parse_log(self):
        with open(self.log, 'r', encoding='utf8') as file:
            for line in file:
                line_elements = line.split(' ')
                if len(line_elements) < 13:
                    continue
                try:
                    size = int(line_elements[9])
                except ValueError:
                    size = 0
                try:
                    self.builder.add_log_record(ip=line_elements[0],
                                                datetime=datetime.strptime(line_elements[3][1:], '%d/%b/%Y:%H:%M:%S'),
                                                timezone=line_elements[4][:-1],
                                                method=line_elements[5][1:],
                                                url=line_elements[6],
                                                http_version=line_elements[7][:-1],
                                                status_code=int(line_elements[8]),
                                                size=size,
                                                referer=line_elements[10],
                                                user_agent=line_elements[11])
                except (DataError, InvalidRequestError):
                    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='file_path', type=str, help='Path to access.log file')
    args = parser.parse_args()
    LoggerOrm(args.file_path)
