# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_category_apis.py
# @author   : 李然 
# @Time     :  11:28
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class ProductCategoryAddApi(BaseMerchantApi):
    """新增产品分类【增】"""
    def __init__(self, name="测试商品分类", pid=0, sort=1, icon=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/store/product/category/add'
        self.method = 'post'
        
        default_data = {
            "icon": icon,
            "name": name,
            "pid": pid,
            "sort": sort,
            "id": 0
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductCategoryListApi(BaseMerchantApi):
    """商品分类列表【查】"""
    def __init__(self, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/store/product/category/list?temp={cur_timestamp}'
        self.method = 'get'


class ProductCategoryUpdateApi(BaseMerchantApi):
    """编辑产品分类【改】"""
    def __init__(self, category_id, name="测试商品分类", pid=0, sort=1, icon=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/store/product/category/update'
        self.method = 'post'
        default_data = {
            "icon": icon,
            "name": name,
            "pid": pid,
            "sort": sort,
            "id": category_id
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductCategoryDeleteApi(BaseMerchantApi):
    """删除商品分类【删】"""
    def __init__(self, category_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/store/product/category/delete/{category_id}'
        self.method = 'post'