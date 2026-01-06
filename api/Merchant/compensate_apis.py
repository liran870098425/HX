# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : compensate_apis.py
# @author   : 李然 
# @Time     :  13:19
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class AfterOrderCompensateListApi(BaseMerchantApi):
    """带工单编号搜索指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, approval_result=None, compensate_status=None,
                 compensate_times=None, compensate_type="", compensate_way="",
                 create_times=None, mer_id="", order_no="", work_no="", ids=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/compensate/list'
        self.method = 'post'
        
        if compensate_times is None:
            compensate_times = []
        
        if create_times is None:
            create_times = []
        
        if ids is None:
            ids = []
        
        default_data = {
            "page": page,
            "limit": limit,
            "approvalResult": approval_result,
            "compensateStatus": compensate_status,
            "compensateTimes": compensate_times,
            "compensateType": compensate_type,
            "compensateWay": compensate_way,
            "createTimes": create_times,
            "merId": mer_id,
            "orderNo": order_no,
            "workNo": work_no,
            "ids": ids
        }
        
        default_data.update(kwargs)
        self.json = default_data


class AfterOrderCompensateDetailApi(BaseMerchantApi):
    """查看赔付详情【查】lcx"""
    def __init__(self, compensate_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/compensate/detail?' \
                   f'id={compensate_id}&temp={cur_timestamp}'
        self.method = 'get'


class AfterOrderCompensateExportApi(BaseMerchantApi):
    """导出指定数据【查】lcx"""
    def __init__(self, page=1, limit=20, approval_result=None, compensate_status=None,
                 compensate_times=None, compensate_type="", compensate_way="",
                 create_times=None, mer_id="", order_no="", work_no="", ids=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/after/order/compensate/export'
        self.method = 'post'
        
        if compensate_times is None:
            compensate_times = []
        
        if create_times is None:
            create_times = []
        
        if ids is None:
            ids = []
        
        default_data = {
            "page": page,
            "limit": limit,
            "approvalResult": approval_result,
            "compensateStatus": compensate_status,
            "compensateTimes": compensate_times,
            "compensateType": compensate_type,
            "compensateWay": compensate_way,
            "createTimes": create_times,
            "merId": mer_id,
            "orderNo": order_no,
            "workNo": work_no,
            "ids": ids
        }
        
        default_data.update(kwargs)
        self.json = default_data