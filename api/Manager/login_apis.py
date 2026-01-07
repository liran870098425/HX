# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import jsonpath

from api.base_api import  BaseManagerApi


class ManagerLoginApi(BaseManagerApi):

    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/login'
        self.method='post'
        self.json={
            "account": username,
            "pwd": password,
            "key": "c75cb14027eef222346411520938688f",
            "code": "",
            "captcha": {
                "captchaVerification": "",
                "secretKey": "",
                "token": ""
            }
        }

if __name__ == '__main__':
    print(jsonpath.jsonpath(ManagerLoginApi('admin', '123456').send().json(), '$..token'))

