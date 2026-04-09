# 断言封装
from common.logger import logger

class Assertion:

    @staticmethod
    def assert_code(response, expected_code):
        actual = response.status_code
        logger.info(f"断言状态码: 实际={actual}, 期望={expected_code}")
        assert actual == expected_code

    @staticmethod
    def assert_in_text(response, expected_text):
        logger.info(f"断言文本包含: {expected_text}")
        assert expected_text in response.text
