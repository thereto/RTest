# 断言封装
class Assertion:

    @staticmethod
    def assert_code(response, expected_code):
        assert response.status_code == expected_code

    @staticmethod
    def assert_in_text(response, expected_text):
        assert expected_text in response.text
