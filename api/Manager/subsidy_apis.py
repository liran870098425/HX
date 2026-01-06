# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : subsidy_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:21
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class GovSubsidyProductPageListApi(BaseManagerApi):
    """国补商品列表查询【查】lcx"""
    def __init__(self, page=1, limit=20, total=0, date_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/product/page/list?' \
                   f'page={page}&limit={limit}&total={total}&dateLimit={date_limit}&temp={cur_timestamp}'
        self.method = 'get'


class GovSubsidyProductDetailApi(BaseManagerApi):
    """国补商品查看详情【查】lcx"""
    def __init__(self, product_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/product/detail?' \
                   f'productId={product_id}&temp={cur_timestamp}'
        self.method = 'get'


class GovSubsidyProductCustomExportApi(BaseManagerApi):
    """国补商品导出【查】lcx"""
    def __init__(self, page=1, limit=20, total=51, date_limit="", file_name="国补商品_0819_13_54_23"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/product/custom/export'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "total": total,
            "dateLimit": date_limit,
            "productIds": [],
            "isAll": 1,
            "fileName": file_name,
            "pageStart": 1,
            "pageEnd": 3,
            "exportFields": [
                {
                    "field": "productId",
                    "sort": 1,
                    "fieldName": "商品ID",
                    "selected": 0
                },
                {
                    "field": "govSubsidyProvince",
                    "sort": 2,
                    "fieldName": "国补省份",
                    "selected": 0
                },
                {
                    "field": "productName",
                    "sort": 3,
                    "fieldName": "商品名称",
                    "selected": 0
                },
                {
                    "field": "price",
                    "sort": 4,
                    "fieldName": "商品售价",
                    "selected": 0
                },
                {
                    "field": "ratio",
                    "sort": 5,
                    "fieldName": "国补比例",
                    "selected": 0
                },
                {
                    "field": "govCategoryName",
                    "sort": 6,
                    "fieldName": "国补品类",
                    "selected": 0
                },
                {
                    "field": "efficiency",
                    "sort": 7,
                    "fieldName": "能效等级",
                    "selected": 0
                },
                {
                    "field": "oneLevelCategoryName",
                    "sort": 8,
                    "fieldName": "一级分类",
                    "selected": 0
                },
                {
                    "field": "twoLevelCategoryName",
                    "sort": 9,
                    "fieldName": "二级分类",
                    "selected": 0
                },
                {
                    "field": "threeLevelCategoryName",
                    "sort": 10,
                    "fieldName": "三级分类",
                    "selected": 0
                },
                {
                    "field": "brandName",
                    "sort": 11,
                    "fieldName": "品牌名称",
                    "selected": 0
                },
                {
                    "field": "supplierName",
                    "sort": 12,
                    "fieldName": "授权厂商",
                    "selected": 0
                },
                {
                    "field": "effectiveTime",
                    "sort": 13,
                    "fieldName": "生效时间",
                    "selected": 0
                }
            ]
        }


class GovSubsidyMerchantPageListApi(BaseManagerApi):
    """查询国补配置列表【查】lcx"""
    def __init__(self, page=1, limit=20, total=5):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/merchant/page/list?' \
                   f'page={page}&limit={limit}&total={total}&temp={cur_timestamp}'
        self.method = 'get'


class GovSubsidyMerchantAddApi(BaseManagerApi):
    """新增国补【增】lcx"""
    def __init__(self, source_mer_id=77, flow_mer_id=77):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/merchant/add'
        self.method = 'post'
        self.json = {
            "govSubsidiesRegion": [],
            "publicSubsidiesRegion": [110000],
            "restrictedReceivingRegion": [],
            "sourceMerId": source_mer_id,
            "effectiveTimeStart": "{{date_recent}}",
            "effectiveTimeEnd": "{{date_soon}}",
            "isAstrict": False,
            "flowMerId": flow_mer_id,
            "excelUrl": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/uploadf/public/marketing/2025/08/19/6e696e80764f403b9fa29ac51a184ccd842nnb5ykj.xls",
            "dataTotalNum": 1
        }


class GovSubsidyMerchantSwitchApi(BaseManagerApi):
    """修改国补状态：开启【改】lcx"""
    def __init__(self, gov_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/merchant/switch?id={gov_id}'
        self.method = 'post'


class GovSubsidyMerchantEditApi(BaseManagerApi):
    """编辑国补【改】lcx"""
    def __init__(self, gov_id, source_mer_id=77, flow_mer_id=77):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/merchant/edit'
        self.method = 'post'
        self.json = {
            "id": gov_id,
            "govSubsidiesRegion": [110000],
            "publicSubsidiesRegion": [110000],
            "sourceMerId": source_mer_id,
            "effectiveTimeStart": "2025-08-19 00:00:00",
            "effectiveTimeEnd": "2025-08-31 00:00:00",
            "isAstrict": False,
            "flowMerId": flow_mer_id,
            "dataTotalNum": 0
        }


class GovSubsidyMerchantCustomExportApi(BaseManagerApi):
    """导出国补配置列表【查】lcx"""
    def __init__(self, page=1, limit=20, total=5, file_name="国补配置_0819_14_56_23"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/merchant/custom/export'
        self.method = 'post'
        self.json = {
            "dateLimit": "",
            "page": page,
            "limit": limit,
            "total": total,
            "govSubsidyIds": [],
            "isAll": 1,
            "fileName": file_name,
            "pageStart": 1,
            "pageEnd": 1,
            "exportFields": [
                {
                    "field": "govSubId",
                    "sort": 1,
                    "fieldName": "国补ID",
                    "selected": 0
                },
                {
                    "field": "govSubsidyProvince",
                    "sort": 2,
                    "fieldName": "国补省份",
                    "selected": 0
                },
                {
                    "field": "govSubsidiesCity",
                    "sort": 3,
                    "fieldName": "国补城市",
                    "selected": 0
                },
                {
                    "field": "sourceMerId",
                    "sort": 4,
                    "fieldName": "商户ID",
                    "selected": 0
                },
                {
                    "field": "sourceMerName",
                    "sort": 5,
                    "fieldName": "商品来源",
                    "selected": 0
                },
                {
                    "field": "effectiveTime",
                    "sort": 6,
                    "fieldName": "生效时间",
                    "selected": 0
                },
                {
                    "field": "restrictedReceivingArea",
                    "sort": 7,
                    "fieldName": "限制收货区域",
                    "selected": 0
                },
                {
                    "field": "enableStatus",
                    "sort": 8,
                    "fieldName": "国补状态(开启/关闭)",
                    "selected": 0
                },
                {
                    "field": "defaultMerName",
                    "sort": 9,
                    "fieldName": "默认流向商户",
                    "selected": 0
                }
            ]
        }