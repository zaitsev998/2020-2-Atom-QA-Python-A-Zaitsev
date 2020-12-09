from locust import HttpUser, TaskSet, task, between
from faker import Faker
from werkzeug.security import generate_password_hash

fake = Faker(locale='en_US')


class IOSUserBehavior(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('test_user', '12345'))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})
        assert r.status_code == 200

    def on_stop(self):
        r = self.client.get("/logout")
        assert r.status_code == 401

    @task
    def profile(self):
        r = self.client.get("/profile")
        assert r.status_code == 200


class AndroidUserBehavior(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('test_user1', '123'))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})
        assert r.status_code == 200

    def on_stop(self):
        r = self.client.get("/logout")
        assert r.status_code == 401

    @task(2)
    def shareware(self):
        r = self.client.get("/shareware")
        assert r.status_code == 200

    @task
    def photo(self):
        r = self.client.get("/photo")
        assert r.status_code == 200


class NewUserBehavior(TaskSet):

    def on_start(self):
        user = fake.first_name()
        password = fake.password()
        headers = {
            'user': user,
            'password': generate_password_hash(password)
        }
        r = self.client.get(f"/new_user", headers=headers)
        assert r.status_code == 200
        r = self.client.get("/", auth=(user, password))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})
        assert r.status_code == 200

    def on_stop(self):
        r = self.client.get("/logout")
        assert r.status_code == 401

    @task(3)
    def shareware(self):
        r = self.client.get("/shareware")
        assert r.status_code == 200

    @task(2)
    def photo(self):
        r = self.client.get("/photo")
        assert r.status_code == 200

    @task
    def profile(self):
        r = self.client.get("/profile")
        assert r.status_code == 200


class WebsiteUser(HttpUser):
    tasks = [NewUserBehavior]
    wait_time = between(1, 2)


class NewIOSUser(HttpUser):
    tasks = [NewUserBehavior, IOSUserBehavior]
    wait_time = between(2, 5)


class NewAndroidUser(HttpUser):
    tasks = [NewUserBehavior, AndroidUserBehavior]
    wait_time = between(1, 3)


class IOSUser(HttpUser):
    tasks = [IOSUserBehavior]
    wait_time = between(2, 5)


class AndroidUser(HttpUser):
    tasks = [AndroidUserBehavior]
    wait_time = between(1, 3)