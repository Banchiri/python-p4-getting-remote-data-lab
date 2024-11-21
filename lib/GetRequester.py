import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        URL = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.content
        

    def load_json(self):
        URL = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.json()
result = GetRequester().load_json()
print(result)