# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : supplier_apis.py
# @author   : 李然 
# @Time     :  11:37
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class SupplierAddAccountApi(BaseMerchantApi):
    """添加供应商账号[增]"""
    def __init__(self, bank_account=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/add/account'
        self.method = 'post'
        
        if bank_account is None:
            bank_account = [
                {
                    "accountNumber": cur_timestamp(),
                    "bankName": "21"
                }
            ]
        
        default_data = {
            "bankAccount": bank_account,
            "supplierName": f"供应商{cur_timestamp()}"
        }
        
        default_data.update(kwargs)
        self.json = default_data


class SupplierAccountListApi(BaseMerchantApi):
    """供应商账号列表【查】"""
    def __init__(self, page=1, limit=20, keyword="", value="1", date_time="", brand_ids="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/account/list?' \
                   f'page={page}&limit={limit}&keyword={keyword}&value={value}&' \
                   f'dateTime={date_time}&brandIds={brand_ids}&temp={cur_timestamp}'
        self.method = 'get'


class SupplierUpdateAccountApi(BaseMerchantApi):
    """编辑供应商站账号【改】"""
    def __init__(self, supplier_id, supplier_name="自动化测试供应商账号", region_id=None, 
                 region_name=None, bank_account=None, supplier_bank_id=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/update/account'
        self.method = 'post'
        
        if bank_account is None:
            if supplier_bank_id:
                bank_account = [
                    {
                        "supplierId": supplier_bank_id,
                        "accountNumber": "6666 666",
                        "bankName": "21"
                    }
                ]
            else:
                bank_account = [
                    {
                        "supplierId": supplier_id,
                        "accountNumber": "6666 666",
                        "bankName": "21"
                    }
                ]
        
        default_data = {
            "supplierId": supplier_id,
            "supplierName": supplier_name,
            "regionId": region_id,
            "regionName": region_name,
            "bankAccount": bank_account
        }
        
        default_data.update(kwargs)
        self.json = default_data


class SupplierDeleteAccountApi(BaseMerchantApi):
    """删除供应商账号【删】"""
    def __init__(self, supplier_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/delete/account'
        self.method = 'post'
        self.json = {
            "supplierId": supplier_id
        }

class SupplierBrandAddApi(BaseMerchantApi):
    """添加供应商品牌【增】"""
    def __init__(self, supplier_id, brand_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/supplier/brand/add'
        self.method = 'post'
        self.json = {
                "town": "",
                "village": "",
                "name": "",
                "phone": "",
                "work": "",
                "city": "",
                "district": "",
                "province": "",
                "supplierName": "",
                "cityCode": 0,
                "townCode": 0,
                "districtCode": 0,
                "provinceCode": 0,
                "userId": "",
                "brandIds": [
                    brand_id # 品牌ID
                ],
                "regionId": "",
                "categoryId": 0,
                "flag": None,
                "supplierId": supplier_id # 供应商ID
            }