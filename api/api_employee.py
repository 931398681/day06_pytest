import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiEmployee(object):
    # 初始化
    def __init__(self):
        # 新增员工 url
        self.url_post = api.host + "/api/sys/user"
        log.info("新增员工的url:{}".format(self.url_post))
        # 修改员工 url
        self.url_put = api.host + "/api/sys/user/{}"
        # 查询员工 url
        self.url_get = api.host + "/api/sys/user/{}"
        # 删除员工 url
        self.url_delete = api.host + "/api/sys/user/{}"
        log.info("新增 修改 删除员工的url:{}".format(self.url_delete))
    # 新增员工
    def api_post_employee(self, username, mobile, workNumber):
        # 请求参数数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}
        log.info("新增员工的url:{} 新增员工的数据：{} 新增员工的请求头：{}".format(self.url_post.format(api.user_id), data,api.headers))
        # 调用post方法->返回响应对象
        return requests.post(url=self.url_post, json=data, headers=api.headers)

    # 修改员工
    def api_put_employee(self):
        # 请求参数数据
        data = {"username": "wc001"}
        log.info("修改员工的url:{} 修改员工的数据：{} 修改员工的请求头：{}".format(self.url_put.format(api.user_id), data, api.headers))
        # 调用put方法->返回响应对象
        return requests.put(url=self.url_put.format(api.user_id), json=data, headers=api.headers)

    # 查询员工
    def api_get_employee(self):
        log.info("查询员工的url:{} 查询员工的请求头：{}".format(self.url_get.format(api.user_id), api.headers))
        # 调用get方法->返回响应对象
        return requests.get(url=self.url_get.format(api.user_id), headers=api.headers)

    # 删除员工
    def api_delete_employee(self):
        log.info("删除员工的url:{} 删除员工的请求头：{}".format(self.url_delete.format(api.user_id),api.headers))
        # 调用delete方法->返回响应对象
        return requests.delete(url=self.url_delete.format(api.user_id), headers=api.headers)
