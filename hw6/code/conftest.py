import pytest 
from socket_client import SocketClient
import flask_server
import httpserver_mock
import requests
import settings
from urllib.parse import urljoin


@pytest.fixture(scope='session')
def server():
    yield flask_server.run_server(settings.APP_HOST, settings.APP_PORT)
    requests.get(urljoin(settings.APP_URL, '/shutdown'))


@pytest.fixture(scope='session')
def mock():
    http_mock = httpserver_mock.SimpleHTTPMock(settings.MOCK_HOST, settings.MOCK_PORT)
    yield http_mock.start()
    http_mock.stop()
