from ui.fixtures.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--selenoid', default=None)
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--browser', default='chrome')


@pytest.fixture(scope='session')
def config(request):
    selenoid = request.config.getoption('--selenoid')
    url = request.config.getoption('--url')
    version = request.config.getoption('--browser_ver')
    browser = request.config.getoption('--browser')
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}
