
import pytest
from common.request_util import RequestUtil
from common.assertion import Assertion
from utils.file_util import load_yaml

data = load_yaml("data/login_data.yaml")

@pytest.mark.parametrize("case", data)
def test_api(case):
    response = RequestUtil.send_request(
        method=case["method"],
        url=case["url"],
        params=case.get("params")
    )

    Assertion.assert_code(response, case["expected_code"])
