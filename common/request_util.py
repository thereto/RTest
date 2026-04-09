# 请求封装

import requests
from config.config import BASE_URL, DEFAULT_HEADERS
from common.logger import logger
from common.token_handler import TokenHandler

class RequestUtil:

    @staticmethod
    def send_request(method, url, need_token=True, **kwargs):
        full_url = BASE_URL + url

        headers = kwargs.get("headers", {})
        headers.update(DEFAULT_HEADERS)

        if need_token:
            token = TokenHandler.get_token()
            headers["Authorization"] = f"Bearer {token}"

        kwargs["headers"] = headers

        logger.info(f"请求地址: {full_url}")
        logger.info(f"请求方式: {method}")
        logger.info(f"请求参数: {kwargs}")

        try:
            response = requests.request(method, full_url, **kwargs)
            logger.info(f"响应状态码: {response.status_code}")
            logger.info(f"响应内容: {response.text}")
            return response
        except Exception as e:
            logger.error(f"请求异常: {e}")
            raise
