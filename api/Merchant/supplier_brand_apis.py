# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : supplier_brand_apis.py
# @author   : 李然 
# @Time     :  11:42
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class SupplierBrandListApi(BaseMerchantApi):
    """查看供应商品牌列表信息"""
    def __init__(self, page=1, limit=20, keyword="", value="1", date_time="", brand_ids="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/brand/list?page={page}&limit={limit}&keyword={keyword}&value={value}&dateTime={date_time}&brandIds={brand_ids}&temp={cur_timestamp}'
        self.method = 'get'


class SupplierBrandInfoApi(BaseMerchantApi):
    """查看品牌信息"""
    def __init__(self, keyword="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/plat/product/brand/brand/list/condition?keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class CityRegionTreeApi(BaseMerchantApi):
    """查看地址信息"""
    def __init__(self, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/city/region/province/city/tree?temp={cur_timestamp}'
        self.method = 'get'


class SupplierBrandGetSupplierListApi(BaseMerchantApi):
    """查看供应商名称信息"""
    def __init__(self, keyword="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/brand/getSupplierList?keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class SupplierBrandEditApi(BaseMerchantApi):
    """修改供应商品牌列表信息"""
    def __init__(self, supplier_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/brand/edit?supplierId={supplier_id}&temp={cur_timestamp}'
        self.method = 'get'


class SupplierBrandDeleteApi(BaseMerchantApi):
    """删除供应商品牌列表信息"""
    def __init__(self, supplier_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/delete/account'
        self.method = 'post'
        default_data = {
            "supplierId": supplier_id
        }
        
        default_data.update(kwargs)
        self.json = default_data