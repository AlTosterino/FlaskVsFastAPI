from locust import HttpUser, task, between

NEWS_ID = None

class NewsUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_news(self):
        global NEWS_ID
        self.client.get(f"/news/{NEWS_ID}", name="news/[id]")

    @task
    def get_news_with_filter(self):
        global NEWS_ID
        self.client.get(f"/news?id={NEWS_ID}", name="news?id=[id]")

    def on_start(self):
        news_response = self.client.post(
            "/news",
            json={
                "title": "Title of the news",
                "content": "Content of the news, usually very long lorem ipsum beacuse why not",
                "creator": {"first_name": "John", "last_name": "Doe"},
            },
        )
        global NEWS_ID
        if not NEWS_ID:
            NEWS_ID = news_response.json()["id"]
