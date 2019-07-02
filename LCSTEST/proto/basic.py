from locust import HttpLocust,TaskSet,task


def index(l):
    l.client.get("/")


def stats(l):
    l.client.get("/stats/requests")


class UserTasks(TaskSet):
    tasks = [index, stats]

    @task
    def page404(self):
        self.client.get("/does_not_exist")


class WebsiteUser(HttpLocust):
    host = "https://www.hao123.com/"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks
