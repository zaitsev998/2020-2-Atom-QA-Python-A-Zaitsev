import json
import time
from socket_client import SocketClient
import requests
from flask import Flask, request, jsonify
from threading import Thread
from settings import MOCK_URL
from urllib.parse import urljoin

app = Flask(__name__)


def run_server(host, port):
    server = Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })
    server.start()
    return server


def shutdown_server():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()


@app.route('/')
def main_page():
    return jsonify('flask sever root'), 200


@app.route('/users/', methods=['GET'])
def get_users():
    if request.method == 'GET':
        response = requests.get(urljoin(MOCK_URL, 'users'))
        return response.text, 200
    return jsonify('Bad request'), 400


@app.route('/users/new/', methods=['POST'])
def add_new_user():
    if request.method == 'POST':
        if request.headers.get('Content-type') == 'application/json':
            response = requests.post(urljoin(MOCK_URL, 'users/new'), data=request.data,
                                     headers={'Content-type': 'application/json'})
            return response.text, 200
        else:
            return jsonify('Bad request'), 400
    return jsonify('Bad request'), 400


@app.route('/users/<id>/edit/', methods=['PUT'])
def edit_user(id):
    if request.method == 'PUT':
        if request.headers['Content-type'] == 'application/json':
            response = requests.put(urljoin(MOCK_URL, f'users/{id}/edit'), data=request.data,
                                    headers={'Content-type': 'application/json'})
            return response.text, 200
        else:
            return jsonify('Bad request'), 400
    return jsonify('Bad request'), 400

