# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : delivery_apis.py
# @author   : 李然 
# @Time     :  13:17
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class SelfDeliveryListApi(BaseMerchantApi):
    """带订单号搜索指定数据【查】lcx"""
    def __init__(self, order_no="", start_time="", end_time="", page=1, limit=20, 
                 keyword="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/self/delivery/list?' \
                   f'orderNo={order_no}&startTime={start_time}&endTime={end_time}&' \
                   f'page={page}&limit={limit}&keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class SelfDeliveryCompleteApi(BaseMerchantApi):
    """重新配送【改】lcx"""
    def __init__(self, order_no, status=6, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/self/delivery/complete'
        self.method = 'post'
        
        default_data = {
            "orderNo": order_no,
            "status": status
        }
        
        default_data.update(kwargs)
        self.json = default_data


class SelfDeliveryExportApi(BaseMerchantApi):
    """导出指定数据【查】lcx"""
    def __init__(self, page=1, order_id_list=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/self/delivery/export'
        self.method = 'post'
        
        if order_id_list is None:
            order_id_list = []
        
        default_data = {
            "page": page,
            "orderIdList": order_id_list
        }
        
        default_data.update(kwargs)
        self.json = default_data