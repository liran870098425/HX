# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : refund_order_issue_apis.py
# @author   : 李然 
# @Time     :  13:13
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class RefundOrderIssueListApi(BaseMerchantApi):
    """带工单编号搜索指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, date_limit="", status="-1", order_no="", work_no=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/refund/issue/list?page={page}&limit={limit}&dateLimit={date_limit}&status={status}&' \
                   f'orderNo={order_no}&workNo={work_no}&temp={cur_timestamp}'
        self.method = 'get'


class RefundOrderIssueOrderDetailApi(BaseMerchantApi):
    """查看退款问题单详情【查】lcx"""
    def __init__(self, work_no=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/refund/issue/order/detail?workNo={work_no}&temp={cur_timestamp}'
        self.method = 'get'


class RefundOrderIssueExportApi(BaseMerchantApi):
    """导出指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, date_limit="", status=-1, order_no="", work_no="", work_no_list=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/refund/issue/export'
        self.method = 'post'
        
        if work_no_list is None:
            work_no_list = []
        
        default_data = {
            "page": page,
            "limit": limit,
            "dateLimit": date_limit,
            "status": status,
            "orderNo": order_no,
            "workNo": work_no,
            "workNoList": work_no_list
        }
        
        default_data.update(kwargs)
        self.json = default_data