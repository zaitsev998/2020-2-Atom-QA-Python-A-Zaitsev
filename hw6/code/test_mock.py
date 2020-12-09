import json
from socket_client import SocketClient
import settings
from random import randint
import pytest
from faker import Faker

fake = Faker(locale='en_US')


def test_add_user(server, mock):
    data = {
        'name': fake.first_name(),
        'email': fake.email(),
        'password': fake.first_name() + str(randint(1, 100)) + fake.last_name()
    }
    user_data = eval(send_new_user(data))
    user_id = str(user_data["id"])
    client = SocketClient(settings.APP_HOST, settings.APP_PORT)
    response = client.send_get('/users/')
    all_users = eval(json.loads(response)[-1])
    try:
        user = all_users[user_id]
    except KeyError:
        assert False
    else:
        assert user_data['name'] == user['name']
        assert user_data['email'] == user['email']
        assert user_data['password'] == user['password']


def test_wrong_user_data_in_creating(server, mock):
    data = {
        'name': fake.first_name(),
        'email': fake.first_name(),
        'password': fake.first_name() + str(randint(1, 100)) + fake.last_name()
    }
    res = send_new_user(data)
    assert res == 'Invalid email address entered.'

    data = {
        'name': str(randint(1, 100)),
        'email': fake.email(),
        'password': fake.first_name() + str(randint(1, 100)) + fake.last_name()
    }
    res = send_new_user(data)
    assert res == 'The name can only consist of letters, spaces, and dashes.'

    data = {
        'name': fake.first_name(),
        'email': fake.email(),
        'password': str(randint(1, 100))
    }
    res = send_new_user(data)
    assert res == 'The password must be between 8 and 20 characters long and can only consist of letters and ' \
                  'numbers. Must have at least one uppercase letter, one lowercase letter, and at least one digit.'


def test_edit_user_email(server, mock):
    data = {
        'name': fake.first_name(),
        'email': fake.email(),
        'password': fake.first_name() + str(randint(1, 100)) + fake.last_name()
    }
    res = eval(send_new_user(data))
    user_id = str(res['id'])
    new_data = {
        'email': fake.email()
    }
    user = eval(send_edit_user(user_id, new_data))
    assert user['name'] == data['name']
    assert user['email'] == new_data['email']
    assert user['password'] == data['password']


def test_wrong_user_data_in_editing_email(server, mock):
    data = {
        'name': fake.first_name(),
        'email': fake.email(),
        'password': fake.first_name() + str(randint(1, 100)) + fake.last_name()
    }
    res = eval(send_new_user(data))
    user_id = str(res['id'])
    new_data = {
        'email': fake.first_name()
    }
    res = send_edit_user(user_id, new_data)
    assert res == 'Invalid email address entered.'


def test_bad_request(server, mock):
    data = {
        'name': fake.first_name()
    }
    data = json.dumps(data)
    client = SocketClient(settings.APP_HOST, settings.APP_PORT)
    response = client.send_post('/users/new/', body=data, headers={'Content-Length': str(len(data))})
    res = json.loads(response)[0]
    assert '400' in res
    assert 'BAD REQUEST' in res


def send_edit_user(user_id, new_data):
    new_data = json.dumps(new_data)
    client = SocketClient(settings.APP_HOST, settings.APP_PORT)
    response = client.send_put(f'/users/{user_id}/edit/', body=new_data, headers={'Content-type': 'application/json',
                                                                                  'Content-Length': str(len(new_data))})
    res = json.loads(response)[-1]
    return res


def send_new_user(data):
    data = json.dumps(data)
    client = SocketClient(settings.APP_HOST, settings.APP_PORT)
    response = client.send_post('/users/new/', body=data, headers={'Content-type': 'application/json',
                                                                   'Content-Length': str(len(data))})
    res = json.loads(response)[-1]
    return res
