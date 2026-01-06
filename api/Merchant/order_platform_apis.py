# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : order_platform_apis.py
# @author   : 李然 
# @Time     :  11:57
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class OrderRecListApi(BaseMerchantApi):
    """带订单号搜索指定数据【查】lcx"""
    def __init__(self, key_word="", limit=20, order_no="", product_id="", order_time=None,
                 page=1, paid="", pay_type=None, refund_no="", refund_time=None,
                 region_id=None, status="all", refund_status=None, status_list=None,
                 supplier_ids=None, brand_ids=None, user_key_word="", finance_push_status="",
                 finance_pay_status="", coupon_id="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/rec/list'
        self.method = 'post'
        
        if pay_type is None:
            pay_type = []
        if refund_time is None:
            refund_time = []
        if region_id is None:
            region_id = []
        if refund_status is None:
            refund_status = []
        if status_list is None:
            status_list = []
        if supplier_ids is None:
            supplier_ids = []
        if brand_ids is None:
            brand_ids = []
        
        default_data = {
            "keyWord": key_word,
            "limit": limit,
            "orderNo": order_no,
            "productId": product_id,
            "orderTime": order_time,
            "page": page,
            "paid": paid,
            "payType": pay_type,
            "refundNo": refund_no,
            "refundTime": refund_time,
            "regionId": region_id,
            "status": status,
            "refundStatus": refund_status,
            "statusList": status_list,
            "supplierIds": supplier_ids,
            "brandIds": brand_ids,
            "userKeyWord": user_key_word,
            "financePushStatus": finance_push_status,
            "financePayStatus": finance_pay_status,
            "couponId": coupon_id
        }
        
        default_data.update(kwargs)
        self.json = default_data


class OrderInfoApi(BaseMerchantApi):
    """查看订单详情【查】lcx"""
    def __init__(self, order_no, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/info/{order_no}?temp={cur_timestamp}'
        self.method = 'get'


class OrderFinancePushApi(BaseMerchantApi):
    """订单推送信息【改】lcx"""
    def __init__(self, order_no, product_id, purchase_price="1", freight_fee="1", 
                 push_remark="1", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/finance/push/push'
        self.method = 'post'
        
        default_data = {
            "purchasePrice": purchase_price,
            "freightFee": freight_fee,
            "pushRemark": push_remark,
            "orderNo": order_no,
            "productId": product_id
        }
        
        default_data.update(kwargs)
        self.json = default_data


class OrderFinancePushCancelApi(BaseMerchantApi):
    """取消订单推送信息【改】lcx"""
    def __init__(self, order_no, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/finance/push/cancel'
        self.method = 'post'
        
        default_data = {
            "orderNo": order_no
        }
        
        default_data.update(kwargs)
        self.json = default_data


class OrderPrintReceiptApi(BaseMerchantApi):
    """更多操作：打印小票【改】lcx"""
    def __init__(self, order_no, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/printreceipt/{order_no}?temp={cur_timestamp}'
        self.method = 'get'


class OrderMarkApi(BaseMerchantApi):
    """更多操作：添加备注【改】lcx"""
    def __init__(self, order_no, remark="测试备注", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/order/mark'
        self.method = 'post'
        
        default_data = {
            "remark": remark,
            "orderNo": order_no
        }
        
        default_data.update(kwargs)
        self.json = default_data


class OrderExportExcelRecCustomApi(BaseMerchantApi):
    """导出全部数据【查】lcx"""
    def __init__(self, key_word="", limit=20, order_no="", product_id="", order_time=None,
                 page=1, paid="", pay_type=None, refund_no="", refund_time=None,
                 region_id=None, status="all", refund_status=None, status_list=None,
                 supplier_ids=None, brand_ids=None, user_key_word="", finance_push_status="",
                 finance_pay_status="", coupon_id="", order_id_list=None, 
                 file_name="订单列表_0929_10_01_58", page_start=1, page_end=1099, 
                 export_fields=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/export/order/excel/rec/custom'
        self.method = 'post'
        
        if pay_type is None:
            pay_type = []
        if refund_time is None:
            refund_time = []
        if region_id is None:
            region_id = []
        if refund_status is None:
            refund_status = []
        if status_list is None:
            status_list = []
        if supplier_ids is None:
            supplier_ids = []
        if brand_ids is None:
            brand_ids = []
        if order_id_list is None:
            order_id_list = []
        if export_fields is None:
            export_fields = [
                {
                    "field": "orderNo",
                    "sort": 1,
                    "fieldName": "订单号",
                    "selected": 0
                },
                {
                    "field": "consigneeName",
                    "sort": 2,
                    "fieldName": "收货人",
                    "selected": 0
                },
                {
                    "field": "productName",
                    "sort": 3,
                    "fieldName": "商品信息",
                    "selected": 0
                }
            ]
        
        default_data = {
            "keyWord": key_word,
            "limit": limit,
            "orderNo": order_no,
            "productId": product_id,
            "orderTime": order_time,
            "page": page,
            "paid": paid,
            "payType": pay_type,
            "refundNo": refund_no,
            "refundTime": refund_time,
            "regionId": region_id,
            "status": status,
            "refundStatus": refund_status,
            "statusList": status_list,
            "supplierIds": supplier_ids,
            "brandIds": brand_ids,
            "userKeyWord": user_key_word,
            "financePushStatus": finance_push_status,
            "financePayStatus": finance_pay_status,
            "couponId": coupon_id,
            "orderIdList": order_id_list,
            "fileName": file_name,
            "pageStart": page_start,
            "pageEnd": page_end,
            "exportFields": export_fields
        }
        
        default_data.update(kwargs)
        self.json = default_data