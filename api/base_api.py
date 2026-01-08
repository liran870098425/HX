# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
from common.client import RequestsClient
from common.file_load import load_yaml_file
from paths_manager import http_yaml_path


# 买家服务基类
class BaseBuyerApi(RequestsClient):
    # 这里定义的全局性的类属性，来代表token，在任何地方用token都是同一个
    # token赋值必须在其他接口调用之前完成，最终会在自定义的fixture里完成赋值
    buyer_token = ''
    uid = ''
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)['buyer']
        self.headers = {
            "Authorization": BaseBuyerApi.buyer_token
        }

# 商家服务基类
class BaseMerchantApi(RequestsClient):
    # 这里定义的全局性的类属性，来代表token，在任何地方用token都是同一个
    # token赋值必须在其他接口调用之前完成，最终会在自定义的fixture里完成赋值
    Merchant_token = ''
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)['seller']
        self.headers = {
            "authori-zation": BaseMerchantApi.Merchant_token,
            "Content-Type": "application/json"
        }

# 后台服务基类
class BaseManagerApi(RequestsClient):
    # 这里定义的全局性的类属性，来代表token，在任何地方用token都是同一个
    # token赋值必须在其他接口调用之前完成，最终会在自定义的fixture里完成赋值
    manager_token = ''
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)['manager']
        self.headers = {
            "authori-zation": BaseManagerApi.manager_token,
            "Content-Type": "application/json",
            # "referer": "https://test01-platform.huanxin.io:3443/vue2/marketing/platformCoupon/creatCouponPro",
            'origin':"https://test01-platform.huanxin.io:3443"
        }

# 基础服务基类
class BaseBasicApi(RequestsClient):

    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)['basic']