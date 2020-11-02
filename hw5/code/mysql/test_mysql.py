import random
from datetime import datetime

import pytest
from mysql.mysql_client import MysqlConnection
from mysql.builder import MysqlBuilder
import faker
from tzlocal import get_localzone

local = get_localzone()
fake = faker.Faker(locale='en_US')


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(connection=self.mysql)

    def test_adding_worker(self):
        ip = fake.ipv4()
        dtm_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dtm = datetime.strptime(dtm_string, '%Y-%m-%d %H:%M:%S')
        timezone = datetime.now(local).strftime('%z')
        method = fake.http_method()
        url = fake.url()
        http_version = 'HTTP/1.1'
        status_code = random.choice(['200', '404', '500', '301'])
        size = random.randint(0, 10000)
        referer = fake.uri()
        user_agent = random.choice([fake.firefox(), fake.chrome(),
                                    fake.safari(), fake.internet_explorer(),
                                    fake.opera()])
        self.builder.add_log_record(ip, dtm, timezone, method, url, http_version, status_code, size, referer, user_agent)
        find_result_query = f'SELECT * FROM access_log WHERE ip="{ip}" and datetime="{dtm_string}" and method="{method}"' \
                            f' and url="{url}" and http_version="{http_version}" and status_code="{status_code}" and ' \
                            f'size="{size}" and referer="{referer}" and user_agent="{user_agent}" and ' \
                            f'timezone="{timezone}"'
        print(find_result_query)
        res = self.mysql.execute_query(find_result_query)
        assert res