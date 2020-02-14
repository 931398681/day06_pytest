# 导包
import unittest
import api
from tools.assert_common import assert_common
from parameterized import parameterized
from tools.read_yaml import read_yaml
from api.api_login import ApiLogin



# 新建测试类 继承unittest.TestCase
class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 获取ApiLogin对象
        self.login = ApiLogin()

    # 登录测试接口方法
    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, mobile, password):
        # 调用登录接口
        result = self.login.api_login(mobile, password)
        print("登录结果：", result.json())
        r = result.json()
        # 断言
        assert_common(self, result)
        # 提取token
        token = r.get("data")
        # 追加到公共变量 headers
        api.headers["Authorization"] = "Bearer " + token
        print("追加token后的headers为：", api.headers)
