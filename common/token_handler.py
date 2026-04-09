
from common.request_util import RequestUtil
from config.config import LOGIN_INFO
from common.logger import logger

class TokenHandler:
    token = None

    # @classmethod
    # def get_token(cls):
    #     if cls.token:
    #         return cls.token

    #     logger.info("开始获取token...")

    #     response = RequestUtil.send_request(
    #         method=LOGIN_INFO["method"],
    #         url=LOGIN_INFO["url"],
    #         json=LOGIN_INFO["data"],
    #         need_token=False
    #     )

    #     # httpbin没有token，这里模拟
    #     cls.token = "mock_token_123456"

    #     logger.info(f"获取token成功: {cls.token}")
    #     return cls.token

    @classmethod
    def get_token(cls):
        if cls.token:
            return cls.token
        return cls.refresh_token()

    @classmethod
    def refresh_token(cls):
        logger.info("重新获取token...")

        response = requests.request(
            LOGIN_INFO["method"],
            BASE_URL + LOGIN_INFO["url"],
            json=LOGIN_INFO["data"]
        )

        # 模拟获取token
        cls.token = "new_mock_token_123"

        logger.info(f"新token: {cls.token}")
        return cls.token
