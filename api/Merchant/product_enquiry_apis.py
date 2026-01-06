# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_enquiry_apis.py
# @author   : 李然 
# @Time     :  11:50
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class ProductEnquiryProListApi(BaseMerchantApi):
    """获取列表信息"""
    def __init__(self, page=1, limit=20, name="", status="1", adjust_date_limit="", 
                 category_id="", enquiry_date_limit="", keyword="", create_mode="0", 
                 is_show=None, audit_status="-1", enquiry_result="ALL", mer_id="", 
                 pro_enquiry_result_sort="", sort="", pid="", product_ids=None, 
                 is_all="", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/enquiry/pro/list'
        self.method = 'post'
        
        if product_ids is None:
            product_ids = []
        
        default_data = {
            "page": page,
            "limit": limit,
            "name": name,
            "status": status,
            "adjustDateLimit": adjust_date_limit,
            "categoryId": category_id,
            "enquiryDateLimit": enquiry_date_limit,
            "keyword": keyword,
            "createMode": create_mode,
            "isShow": is_show,
            "auditStatus": audit_status,
            "enquiryResult": enquiry_result,
            "merId": mer_id,
            "proEnquiryResultSort": pro_enquiry_result_sort,
            "sort": sort,
            "pid": pid,
            "productIds": product_ids,
            "isAll": is_all
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductEnquiryRecordListApi(BaseMerchantApi):
    """抽查记录查看"""
    def __init__(self, page=1, limit=10, pid=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/enquiry/record/list?' \
                   f'page={page}&limit={limit}&temp={cur_timestamp}'
        
        if pid:
            self.url += f'&pid={pid}'
        
        self.method = 'get'


class ProductEnquiryAdjustLogApi(BaseMerchantApi):
    """调价查看"""
    def __init__(self, page=1, limit=10, pid=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/enquiry/adjust/log?' \
                   f'page={page}&limit={limit}&temp={cur_timestamp}'
        
        if pid:
            self.url += f'&pid={pid}'
        
        self.method = 'get'


class ProductEnquiryExportSelectFieldsApi(BaseMerchantApi):
    """导出信息选取"""
    def __init__(self, type_val="product_enquiry_export_custom_merchant", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/export/select/fields?' \
                   f'type={type_val}&temp={cur_timestamp}'
        self.method = 'get'


class ProductEnquiryRecordExportApi(BaseMerchantApi):
    """导出全部数据"""
    def __init__(self, page=1, limit=20, name="", status="1", adjust_date_limit="", 
                 category_id="", enquiry_date_limit="", keyword="", create_mode="0", 
                 is_show=None, audit_status="-1", enquiry_result="ALL", mer_id="", 
                 pro_enquiry_result_sort="", sort="", pid="", product_ids=None, 
                 is_all=1, file_name="询价列表_0929_17_01_06", page_start=1, page_end=2303, 
                 export_fields=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/enquiry/record/export'
        self.method = 'post'
        
        if product_ids is None:
            product_ids = []
        
        if export_fields is None:
            export_fields = [
                {
                    "field": "productId",
                    "sort": 59,
                    "fieldName": "商品ID",
                    "selected": 1
                },
                {
                    "field": "productName",
                    "sort": 59,
                    "fieldName": "商品名称",
                    "selected": 2
                },
                {
                    "field": "proBrandModel",
                    "sort": 59,
                    "fieldName": "品牌+型号",
                    "selected": 6
                },
                {
                    "field": "lastEnquiryDate",
                    "sort": 59,
                    "fieldName": "上次询价日期",
                    "selected": 7
                },
                {
                    "field": "lastEnquiryResult",
                    "sort": 59,
                    "fieldName": "上次询价结果",
                    "selected": 8
                },
                {
                    "field": "oneLevelCategoryName",
                    "sort": 59,
                    "fieldName": "一级分类",
                    "selected": 3
                },
                {
                    "field": "twoLevelCategoryName",
                    "sort": 59,
                    "fieldName": "二级分类",
                    "selected": 4
                },
                {
                    "field": "threeLevelCategoryName",
                    "sort": 59,
                    "fieldName": "三级分类",
                    "selected": 5
                }
            ]
        
        default_data = {
            "page": page,
            "limit": limit,
            "name": name,
            "status": status,
            "adjustDateLimit": adjust_date_limit,
            "categoryId": category_id,
            "enquiryDateLimit": enquiry_date_limit,
            "keyword": keyword,
            "createMode": create_mode,
            "isShow": is_show,
            "auditStatus": audit_status,
            "enquiryResult": enquiry_result,
            "merId": mer_id,
            "proEnquiryResultSort": pro_enquiry_result_sort,
            "sort": sort,
            "pid": pid,
            "productIds": product_ids,
            "isAll": is_all,
            "fileName": file_name,
            "pageStart": page_start,
            "pageEnd": page_end,
            "exportFields": export_fields
        }
        
        default_data.update(kwargs)
        self.json = default_data