# 请求封装

import requests
from config.config import BASE_URL, DEFAULT_HEADERS
from common.logger import logger
from common.token_handler import TokenHandler


class RequestUtil:

    @staticmethod
    def send_request(method, url, retry=True, **kwargs):
        full_url = BASE_URL + url

        headers = kwargs.get("headers", {})
        headers.update(DEFAULT_HEADERS)

        token = TokenHandler.get_token()
        headers["Authorization"] = f"Bearer {token}"

        kwargs["headers"] = headers

        logger.info(f"请求地址: {full_url}")
        logger.info(f"请求参数: {kwargs}")

        response = requests.request(method, full_url, **kwargs)

        # 模拟token失效逻辑（实际项目一般是401）
        if response.status_code == 401 and retry:
            logger.warning("token失效，重新获取...")

            TokenHandler.refresh_token()

            return RequestUtil.send_request(method, url, retry=False, **kwargs)

        logger.info(f"响应: {response.status_code}")
        return response
