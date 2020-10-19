import json
from random import randint
from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict

from settings import EMAIL, PASSWORD


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient:

    def __init__(self):
        self.base_url = 'https://target.my.com/'
        self.email = EMAIL
        self.password = PASSWORD
        self.session = requests.Session()
        self.csrftoken = None
        self.login()

    def _request(self, method, location, status_code=200, headers=None, params=None, data=None, json=True):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers, params=params, data=data)
        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if json:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" with error "{error}"!')
            return json_response
        return response

    def login(self):
        url_auth = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36',
            'Referer': 'https://target.my.com/',
        }

        data = {
            'email': self.email,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        self.session.request('POST', url=url_auth, headers=headers, data=data)
        self.get_csrf_token()

    def get_csrf_token(self):
        location_csrf = 'csrf/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'Referer': 'https://target.my.com/dashboard',
        }

        response = self._request('GET', location_csrf, headers=headers, json=False)
        self.csrftoken = list(response.cookies)[0].value
        print(self.session.cookies)

    def create_segment(self, segment_name: str = None):
        if segment_name is None:
            segment_name = f'{randint(1,100)}{randint(1, 100)}'
        request_payload = {"name": segment_name,
                           "pass_condition": 1,
                           "relations": [{"object_type": "remarketing_player",
                                         "params": {"type": "positive",
                                                    "left": 365,
                                                    "right": 0}}],
                           "logicType": "or"}
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,' \
                   'relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrftoken,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'Referer': 'https://target.my.com/segments/segments_list/new'
        }
        data = json.dumps(request_payload)
        response = self._request('POST', location, headers=headers, data=data, json=False)
        segment_id = response.text.split(',')[1].split(': ')[-1]
        return int(segment_id)

    def delete_segment(self, segment_id):
        deleting_location = f'/api/v2/remarketing/segments/{segment_id}.json'
        headers = {
            'X-CSRFToken': self.csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'Content-Type': 'application/json'
        }
        self._request('DELETE', deleting_location, status_code=204, headers=headers, json=False)

    def get_all_segments_ids(self):
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,' \
                   'relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,' \
                   'flags&limit=500&_=1603102403184'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = self._request('GET', location, headers=headers)
        segment_ids = [segment['id'] for segment in response['items']]
        return segment_ids


if __name__ == '__main__':
    mtc = MyTargetClient()
    # mtc.create_segment()
    mtc.get_all_segments_ids()