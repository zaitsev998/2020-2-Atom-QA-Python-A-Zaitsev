import json
import socket


class SocketClient:

    def __init__(self, target_host: str, target_port: int, timeout=0.1):
        self.target_host = target_host
        self.target_port = target_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.settimeout(timeout)        
        self.client.connect((self.target_host, self.target_port))
        self.buffer_size = 4096

    def _get_data(self, request):
        self.client.send(request.encode())
        total_data = []
        while True:
            data = self.client.recv(self.buffer_size)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        return data

    @staticmethod
    def _make_headers(headers):
        if headers is None:
            headers = ''
        else:
            headers = '\r\n'.join([': '.join((k, v)) for k, v in headers.items()]) + '\r\n'
        return headers

    def send_get(self, location: str, headers=None):
        headers = self._make_headers(headers)
        request = f'GET {location} HTTP/1.1\r\nHost:{self.target_host}\r\n{headers}\r\n'
        data = self._get_data(request)
        data = json.dumps(data, indent=4)
        return data

    def send_post(self, location: str, headers=None, body=''):
        headers = self._make_headers(headers)
        request = f'POST {location} HTTP/1.1\r\nHost:{self.target_host}\r\n{headers}\r\n{body}\r\n'
        data = self._get_data(request)
        data = json.dumps(data, indent=4)
        return data

    def send_put(self, location: str, headers=None, body=''):
        headers = self._make_headers(headers)
        request = f'PUT {location} HTTP/1.1\r\nHost:{self.target_host}\r\n{headers}\r\n{body}\r\n'
        data = self._get_data(request)
        data = json.dumps(data, indent=4)
        return data
