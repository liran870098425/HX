# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  11:09
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi, BaseManagerApi
from common.random_util import cur_timestamp, rdm_five_digit


class ProductSaveApi(BaseMerchantApi):
    """添加商品【增】"""
    def __init__(self, main_attrId, second_attrId):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/save'
        self.method = 'post'
        # 默认商品数据
        self.json = {
                    "name": f"商品{rdm_five_digit()}",
                    "type": 0,
                    "categoryId": 4876, # 商品分类ID
                    "brandId": 6968,  # 商品品牌ID
                    "cateId": 1139,
                    "labelIds": [
                        1
                    ],
                    "supplierId": 5216,
                    "attrMap": {
                        main_attrId: {
                            "attrId": main_attrId,
                            "attrName": "属性标题",
                            "attrValue": "123"
                    },
                        second_attrId: {
                            "attrId": second_attrId,
                            "attrName": "次要标题",
                            "attrValue": "123"
                    }
                    },
                    "isGroup": 0,
                    "storeModel": "123",
                    "unitName": "123",
                    "isPromoteCommission": True,
                    "sort": 1,
                    "tableShow": 1,
                    "intro": "123",
                    "keyword": "123",
                    "deliveryType": 1,
                    "tempId": 1989,
                    "guaranteeIds": 286,
                    "image": "https://ceph.huanxin.io:7580/crmebimage/public/product/2026/01/06/89c8d307e3af4a94bf8ca6c2216b9a31wplsappkda.jpg",
                    "sliderImage": "[\"https://ceph.huanxin.io:7580/crmebimage/public/product/2026/01/06/82b610ede0814afdbfb6002010efd6964dly81t7kz.png\"]",
                    "specType": False,
                    "attrValue": [
                        {
                            "price": 123,
                            "otPrice": 11,
                            "cost": 2,
                            "quota": 5,
                            "stock": 111,
                            "volume": 1,
                            "weight": 1,
                            "fullCode": "123",
                            "barCode": "123",
                            "attrValue": "{\"规格\":\"默认\"}"
                        }
                    ],
                    "attr": [
                        {
                            "attrName": "规格",
                            "attrValues": "默认"
                        }
                    ],
                    "pickType": "selfDelivery"
                }


class ProductListApi(BaseMerchantApi):
    """商品管理列表【查】"""
    def __init__(self, page=1, limit=20, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/list'
        self.method = 'post'
        
        default_data = {
            "page": page,
            "limit": limit,
            "cateId": "",
            "keywords": "",
            "type": "2",
            "categoryId": None,
            "exportType": "2",
            "productType": "",
            "tempId": "",
            "labelId": "",
            "isAll": 1,
            "batchIds": None,
            "batchSkuNos": None
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductUpdateApi(BaseMerchantApi):
    """编辑商品【改】"""
    def __init__(self, product_id, main_attrId, second_attrId,name="接口自动化测试商品"):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/update'
        self.method = 'post'
        default_data = {
            "isPromoteCommission": True,
            "isGroup": 0,
            "name": name,
            "params": [],
            "intro": "12",
            "keyword": "其他,智能手机,其他智能手机,其他手机通讯,手机通讯其他,3c数码,其他3c数码,3c数码其他,哈哈",
            "cateIds": [],
            "cateId": "",
            "unitName": "12",
            "sort": 1,
            "isShow": False,
            "tempId": 1927,
            "attr": [
                {
                    "attrName": "规格",
                    "attrValues": "默认",
                    "id": 272203
                }
            ],
            "attrValue": [
                {
                    "id": 391216,
                    "productId": 0,
                    "sku": "默认",
                    "stock": 0,
                    "sales": 0,
                    "price": "1.00",
                    "image": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png",
                    "cost": "0.01",
                    "otPrice": "0.01",
                    "weight": "0.00",
                    "volume": "0.00",
                    "brokerage": 0,
                    "brokerageTwo": 0,
                    "type": 0,
                    "quota": 0,
                    "quotaShow": 0,
                    "attrValue": "{\"规格\":\"默认\"}",
                    "minPrice": None,
                    "barCode": "",
                    "expand": "",
                    "cdkeyId": 0,
                    "cdkeyLibraryName": None,
                    "model": "",
                    "brokerageMoney": "0.00",
                    "brokerageRate": "0.00",
                    "purchasePrice": "0",
                    "purchaseQuota": 0,
                    "fullCode": "",
                    "skuNo": "PGPZ-P8P4-PSP4-084K-X5AS"
                }
            ],
            "isSub": False,
            "content": "",
            "specType": False,
            "id": product_id,
            "coupons": [],
            "couponIds": [],
            "brandId": 1,
            "deliveryWay": 2,
            "deliveryFree": 0,
            "refundSwitch": 1,
            "storeModel": "121",
            "categoryId": 463,
            "labelIds": [],
            "supplierName": "其他",
            "attrMap": {
                main_attrId: {
                    "attrId": main_attrId,
                    "attrName": "属性标题",
                    "attrValue": "123"
                },
                second_attrId: {
                    "attrId": second_attrId,
                    "attrName": "次要标题",
                    "attrValue": "123"
                }
            },
            "supplierId": 0,
            "guaranteeIds": "1,3,7,8,9,12",
            "merchantGuaranteeId": 323,
            "type": 0,
            "guaranteeIdsList": [
                1,
                3,
                7,
                8,
                9,
                12
            ],
            "image": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png",
            "sliderImage": "[\"https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png\"]",
            "sliderImages": [
                "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png"
            ],
            "isSquare": True,
            "tableShow": 1,
            "videoLink": "",
            "regionList": None,
            "productHomeProperty": [],
            "url": "",
            "form": 2
        }

        self.json = default_data


class ProductSetLabelApi(BaseMerchantApi):
    """设置商品标签"""
    def __init__(self, label_ids=None, product_ids=None, **kwargs):
        if label_ids is None:
            label_ids = [1]
        if product_ids is None:
            product_ids = []
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/batch/set/label'
        self.method = 'post'
        
        default_data = {
            "labelId": label_ids,
            "pids": product_ids
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductSetFreightTemplateApi(BaseMerchantApi):
    """设置商品运费"""
    def __init__(self, product_id, template_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/set/freight/template'
        self.method = 'post'
        
        default_data = {
            "id": product_id,
            "templateId": template_id
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductSetBrokerageApi(BaseMerchantApi):
    """设置商品佣金"""
    def __init__(self, product_id, brokerage=0, brokerage_two=0, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/set/brokerage'
        self.method = 'post'
        
        default_data = {
            "brokerage": brokerage,
            "brokerageTwo": brokerage_two,
            "id": product_id,
            "idList": []
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductInfoApi(BaseMerchantApi):
    """查看商品详情"""
    def __init__(self, product_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/info/{product_id}'
        self.method = 'get'
        
        # 添加查询参数到URL
        params_str = '&'.join([f'{k}={v}' for k, v in kwargs.items()])
        if params_str:
            self.url += f'?{params_str}'
        else:
            self.url += f'?temp={cur_timestamp}'


class ProductReplyListApi(BaseMerchantApi):
    """查看商品评价"""
    def __init__(self, page=1, limit=20, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/reply/list'
        self.method = 'get'
        
        # 添加查询参数到URL
        default_params = {
            "page": page,
            "limit": limit
        }
        default_params.update(kwargs)
        
        params_str = '&'.join([f'{k}={v}' for k, v in default_params.items() if v is not None])
        self.url += f'?{params_str}&temp={cur_timestamp}'


class ProductUpApi(BaseMerchantApi):
    """上架商品"""
    def __init__(self, product_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/up/{product_id}'
        self.method = 'post'


class ProductDownApi(BaseMerchantApi):
    """下架商品"""
    def __init__(self, product_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/merchant/product/down/{product_id}'
        self.method = 'post'


class ProductExportApi(BaseMerchantApi):
    """导出商品"""
    def __init__(self, product_ids=None, **kwargs):
        if product_ids is None:
            product_ids = []
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/export/export/product'
        self.method = 'post'
        
        default_data = {
            "page": 1,
            "limit": 20,
            "cateId": "",
            "keywords": "",
            "type": "2",
            "categoryId": None,
            "exportType": "3",
            "productType": "",
            "tempId": "",
            "isUsed": "",
            "labelId": "",
            "isAll": 1,
            "batchIds": None,
            "batchSkuNos": None,
            "productIds": product_ids
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductExportQRCodeApi(BaseMerchantApi):
    """导出价签"""
    def __init__(self, product_ids=None, **kwargs):
        if product_ids is None:
            product_ids = []
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/export/product/qrcode'
        self.method = 'post'
        
        default_data = {
            "page": 1,
            "limit": 20,
            "cateId": "",
            "keywords": "",
            "type": "2",
            "categoryId": None,
            "exportType": "3",
            "productType": "",
            "tempId": "",
            "isUsed": "",
            "labelId": "",
            "isAll": 1,
            "batchIds": None,
            "batchSkuNos": None,
            "productIds": product_ids
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductDeleteApi(BaseMerchantApi):
    """删除商品"""
    def __init__(self, product_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/delete'
        self.method = 'post'
        
        default_data = {
            "id": product_id,
            "type": "delete"
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductCollectionApi(BaseMerchantApi):
    """商品采集"""
    def __init__(self, collection_links=None, collection_source="JD", **kwargs):
        if collection_links is None:
            collection_links = []
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/coll-log/batch-add'
        self.method = 'post'
        
        default_data = {
            "type": 0,
            "collectionSource": collection_source,
            "collectionLinks": collection_links
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductCustomExportApi(BaseMerchantApi):
    """自定义导出"""
    def __init__(self, file_name=None, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/export/product/custom'
        self.method = 'post'
        
        if file_name is None:
            file_name = f"商品列表_{cur_timestamp}"
            
        default_data = {
            "page": 1,
            "limit": 20,
            "cateId": "",
            "keywords": "",
            "type": "1",
            "categoryId": None,
            "exportType": "2",
            "productType": "",
            "tempId": "",
            "isUsed": "",
            "labelId": "",
            "isAll": 1,
            "batchIds": None,
            "batchSkuNos": None,
            "productIds": [],
            "fileName": file_name,
            "pageStart": 1,
            "pageEnd": 1,
            "exportFields": [
                {
                    "field": "id",
                    "sort": 1,
                    "fieldName": "商品id",
                    "selected": 0
                },
                {
                    "field": "productCost",
                    "sort": 4,
                    "fieldName": "商品成本价",
                    "selected": 0
                }
            ]
        }
        
        default_data.update(kwargs)
        self.json = default_data