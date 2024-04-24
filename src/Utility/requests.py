import json

from src.Config.host_config import API_HOST


import requests
import os

class RequestsAPI(object):
    def __init__(self):
        self.env = os.environ['ENV']
        self.baseUrl = API_HOST[self.env]


    def POST(self, endpoint, payload=None, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.baseUrl + endpoint

        response = requests.post(
            url=url,
            data=json.dumps(payload),
            headers=headers
        )

        return response.json()