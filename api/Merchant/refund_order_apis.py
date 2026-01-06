# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : refund_order_apis.py
# @author   : 李然 
# @Time     :  13:08
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class RefundOrderRecListApi(BaseMerchantApi):
    """带退款单号搜索指定数据【查】lcx"""
    def __init__(self, refund_status="9", date_limit="", order_no="", keyword="", 
                 refund_order_no="", page=1, limit=20, sale_no="", is_all="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/refund/order/rec/list?' \
                   f'refundStatus={refund_status}&dateLimit={date_limit}&orderNo={order_no}&' \
                   f'keyword={keyword}&refundOrderNo={refund_order_no}&page={page}&' \
                   f'limit={limit}&saleNo={sale_no}&isAll={is_all}&temp={cur_timestamp}'
        self.method = 'get'


class RefundOrderExcelCustomApi(BaseMerchantApi):
    """导出全部数据【查】lcx"""
    def __init__(self, refund_status="9", date_limit="", order_no="", keyword="", 
                 refund_order_no="", page=1, limit=20, refund_order_ids=None, 
                 sale_no="", refund_order_no_list=None, is_all=1, 
                 file_name="退款单列表_0929_11_16_30", page_start=1, page_end=133, 
                 export_fields=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/refund/order/order/excel/custom'
        self.method = 'post'
        
        if refund_order_ids is None:
            refund_order_ids = []
        
        if refund_order_no_list is None:
            refund_order_no_list = []
        
        if export_fields is None:
            export_fields = [
                {
                    "field": "saleNo",
                    "sort": 1,
                    "fieldName": "售后单号",
                    "selected": 0
                },
                {
                    "field": "refundOrderNo",
                    "sort": 2,
                    "fieldName": "退款单号",
                    "selected": 0
                },
                {
                    "field": "orderNo",
                    "sort": 3,
                    "fieldName": "订单号",
                    "selected": 0
                }
            ]
        
        default_data = {
            "refundStatus": refund_status,
            "dateLimit": date_limit,
            "orderNo": order_no,
            "keyword": keyword,
            "refundOrderNo": refund_order_no,
            "page": page,
            "limit": limit,
            "refundOrderIds": refund_order_ids,
            "saleNo": sale_no,
            "refundOrderNoList": refund_order_no_list,
            "isAll": is_all,
            "fileName": file_name,
            "pageStart": page_start,
            "pageEnd": page_end,
            "exportFields": export_fields
        }
        
        default_data.update(kwargs)
        self.json = default_data