# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : after_order_apis.py
# @author   : 李然 
# @Time     :  11:59
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class AfterOrderListApi(BaseMerchantApi):
    """带售后单号搜索指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, date_limit="", sale_no="", keywords="", 
                 order_no="", paid="", after_sales_type="", user_info="", 
                 processing_state="9", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/list?' \
                   f'page={page}&limit={limit}&dateLimit={date_limit}&saleNo={sale_no}&' \
                   f'keywords={keywords}&orderNo={order_no}&paid={paid}&' \
                   f'afterSalesType={after_sales_type}&userInfo={user_info}&' \
                   f'processingState={processing_state}&temp={cur_timestamp}'
        self.method = 'get'


class AfterOrderExportApi(BaseMerchantApi):
    """导出指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, date_limit="", sale_no="", keywords="", 
                 order_no="", paid="", after_sales_type="", user_info="", 
                 processing_state=9, sale_nos=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/export'
        self.method = 'post'
        
        if sale_nos is None:
            sale_nos = []
        
        default_data = {
            "page": page,
            "limit": limit,
            "dateLimit": date_limit,
            "saleNo": sale_no,
            "keywords": keywords,
            "orderNo": order_no,
            "paid": paid,
            "afterSalesType": after_sales_type,
            "userInfo": user_info,
            "processingState": processing_state,
            "saleNos": sale_nos
        }
        
        default_data.update(kwargs)
        self.json = default_data