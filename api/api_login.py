# 导包
import api
import requests
from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiLogin(object):
    # 初始化
    def __init__(self):
        # 组装 登录url
        self.url_login = api.host + "/api/sys/login"
        log.info("登录url：{}".format(self.url_login))
    # 登录接口封装
    def api_login(self, mobile, password):
        # 定义测试数据
        data = {"mobile": mobile, "password": password}
        log.info("登录的数据:{} 登录的请求头：{}".format(data,api.headers))
        # 调用post方法 将响应对象返回
        return requests.post(url=self.url_login, json=data, headers=api.headers)
