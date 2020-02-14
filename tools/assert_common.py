def assert_common(self, response,
                  status_code=200,
                  success=True,
                  code=10000,
                  message="操作成功！"):
    """

    :param self: TestCase实例
    :param response: 响应对象
    """
    r = response.json()
    # 断言状态码 200
    self.assertEqual(status_code, response.status_code)
    # 断言seccess  true
    self.assertEqual(success, r.get("success"))
    # 断言code 10000
    self.assertEqual(code, r.get("code"))
    # 断言 msg
    self.assertEqual(message, r.get("message"))
