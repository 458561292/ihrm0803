import json
import unittest
import requests
import app
from api.UserAPI import UserLogin
from parameterized import parameterized


def read_from_json():
    data = []
    with open(app.BASE_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        test_data = json.load(f)
        for value in test_data.values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            data.append((mobile, password, success, code, message))

    return data


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.user_obj = UserLogin()

    def tearDown(self):
        self.session.close()

    def test_login_success(self):
        response = self.user_obj.login(self.session, "13800000002", "123456")
        print("登录成功的响应结果:", response.json())
        result = response.json()
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("成功", result.get("message"))

    @parameterized.expand(read_from_json())
    def test_login(self, mobile, password, success, code, message):
        response = self.user_obj.login(self.session, mobile, password)
        result = response.json()
        self.assertEqual(success, result.get("success"))
        self.assertEqual(code, result.get("code"))
        self.assertIn(message, result.get("message"))
