from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_home(self):
        self.client.get("/")
