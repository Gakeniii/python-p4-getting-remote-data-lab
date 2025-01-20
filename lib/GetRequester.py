import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response =requests.get(self.url)
        return response.content

    def load_json(self):
        body = self.get_response_body().decode('utf-8')
        return json.loads(body)

if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    print(requester.load_json())
