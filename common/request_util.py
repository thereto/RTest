# 请求封装

import requests
from config.config import BASE_URL

class RequestUtil:

    @staticmethod
    def send_request(method, url, **kwargs):
        full_url = BASE_URL + url
        response = requests.request(method, full_url, **kwargs)
        return response
