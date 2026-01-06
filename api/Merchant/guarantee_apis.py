# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : guarantee_apis.py
# @author   : 李然 
# @Time     :  11:47
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class GuaranteeGroupListApi(BaseMerchantApi):
    """模板隐藏"""
    def __init__(self, guarantee_id, status=1, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/list'
        self.method = 'post'
        
        default_data = {
            "id": guarantee_id,
            "status": status
        }
        
        default_data.update(kwargs)
        self.json = default_data


class GuaranteeSearchListApi(BaseMerchantApi):
    """查看添加面板"""
    def __init__(self, keyword="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/plat/product/guarantee/search/list?' \
                   f'keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class GuaranteeGroupAddApi(BaseMerchantApi):
    """添加服务模版"""
    def __init__(self, name="测试", gids=None, sort=0, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/add'
        self.method = 'post'
        
        if gids is None:
            gids = []
        
        default_data = {
            "name": name,
            "gids": gids,
            "sort": sort
        }
        
        default_data.update(kwargs)
        self.json = default_data


class GuaranteeGroupDetailApi(BaseMerchantApi):
    """查看添加面板 Copy"""
    def __init__(self, guarantee_group_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/detail?' \
                   f'id={guarantee_group_id}&temp={cur_timestamp}'
        self.method = 'get'


class GuaranteeGroupEditApi(BaseMerchantApi):
    """修改服务模板"""
    def __init__(self, guarantee_group_id, gids=None, name="cs", sort=0, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/edit'
        self.method = 'post'
        
        if gids is None:
            gids = [11]
        
        default_data = {
            "id": guarantee_group_id,
            "gids": gids,
            "name": name,
            "sort": sort
        }
        
        default_data.update(kwargs)
        self.json = default_data


class GuaranteeGroupIsShowApi(BaseMerchantApi):
    """模板展示"""
    def __init__(self, guarantee_group_id, status=1, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/isShow'
        self.method = 'post'
        
        default_data = {
            "id": guarantee_group_id,
            "status": status
        }
        
        default_data.update(kwargs)
        self.json = default_data


class GuaranteeGroupSaveToDefaultApi(BaseMerchantApi):
    """设置默认模板 Copy Copy"""
    def __init__(self, guarantee_group_id, status=1, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/saveToDefault/{guarantee_group_id}'
        self.method = 'post'
        
        default_data = {
            "id": guarantee_group_id,
            "status": status
        }
        
        default_data.update(kwargs)
        self.json = default_data


class GuaranteeGroupDeleteApi(BaseMerchantApi):
    """删除模板"""
    def __init__(self, guarantee_group_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/guarantee/group/delete/{guarantee_group_id}'
        self.method = 'post'