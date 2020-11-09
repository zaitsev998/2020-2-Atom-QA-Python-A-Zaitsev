from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.25', 3333
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

MOCK_HOST, MOCK_PORT = '127.0.0.26', 1054
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

USERS_URL = urljoin(APP_URL, 'users')
NEW_USER_URL = urljoin(USERS_URL, 'new')
# VALID_URL = urljoin(STUB_URL, 'valid')
# MOCK_VALID_URL = urljoin(MOCK_URL, 'valid')
# APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')
# STUB_SHUTDOWN_URL = urljoin(STUB_URL, 'shutdown')
# MOCK_SHUTDOWN_URL = urljoin(MOCK_URL, 'shutdown')
# MOCK_SET_USERS = urljoin(MOCK_URL, 'set_valid_users')
