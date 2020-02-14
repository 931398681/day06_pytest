# 导包
import unittest
import api
from tools.assert_common import assert_common
from parameterized import parameterized
from tools.read_yaml import read_yaml
from api.api_employee import ApiEmployee


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        # 获取ApiEmployee对象
        cls.api = ApiEmployee()

    # 新增员工 接口测试方法
    @parameterized.expand(read_yaml("employee.yaml"))
    def test01_post(self, username, mobile, workNumber):
        # 调用新增员工接口
        r = self.api.api_post_employee(username, mobile, workNumber)
        # 断言
        assert_common(self, r)
        print("新增员工结果：", r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("员工user_id值为：", api.user_id)

    # 修改员工 接口测试方法
    def test02_put(self):
        # 调用修改员工接口
        r = self.api.api_put_employee()
        # 断言
        assert_common(self, r)
        print("修改员工结果：", r.json())

    # 查询员工 接口测试方法
    def test03_get(self):
        # 调用查询员工接口
        r = self.api.api_get_employee()
        # 断言
        assert_common(self, r)
        print("查询员工结果：", r.json())

    # 删除员工 接口测试方法
    def test04_delete(self):
        # 调用删除员工接口
        r = self.api.api_delete_employee()
        print("删除结果为：", r.json())
        # 断言
        assert_common(self, r)
