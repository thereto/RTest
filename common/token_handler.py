
from common.request_util import RequestUtil
from config.config import LOGIN_INFO
from common.logger import logger

class TokenHandler:
    token = None

    @classmethod
    def get_token(cls):
        if cls.token:
            return cls.token

        logger.info("开始获取token...")

        response = RequestUtil.send_request(
            method=LOGIN_INFO["method"],
            url=LOGIN_INFO["url"],
            json=LOGIN_INFO["data"],
            need_token=False
        )

        # httpbin没有token，这里模拟
        cls.token = "mock_token_123456"

        logger.info(f"获取token成功: {cls.token}")
        return cls.token
