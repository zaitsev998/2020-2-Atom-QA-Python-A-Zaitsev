import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import re


class MockHandleRequests(BaseHTTPRequestHandler):
    data = None
    rules = {
        'name': 'The name can only consist of letters, spaces, and dashes.',
        'email': 'Invalid email address entered.',
        'password': 'The password must be between 8 and 20 characters long and can only consist of letters and '
                    'numbers. Must have at least one uppercase letter, one lowercase letter, and at least one digit.'
    }
    users = {}

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/users'):
            self._set_headers()
            self.wfile.write(json.dumps(self.users).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path.startswith('/users/new'):
            self.add_new_user()
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        if self.path.startswith('/users') and self.path.endswith('/edit'):
            self.edit_user()
        else:
            self.send_response(404)
            self.end_headers()

    def edit_user(self):
        content_type = self.headers.get('Content-type', 0)
        if content_type == 'application/json':
            self._set_headers()
            id = int(self.path.split('/')[2])
            content_len = int(self.headers.get('content-length', 0))
            put_body = self.rfile.read(content_len)
            data = json.loads(put_body)
            self.edit_user_data(data, id)
        else:
            self.send_response(400)
            self.end_headers()

    def edit_user_data(self, data, id):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        check = dict()
        if name:
            check['name'] = self.check_name(name)
            if check['name']:
                self.users[id]['name'] = name
        else:
            check['name'] = True
        if email:
            check['email'] = self.check_email(data['email'])
            if check['email']:
                self.users[id]['email'] = email
        else:
            check['name'] = True
        if password:
            check['password'] = self.check_password(data['password'])
            if check['password']:
                self.users[id]['password'] = password
        else:
            check['password'] = True
        if set(check.values()) == {True}:
            self.wfile.write(json.dumps(self.users[id]).encode())
        else:
            self.wfile.write('\r\n'.join([self.rules[k] if v is False else '' for k, v in check.items()]).encode())

    def add_new_user(self):
        content_type = self.headers.get('Content-type', 0)
        if content_type == 'application/json':
            self._set_headers()
            content_len = int(self.headers.get('Content-Length', 0))
            post_body = self.rfile.read(content_len)
            data = json.loads(post_body)
            check = dict()
            check['name'] = self.check_name(data['name'])
            check['email'] = self.check_email(data['email'])
            check['password'] = self.check_password(data['password'])
            if set(check.values()) == {True}:
                users_count = len(self.users)
                data['id'] = users_count + 1
                self.users[users_count + 1] = data
                self.wfile.write(json.dumps(self.users[users_count + 1]).encode())
            else:
                self.wfile.write(''.join([self.rules[k] + '\r\n' if v is False else '' for k, v in
                                          check.items()]).encode())
        else:
            self.send_response(400)
            self.end_headers()

    @staticmethod
    def check_name(name):
        for letter in name:
            if not letter.isalpha() and letter not in ('-', ' '):
                return False
        return True

    @staticmethod
    def check_email(email):
        regexp = re.compile("^([a-z0-9_-]+\\.)*[a-z0-9_-]+@[a-z0-9_-]+(\\.[a-z0-9_-]+)*\\.[a-z]{2,6}$")
        email = regexp.match(email)
        if not email:
            return False
        return True

    @staticmethod
    def check_password(password):
        if len(password) < 8 or len(password) > 20:
            return False
        check = {
            'lowercase': False,
            'uppercase': False,
            'digit': False,
        }
        for letter in password:
            if letter.isalpha():
                if letter.islower():
                    check['lowercase'] = True
                if letter.isupper():
                    check['uppercase'] = True
            elif letter.isdigit():
                check['digit'] = True
            else:
                return False
        if False in check.values():
            return False
        return True


class SimpleHTTPMock:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()
