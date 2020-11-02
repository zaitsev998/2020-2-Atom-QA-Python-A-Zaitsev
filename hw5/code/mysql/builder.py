from random import randint
from faker import Faker
from mysql_client import MysqlConnection
fake = Faker(locale='en_US')


class MysqlBuilder(object):
    def __init__(self, connection: MysqlConnection):
        self.connection = connection
        self.create_log()

    def create_log(self):
        log_query = """
            CREATE TABLE IF NOT EXISTS `access_log` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `ip` varchar(18) NOT NULL,
                `datetime` datetime NOT NULL,
                `timezone` varchar(6) NOT NULL,
                `method` varchar(8) NOT NULL,
                `url` varchar(500) NOT NULL,
                `http_version` varchar(10) NOT NULL,
                `status_code` varchar(5) NOT NULL,
                `size` int(11) DEFAULT NULL,
                `referer` varchar(1500) DEFAULT NULL,
                `user_agent` varchar(10000) DEFAULT NULL,
                PRIMARY KEY (`id`))CHARSET=utf8
        """
        self.connection.execute_query(log_query)

    def add_log_record(self, ip, datetime, timezone, method, url, http_version, status_code, size, referer, user_agent):
        insert_log_record = f"""
                        INSERT INTO access_log(ip, datetime, timezone, method, url, 
                        http_version, status_code, size, referer, user_agent) 
                        VALUES('{ip}', '{datetime}', '{timezone}', '{method}', '{url}', '{http_version}', 
                        '{status_code}', '{size}', '{referer}', '{user_agent}')
                         """
        self.connection.execute_query(insert_log_record)


