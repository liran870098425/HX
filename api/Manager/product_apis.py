# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:21
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp, rdm_five_digit


class ProductListApi(BaseManagerApi):
    """根据商品id查询【查】"""
    def __init__(self, page=1, limit=20, category_id=None, keywords="", type="1", is_self=None, mer_id=None, product_id=None):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/list?page={page}&limit={limit}'
        self.method = 'post'
        batch_ids = [product_id] if product_id else []
        self.json = {
            "page": page,
            "limit": limit,
            "categoryId": category_id,
            "keywords": keywords,
            "type": type,
            "isSelf": is_self,
            "merId": mer_id,
            "batchIds": batch_ids,
            "batchSkuNos": None
        }


class ProductUpdateApi(BaseManagerApi):
    """编辑商品，将库存改成10【改】"""
    def __init__(self, product_id, ficti=10, rank=0):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/update'
        self.method = 'post'
        self.json = {
            "id": product_id,
            "ficti": ficti,
            "rank": rank
        }


class ProductInfoApi(BaseManagerApi):
    """查看详情【查】"""
    def __init__(self, product_id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/info/{product_id}?temp={cur_timestamp}'
        self.method = 'get'


class ProductSubsidyCouponApi(BaseManagerApi):
    """查看补贴设置【查】"""
    def __init__(self, product_id, page=1, limit=10):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/getProdSubCoupon?' \
                   f'limit={limit}&page={page}&productId={product_id}&temp={cur_timestamp}'
        self.method = 'get'


class ProductReplyListApi(BaseManagerApi):
    """查看商品评论列表【查】"""
    def __init__(self, page=1, limit=20, is_reply="", date_limit="", nickname="", keyword="", 
                 is_del="false", is_all="1", uid=""):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/reply/list?' \
                   f'page={page}&limit={limit}&isReply={is_reply}&dateLimit={date_limit}&' \
                   f'nickname={nickname}&keyword={keyword}&isDel={is_del}&isAll={is_all}&' \
                   f'uid={uid}&temp={cur_timestamp}'
        self.method = 'get'


class ProductGuaranteeListApi(BaseManagerApi):
    """查询保障服务列表"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/guarantee/list?temp={cur_timestamp}'
        self.method = 'get'


class ProductGuaranteeAddApi(BaseManagerApi):
    """新增保障服务【增】"""
    def __init__(self,sort=0):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/guarantee/add'
        self.method = 'post'
        self.json = {
            "id": 0,
            "name": f'自动化新增保障服务条款{rdm_five_digit()}',
            "content": "这是服务条款的描述",
            "icon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncaiProductCate/2025/08/15/b4e3b07069ac4f8eaa92ab977a567221k4p03qvhfg.png",
            "sort": sort
        }


class ProductGuaranteeUpdateApi(BaseManagerApi):
    """编辑保障服务【改】"""
    def __init__(self, guarantee_id, name="新增保障服务条款-修改", 
                 content="这是服务条款的描述", 
                 icon="https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncaiProductCate/2025/08/15/b4e3b07069ac4f8eaa92ab977a567221k4p03qvhfg.png", 
                 sort=0):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/guarantee/update'
        self.method = 'post'
        self.json = {
            "id": guarantee_id,
            "name": name,
            "content": content,
            "icon": icon,
            "sort": sort
        }


class ProductGuaranteeDeleteApi(BaseManagerApi):
    """删除保障服务【删】"""
    def __init__(self, guarantee_id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/guarantee/delete/{guarantee_id}'
        self.method = 'post'


class ProductBrandAddApi(BaseManagerApi):
    """新增品牌【增】"""
    def __init__(self, name="自动化新增品牌", sort=1, icon="", category_id_data=None):
        if category_id_data is None:
            category_id_data = [4785]
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/brand/add'
        self.method = 'post'
        self.json = {
            "sort": sort,
            "icon": icon,
            "name": name,
            "categoryIdData": category_id_data,
            "categoryIds": ",".join(map(str, category_id_data))
        }


class ProductBrandListApi(BaseManagerApi):
    """品牌列表查询"""
    def __init__(self, page=1, limit=20, name="", date_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/brand/list?' \
                   f'page={page}&limit={limit}&name={name}&dateLimit={date_limit}&temp={cur_timestamp}'
        self.method = 'get'


class ProductBrandUpdateApi(BaseManagerApi):
    """编辑品牌【改】"""
    def __init__(self, brand_id, name="自动化新增品牌-编辑", icon="", sort=1, is_show=True):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/brand/update'
        self.method = 'post'
        self.json = {
            "id": brand_id,
            "name": name,
            "icon": icon,
            "sort": sort,
            "isShow": is_show,
            "categoryIdData": ["4785"],
            "categoryIds": "4785"
        }


class ProductBrandDeleteApi(BaseManagerApi):
    """删除品牌【删】"""
    def __init__(self, brand_id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/product/brand/delete/{brand_id}'
        self.method = 'post'


class ProductTagSaveApi(BaseManagerApi):
    """新增标签【增】"""
    def __init__(self, tag_name="自动化", tag_note="这是说明", sort=1, play_products="141495"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/producttag/save'
        self.method = 'post'
        self.json = {
            "tagName": tag_name,
            "timerange": ["{{date_recent}}", "{{date_soon}}"],
            "sort": sort,
            "playType": "product",
            "playProducts": play_products,
            "position": 0,
            "proBrandList": [
                {
                    "id": 141495,
                    "image": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/07/28/49dbec69cc9347359fca6471ab3d32859g34p7e7mf.jpg",
                    "name": "自动化测试专用商品（勿动）",
                    "price": "100.00",
                    "stock": 29962,
                    "isShow": True,
                    "specType": True,
                    "merName": "焕新生活",
                    "merCategoryId": None,
                    "categoryId": 4785,
                    "merStarLevel": 4,
                    "categoryName": "测试三级",
                    "brandId": 6888,
                    "attrValue": [
                        {
                            "id": 390557,
                            "productId": 141495,
                            "sku": "大号【50*40*50cm】,蓝色条纹【110L】2个装",
                            "stock": 9962,
                            "sales": 38,
                            "price": "100.00",
                            "image": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/07/28/49dbec69cc9347359fca6471ab3d32859g34p7e7mf.jpg",
                            "cost": "80.00",
                            "barCode": "",
                            "otPrice": "90.00",
                            "weight": "0.00",
                            "volume": "0.00",
                            "brokerage": 0,
                            "brokerageTwo": 0,
                            "type": 0,
                            "quota": 0,
                            "quotaShow": 0,
                            "attrValue": "{\"尺寸\":\"大号【50*40*50cm】\",\"颜色分类\":\"蓝色条纹【110L】2个装\"}",
                            "isDel": False,
                            "version": 68,
                            "masterId": 0,
                            "isCallback": False,
                            "expand": "",
                            "cdkeyId": 0,
                            "model": "",
                            "brokerageMoney": "0.00",
                            "brokerageRate": "0.00",
                            "procurePrice": "0.00",
                            "procureLowNum": 0,
                            "fullCode": "",
                            "skuNo": "J5PJ-JHPJ-JDPJ-082Q-M0L8"
                        }
                    ],
                    "sales": 38,
                    "ficti": 41,
                    "unitName": "件",
                    "amount": "0.00",
                    "ratio": "0.00"
                }
            ],
            "status": 0,
            "tagNote": tag_note,
            "startTime": "{{date_recent}}",
            "endTime": "{{date_soon}}"
        }


class ProductTagListApi(BaseManagerApi):
    """查看商品标签列表页【查】"""
    def __init__(self, page=1, limit=20, keywords=""):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/producttag/list?' \
                   f'page={page}&limit={limit}&keywords={keywords}&temp={cur_timestamp}'
        self.method = 'get'


class ProductTagUpdateApi(BaseManagerApi):
    """编辑商品标签【改】"""
    def __init__(self, tag_id, tag_name="修改标签", tag_note="这是标签说明", sort=1, play_products="122466"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/producttag/update?temp={cur_timestamp}'
        self.method = 'post'
        self.json = {
            "id": tag_id,
            "tagName": tag_name,
            "tagNote": tag_note,
            "sort": sort,
            "status": 0,
            "startTime": "{{date_recent}}",
            "endTime": "{{date_soon}}",
            "position": 0,
            "playType": "product",
            "playProducts": play_products,
            "owner": 1,
            "createTime": "{{date_recent}}",
            "updateTime": "{{date_soon}}",
            "timerange": ["{{date_recent}}", "{{date_soon}}"],
            "data": play_products
        }


class ProductTagDeleteApi(BaseManagerApi):
    """删除标签【删】"""
    def __init__(self, tag_id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/producttag/delete/{tag_id}?temp={cur_timestamp}'
        self.method = 'get'


class DictInfoUpdateApi(BaseManagerApi):
    """编辑词条【改】"""
    def __init__(self, dict_id, word="测试1,测试2,测试3修改", brand_id="449", brand_name="鲁比亚", 
                 category_id="4783,4785", category_name="测试二级, 测试三级"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/dictinfo/insertorupdate'
        self.method = 'post'
        self.json = {
            "id": dict_id,
            "word": word,
            "relatedKeywords": None,
            "type": 0,
            "brandId": brand_id,
            "brandName": brand_name,
            "categoryId": category_id,
            "categoryName": category_name,
            "brandIds": [brand_id]
        }


class DictInfoListApi(BaseManagerApi):
    """查询商品词库列表【查】"""
    def __init__(self, page=1, limit=15, is_del="", record_no="", status="vocabulary", type="0", brand_id=""):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/dictinfo/list?' \
                   f'limit={limit}&page={page}&isDel={is_del}&recordNo={record_no}&' \
                   f'status={status}&type={type}&brandId={brand_id}&temp={cur_timestamp}'
        self.method = 'get'


class DictInfoDeleteApi(BaseManagerApi):
    """删除词条【删】"""
    def __init__(self, dict_id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/dictinfo/delete?id={dict_id}&temp={cur_timestamp}'
        self.method = 'get'


class SplitCommProductListApi(BaseManagerApi):
    """根据商品id查询分销商品【查】"""
    def __init__(self, product_id, page=1, limit=20, total=1):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProduct/list?' \
                   f'keywords={product_id}&page={page}&limit={limit}&total={total}&temp={cur_timestamp}'
        self.method = 'get'


class SplitCommProGroupAddApi(BaseManagerApi):
    """添加分佣分组【增】"""
    def __init__(self, group_name="自动化添加分组"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/add'
        self.method = 'post'
        self.json = {
            "groupName": group_name,
            "idDel": False
        }


class SplitCommProGroupListApi(BaseManagerApi):
    """获取分佣分组，取刚刚新建的分组id【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/getGroupDropList?temp={cur_timestamp}'
        self.method = 'get'


class SplitCommProductEditApi(BaseManagerApi):
    """编辑分佣商品-关联新建的分组【改】"""
    def __init__(self, group_id, product_id=141495):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProduct/edit'
        self.method = 'post'
        self.json = {
            "groupId": group_id,
            "rightsDetails": [
                {
                    "rightsId": 160,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "渠道正式",
                    "copyRatio": "5.00",
                    "currentRatio": 5,
                    "currentSum": None,
                    "copySecondRatio": "10.00",
                    "currentSecondRatio": 10
                },
                {
                    "rightsId": 144,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "街道见习",
                    "copyRatio": "10.00",
                    "currentRatio": 10,
                    "currentSum": None,
                    "copySecondRatio": "0.00",
                    "currentSecondRatio": 0
                },
                {
                    "rightsId": 145,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "普通用户",
                    "copyRatio": "1.00",
                    "currentRatio": 1,
                    "currentSum": None,
                    "copySecondRatio": "1.00",
                    "currentSecondRatio": 1
                },
                {
                    "rightsId": 162,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "分佣商品分组",
                    "copyRatio": "10.00",
                    "currentRatio": 10,
                    "currentSum": None,
                    "copySecondRatio": "10.00",
                    "currentSecondRatio": 10
                },
                {
                    "rightsId": 135,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "校园推广-金5.14",
                    "copyRatio": "20.00",
                    "currentRatio": 20,
                    "currentSum": None,
                    "copySecondRatio": "10.00",
                    "currentSecondRatio": 10
                },
                {
                    "rightsId": 167,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "去",
                    "copyRatio": "1.00",
                    "currentRatio": 1,
                    "currentSum": None,
                    "copySecondRatio": "1.00",
                    "currentSecondRatio": 1
                },
                {
                    "rightsId": 154,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "渠道网格员",
                    "copyRatio": "11.00",
                    "currentRatio": 11,
                    "currentSum": None,
                    "copySecondRatio": "20.00",
                    "currentSecondRatio": 20
                },
                {
                    "rightsId": 155,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "战友推广",
                    "copyRatio": "20.00",
                    "currentRatio": 20,
                    "currentSum": None,
                    "copySecondRatio": "15.00",
                    "currentSecondRatio": 15
                },
                {
                    "rightsId": 140,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "校园网格员",
                    "copyRatio": "20.00",
                    "currentRatio": 20,
                    "currentSum": None,
                    "copySecondRatio": "15.00",
                    "currentSecondRatio": 15
                },
                {
                    "rightsId": 94,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "街道推广-正式",
                    "copyRatio": "20.00",
                    "currentRatio": 20,
                    "currentSum": None,
                    "copySecondRatio": "10.00",
                    "currentSecondRatio": 10
                },
                {
                    "rightsId": 159,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "戎光惠推广权益",
                    "copyRatio": "1.00",
                    "currentRatio": 1,
                    "currentSum": None,
                    "copySecondRatio": "0.00",
                    "currentSecondRatio": 0
                },
                {
                    "rightsId": 143,
                    "rightsTypeId": 3,
                    "roleId": None,
                    "rightsType": "all_product",
                    "rightsName": "街道网格员",
                    "copyRatio": "15.00",
                    "currentRatio": 15,
                    "currentSum": None,
                    "copySecondRatio": "10.00",
                    "currentSecondRatio": 10
                }
            ],
            "productId": product_id
        }


class SplitCommProGroupAddServiceApi(BaseManagerApi):
    """添加商品分组【增】"""
    def __init__(self, group_name="自动化添加商品分组", product_id=None):
        if product_id is None:
            product_id = [141495]
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/addService'
        self.method = 'post'
        self.json = {
            "groupName": group_name,
            "enableStatus": True,
            "productIds": product_id
        }


class SplitCommProGroupListPageApi(BaseManagerApi):
    """查询商品分组列表页【查】"""
    def __init__(self, page=1, limit=20, total=9):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/list?' \
                   f'page={page}&limit={limit}&total={total}&createTimeList=,&temp={cur_timestamp}'
        self.method = 'get'


class SplitCommProGroupDetailProductListApi(BaseManagerApi):
    """查询分组关联的商品【查】"""
    def __init__(self, group_id, page=1, limit=20, total=0):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/detailProductList?' \
                   f'page={page}&limit={limit}&total={total}&groupId={group_id}&temp={cur_timestamp}'
        self.method = 'get'


class SplitCommProGroupEditServiceGroupProductApi(BaseManagerApi):
    """移除分组中的商品【改】"""
    def __init__(self, group_id, product_id=None):
        if product_id is None:
            product_id = [141495]
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/splitCommProGroup/editServiceGroupProduct'
        self.method = 'post'
        self.json = {
            "id": group_id,
            "productIds": product_id
        }


class MerchantBrandListApi(BaseManagerApi):
    """查询商户品牌列表页（待审核）【查】"""
    def __init__(self, page=1, limit=20, name="", status="1"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/merchant/brand/list'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "name": name,
            "startTime": None,
            "endTime": None,
            "status": status,
            "merchantId": None
        }


class MerchantBrandUpdateApi(BaseManagerApi):
    """商户品牌审核通过（由于该数据是从商户端新建的且目前有3000多条数据，所以目前先使用现有的数据去测试，后续再改成从商户端新建）【改】"""
    def __init__(self, brand_id, text="审核通过咯"):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/merchant/brand/update/show'
        self.method = 'post'
        self.json = {
            "ids": [brand_id],
            "status": 2,
            "text": text
        }