# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import jsonpath

from api.base_api import BaseMerchantApi


class  MerchantLoginApi(BaseMerchantApi):
     def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/merchant/login'
        self.method='post'
        self.json={
            "account": username,
            "pwd": password
        }

if __name__ == '__main__':
    # MerchantLoginApi('admin1','123456').send()
    print(MerchantLoginApi('admin1','123456').send())
    print(jsonpath.jsonpath(MerchantLoginApi('admin1','123456').send().json(),'$.data.token'))
