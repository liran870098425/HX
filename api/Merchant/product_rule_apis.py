# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_rule_apis.py
# @author   : 李然 
# @Time     :  11:30
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class ProductRuleSaveApi(BaseMerchantApi):
    """添加商品规格【增】"""
    def __init__(self, rule_name="接口自动化测试商品规格", rule_value=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/rule/save'
        self.method = 'post'
        
        if rule_value is None:
            rule_value = '[{"value":"1","detail":["1"]}]'
        
        default_data = {
            "id": 0,
            "ruleName": rule_name,
            "ruleValue": rule_value
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductRuleListApi(BaseMerchantApi):
    """商品规格列表【查】"""
    def __init__(self, page=1, limit=20, keywords="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/rule/list?' \
                   f'page={page}&limit={limit}&keywords={keywords}&temp={cur_timestamp}'
        self.method = 'get'


class ProductRuleUpdateApi(BaseMerchantApi):
    """编辑商品规格【改】"""
    def __init__(self, rule_id, rule_name="接口自动化测试商品规格", rule_value=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/rule/update'
        self.method = 'post'
        
        if rule_value is None:
            rule_value = '[{"value":"1","detail":["1"]}]'
        
        default_data = {
            "id": rule_id,
            "ruleName": rule_name,
            "ruleValue": rule_value
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductRuleDeleteApi(BaseMerchantApi):
    """删除商品规格【删】"""
    def __init__(self, rule_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/rule/delete/{rule_id}'
        self.method = 'post'