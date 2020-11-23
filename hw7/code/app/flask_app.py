from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'test_user': generate_password_hash('12345'),
    'test_user1': generate_password_hash('123')
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


@app.route('/profile')
@auth.login_required
def profile():
    return "{}, this is your profile!".format(auth.current_user())


@app.route('/photo')
@auth.login_required
def photo():
    return 'Photo'


@app.route('/shareware')
def shareware():
    return 'Shareware'


@app.route('/new_user', methods=['GET'])
def new_user():
    user = request.headers.get('user')
    password = request.headers.get('password')
    if user not in users:
        users[user] = password
        return f'Congratulations, {user} you have successfully registered.'
    return 'A user with this name already exists.'


@app.route('/logout')
@auth.login_required
def logout():
    return f"{auth.current_user()} was logout!", 401


if __name__ == '__main__':
    app.run(debug=False, host='192.168.0.106', port=2222)
