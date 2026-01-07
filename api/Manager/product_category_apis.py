# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_category_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  15:59
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp, rdm_five_digit


class ProductCategoryAddApi(BaseManagerApi):

    def __init__(self,level):
        """
        添加商品分类
        :param level: 分类级别
        """

        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/category/add'
        self.method = 'post'
        self.json = {
            "icon":"",
            "name":f"新增分类{rdm_five_digit()}",
            "pid":0,
            "sort":0,
            "type":1,
            "url":"",
            "id":0,
            "extra":"",
            "level":level
        }

class ProductCategoryListApi(BaseManagerApi):
    """
    获取商品分类列表
    """
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/category/step/list?productCategoryId=0'
        self.method = 'get'

class ProductCategoryDeleteApi(BaseManagerApi):
    """
    删除商品分类
    :param categoryid: 分类ID
    """
    def __init__(self,categoryid):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/category/delete/{categoryid}'
        self.method = 'post'

class ProductCategoryUpdatelApi(BaseManagerApi):
    """
    获取商品分类详情
    :param categoryid: 分类ID
    """
    def __init__(self,categoryid,level):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/category/update'
        self.method = 'post'
        self.json = {"icon":"https://ceph.huanxin.io:7580/crmebimage/public/product/2025/05/20/efccd48885e542c29217909c5ba8fc9ebopzvkbdqg.png",
                     "name":"礼品",
                     "pid":0,
                     "sort":0,
                     "type":1,
                     "url":"",
                     "id":categoryid,
                     "extra":"",
                     "level":level
                     }