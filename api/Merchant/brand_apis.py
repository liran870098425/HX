# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : brand_apis.py
# @author   : 李然 
# @Time     :  11:52
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp, rdm_five_digit


class BrandListApi(BaseMerchantApi):
    """列表信息获取 Copy Copy"""
    def __init__(self, page=1, limit=20, name="", merchant_id="77", start_time="", 
                 end_time="", date_time="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/brand/list?page={page}&limit={limit}&name={name}&merchantId={merchant_id}&startTime={start_time}&endTime={end_time}&dateTime={date_time}&' \
                   f'temp={cur_timestamp}'
        self.method = 'get'


class BrandTabsHeadersApi(BaseMerchantApi):
    """统计信息获取"""
    def __init__(self, page=1, limit=20, name="", merchant_id="77", start_time="", 
                 end_time="", date_time="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/brand/tabs/headers?' \
                   f'page={page}&limit={limit}&name={name}&merchantId={merchant_id}&' \
                   f'startTime={start_time}&endTime={end_time}&dateTime={date_time}&' \
                   f'temp={cur_timestamp}'
        self.method = 'get'


class BrandAddApi(BaseMerchantApi):
    """添加品牌"""
    def __init__(self, sort=0, icon="", category_id_data=None,
                 category_ids="463", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/plat/product/brand/brand/add'
        self.method = 'post'
        
        if category_id_data is None:
            category_id_data = [463]
        
        default_data = {
            "sort": sort,
            "icon": icon,
            "name": f'品牌名称{rdm_five_digit()}',
            "categoryIdData": category_id_data,
            "categoryIds": category_ids
        }
        
        default_data.update(kwargs)
        self.json = default_data


class BrandAuditResetApi(BaseMerchantApi):
    """取消审核"""
    def __init__(self, brand_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/brand/audit/reset/{brand_id}?temp={cur_timestamp}'
        self.method = 'get'


class BrandUpdateApi(BaseMerchantApi):
    """修改品牌"""
    def __init__(self, brand_id, name="森岛帆高", icon="", reject_reason=None, 
                 status=0, update_time="2025-10-17 13:41:56", category_ids="4823", 
                 category_id_data=None, sort=0, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/plat/product/brand/brand/update'
        self.method = 'post'
        
        if category_id_data is None:
            category_id_data = ["4823"]
        
        default_data = {
            "id": brand_id,
            "icon": icon,
            "name": name,
            "rejectReason": reject_reason,
            "status": status,
            "updateTime": update_time,
            "categoryIds": category_ids,
            "categoryIdData": category_id_data,
            "sort": sort
        }
        
        default_data.update(kwargs)
        self.json = default_data


class BrandDeleteApi(BaseMerchantApi):
    """删除品牌"""
    def __init__(self, brand_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/plat/product/brand/brand/delete/{brand_id}'
        self.method = 'post'