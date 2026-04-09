import pytest
import allure
from common.request_util import RequestUtil
from common.assertion import Assertion
from utils.file_util import load_yaml

cases = load_yaml("data/login_data.yaml")

@allure.feature("接口测试")
@pytest.mark.parametrize("case", cases)
def test_api(case):

    with allure.step(f"执行用例: {case['name']}"):
        response = RequestUtil.send_request(
            method=case["method"],
            url=case["url"],
            params=case.get("params")
        )

    with allure.step("断言状态码"):
        Assertion.assert_code(response, case["expected_code"])
