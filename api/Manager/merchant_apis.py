# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : merchant_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:21
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class MerchantCategoryAddApi(BaseMerchantApi):
    """添加商户分类【增】"""
    def __init__(self, name="自动化测试添加商户分类", handling_fee=0):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/category/add'
        self.method = 'post'
        self.json = {
            "id": 0,
            "name": name,
            "handlingFee": handling_fee
        }


class MerchantCategoryListApi(BaseMerchantApi):
    """查询商户分类列表【查】"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/category/list?' \
                   f'page={page}&limit={limit}&temp={cur_timestamp}'
        self.method = 'get'


class MerchantCategoryUpdateApi(BaseMerchantApi):
    """修改商户分类【改】"""
    def __init__(self, category_id, name="自动化添加商户分类改", handling_fee=0):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/category/update'
        self.method = 'post'
        self.json = {
            "id": category_id,
            "name": name,
            "handlingFee": handling_fee
        }


class MerchantCategoryDeleteApi(BaseMerchantApi):
    """删除商户分类【删】"""
    def __init__(self, category_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/category/delete/{category_id}'
        self.method = 'post'


class MerchantAddApi(BaseMerchantApi):
    """新增国企【增】"""
    def __init__(self, name="自动化新增国企", mer_account=None, company_name="这是企业名称"):
        if mer_account is None:
            mer_account = f"shanghuzhanghao{cur_timestamp}"
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/add'
        self.method = 'post'
        self.json = {
            "merchantCompanyInfoRequest": {
                "companyName": company_name,
                "companyNature": "有限责任公司",
                "registeredCapital": "100",
                "companyAddress": "这是企业地址",
                "billLevelId": None,
                "status": 1,
                "companyIfMoney": True,
                "companyMoneyPeriod": None,
                "isContributingAccount": False,
                "taxCompanyName": "",
                "taxNumber": "1234AB",
                "taxBankOpen": "",
                "taxBankAccount": None,
                "taxRegisterCertImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/09/71b545359da54228bb2b074d50e17389f1wsaxihaz.jpg",
                "merId": "",
                "cardFront": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/system/2025/09/09/7a932420ec8c494d941c31a5af02da6115jm7951q2.png",
                "cardSide": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/system/2025/09/09/1d8c1e51f1134103baba5d9deda58c4cutq0lf25lb.png",
                "validity": "2025-09-09,2025-09-24",
                "businessScope": "经营范围",
                "userName": "这是法人姓名"
            },
            "merchantCutInfoRequest": {
                "cutStatus": False,
                "labelRules": [],
                "classifyRules": []
            },
            "handlingFee": 0,
            "isRecommend": 0,
            "isSelf": False,
            "isSwitch": False,
            "productSwitch": False,
            "name": f"{name}{cur_timestamp}",
            "phone": "18569480669",
            "realName": "陈亚静",
            "intro": "店铺简介",
            "sort": 0,
            "district": 110101,
            "settlementLimit": 1,
            "isContributingAccount": True,
            "merPassword": "123456",
            "divBillMerNum": "",
            "contributingId": "",
            "agentClass": 3,
            "settlementDay": 7,
            "copyProductNum": 0,
            "imgsArr": [],
            "proCategoryId": 395,
            "addressDetail": "这是详细地址",
            "merAccount": mer_account,
            "merchantCentCreditAddRequest": None
        }


class MerchantUpdateApi(BaseMerchantApi):
    """编辑商户【改】"""
    def __init__(self, merchant_id=1139, name="自动化新增国企编辑"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/update'
        self.method = 'post'
        self.json = {
            "id": merchant_id,
            "name": name,
            "categoryId": None,
            "typeId": None,
            "addressDetail": "这是详细地址",
            "isSelf": False,
            "sort": 0,
            "isRecommend": False,
            "status": 0,
            "isContributingAccount": True,
            "remark": "",
            "handlingFee": "0.00",
            "settlementDay": 7,
            "settlementLimit": "1.00",
            "merAccount": f"shanghuzhanghao{cur_timestamp}",
            "realName": "陈亚静",
            "phone": "18569480669",
            "divBillMerNum": "",
            "keywords": "",
            "latitude": "",
            "longitude": "",
            "productSwitch": False,
            "createType": "admin",
            "adminId": 1339,
            "starLevel": 4,
            "merchantCompanyInfoRequest": {
                "companyName": "这是企业名称",
                "companyNature": "有限责任公司",
                "registeredCapital": "100",
                "companyAddress": "这是企业地址",
                "billLevelId": None,
                "status": 1,
                "companyIfMoney": True,
                "companyMoneyPeriod": None,
                "isContributingAccount": False,
                "taxCompanyName": "",
                "taxNumber": "1234AB",
                "taxBankOpen": "",
                "taxBankAccount": None,
                "taxRegisterCertImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/09/71b545359da54228bb2b074d50e17389f1wsaxihaz.jpg",
                "merId": merchant_id,
                "cardFront": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/system/2025/09/09/7a932420ec8c494d941c31a5af02da6115jm7951q2.png",
                "cardSide": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/system/2025/09/09/1d8c1e51f1134103baba5d9deda58c4cutq0lf25lb.png",
                "validity": "2025-09-09,2025-09-24",
                "companyCreateDate": "2025-09-09 15:30:08",
                "isHuaSheng": False,
                "recordDate": None,
                "userName": "这是法人姓名",
                "userNumber": None,
                "businessScope": "经营范围"
            },
            "createTime": "2025-09-09 15:30:08",
            "updateTime": "2025-09-09 15:30:08",
            "district": 110101,
            "districtDetail": "北京市-市辖区-东城区",
            "isSwitch": False,
            "contributingId": 0,
            "contributingName": None,
            "merchantCutInfoRequest": {
                "cutStatus": False,
                "classifyRules": [],
                "labelRules": []
            },
            "proCategoryId": 395,
            "agentClass": 3,
            "intro": "店铺简介",
            "copyProductNum": 0,
            "imgsArr": [],
            "merchantCentCreditAddRequest": None
        }


class MerchantListApi(BaseMerchantApi):
    """查询商户列表【查】"""
    def __init__(self, page=1, limit=20, date_limit="", is_recommend="", is_self="",
                 is_switch="true", keywords="", category_id="", type_id="", pro_category="",
                 agent_class="", province="", city="", district="",
                 copy_product_num_start="", copy_product_num_end=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/list?' \
                   f'page={page}&limit={limit}&dateLimit={date_limit}&isRecommend={is_recommend}&' \
                   f'isSelf={is_self}&isSwitch={is_switch}&keywords={keywords}&' \
                   f'categoryId={category_id}&typeId={type_id}&proCategory={pro_category}&' \
                   f'agentClass={agent_class}&province={province}&city={city}&' \
                   f'district={district}&copyProductNumStart={copy_product_num_start}&' \
                   f'copyProductNumEnd={copy_product_num_end}&temp={cur_timestamp}'
        self.method = 'get'


class MerchantTypeAddApi(BaseMerchantApi):
    """添加店铺类型【增】"""
    def __init__(self, name="自动化添加店铺类型", info="这是店铺类型要求"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/type/add'
        self.method = 'post'
        self.json = {
            "id": 0,
            "name": name,
            "info": info
        }


class MerchantTypeListApi(BaseMerchantApi):
    """查询店铺类型【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/type/list?temp={cur_timestamp}'
        self.method = 'get'


class MerchantTypeUpdateApi(BaseMerchantApi):
    """编辑店铺类型【改】"""
    def __init__(self, type_id, name="自动化添加店铺类型", info="这是店铺类型要求"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/type/update'
        self.method = 'post'
        self.json = {
            "id": type_id,
            "name": name,
            "info": info
        }


class MerchantTypeDeleteApi(BaseMerchantApi):
    """删除店铺类型【删】"""
    def __init__(self, type_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/type/delete/{type_id}'
        self.method = 'post'


class MerchantApplyRecordApi(BaseMerchantApi):
    """查询商户入驻列表"""
    def __init__(self, page=1, limit=20, date_limit="", audit_status="", keywords=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/apply/record?' \
                   f'page={page}&limit={limit}&dateLimit={date_limit}&' \
                   f'auditStatus={audit_status}&keywords={keywords}&temp={cur_timestamp}'
        self.method = 'get'


class MerchantApplyRemarkApi(BaseMerchantApi):
    """添加商户备注"""
    def __init__(self, merchant_id, remark="88"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/apply/remark'
        self.method = 'post'
        self.json = {
            "id": merchant_id,
            "remark": remark
        }


class MerchantMenuAddApi(BaseMerchantApi):
    """新增商户菜单【增】"""
    def __init__(self, name="自动化测试新增商户菜单", icon="", menu_type="M", sort=1,
                 is_show=True, component="", perms=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/menu/add'
        self.method = 'post'
        self.json = {
            "menuId": "",
            "parentId": 0,
            "name": name,
            "icon": icon,
            "menuType": menu_type,
            "sort": sort,
            "isShow": is_show,
            "component": component,
            "perms": perms,
            "pid": 0
        }


class MerchantMenuListApi(BaseMerchantApi):
    """启用禁用短信模版【改】"""
    def __init__(self, menu_type="", name="", plat_mer_type="a"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/menu/list?' \
                   f'menuType={menu_type}&name={name}&platMerType={plat_mer_type}&temp={cur_timestamp}'
        self.method = 'get'


class MerchantMenuUpdateApi(BaseMerchantApi):
    """修改商户菜单【改】"""
    def __init__(self, menu_id, name="自动化测试添加商户菜单", icon="s-goods", perms="",
                 component="/product", menu_type="M", sort=6600, is_show=True):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/menu/update'
        self.method = 'post'
        self.json = {
            "id": menu_id,
            "pid": 0,
            "name": name,
            "icon": icon,
            "perms": perms,
            "component": component,
            "menuType": menu_type,
            "sort": sort,
            "isShow": is_show,
            "isDelte": False,
            "type": 4,
            "platformType": "platform_mall",
            "createTime": None,
            "updateTime": "2024-11-22 02:44:21",
            "platMerType": "a"
        }


class MerchantMenuDeleteApi(BaseMerchantApi):
    """删除商户菜单【删】"""
    def __init__(self, menu_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/merchant/menu/delete/{menu_id}'
        self.method = 'post'


class OrderFlowListApi(BaseMerchantApi):
    """订单流配置列表【查】"""
    def __init__(self, page=1, limit=20, menu_type="", name="", plat_mer_type="a",
                 keyword="", city="", region_id="", town="", province="",
                 village="", status=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/flow/order/flow/list?' \
                   f'page={page}&limit={limit}&menuType={menu_type}&name={name}&' \
                   f'platMerType={plat_mer_type}&keyword={keyword}&city={city}&' \
                   f'regionId={region_id}&town={town}&province={province}&' \
                   f'village={village}&status={status}&temp={cur_timestamp}'
        self.method = 'get'


class CityCustomListApi(BaseMerchantApi):
    """自定义区域管理列表【查】"""
    def __init__(self, page=1, limit=20, region_id=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/city/custom/list'
        self.method = 'post'
        self.json = {
            "limit": limit,
            "page": page,
            "regionId": region_id
        }


class SmsTemplatePageApi(BaseMerchantApi):
    """短信模版列表【查】"""
    def __init__(self, page=1, limit=10, menu_type="", name="", plat_mer_type="a", title=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/sms/template/page?' \
                   f'page={page}&limit={limit}&menuType={menu_type}&name={name}&' \
                   f'platMerType={plat_mer_type}&title={title}&temp={cur_timestamp}'
        self.method = 'get'


class SmsTemplateGetApi(BaseMerchantApi):
    """短信模版详情【查】"""
    def __init__(self, sms_id, menu_type="", name="", plat_mer_type="a"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/sms/template/get?' \
                   f'menuType={menu_type}&name={name}&platMerType={plat_mer_type}&' \
                   f'id={sms_id}&temp={cur_timestamp}'
        self.method = 'get'


class GovSubsidyOrderFlowPageListApi(BaseMerchantApi):
    """国补订单流配置【查】"""
    def __init__(self, page=1, limit=20, menu_type="", name="", plat_mer_type="a",
                 region_type="gov_subsidy_merchant", total="6"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/order/flow/page/list?' \
                   f'page={page}&limit={limit}&menuType={menu_type}&name={name}&' \
                   f'platMerType={plat_mer_type}&regionType={region_type}&' \
                   f'total={total}&temp={cur_timestamp}'
        self.method = 'get'


class GovSubsidyOrderFlowDetailApi(BaseMerchantApi):
    """区域详情【查】"""
    def __init__(self, subsidy_order_id, menu_type="", name="", plat_mer_type="a"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/gov/subsidy/order/flow/detail?' \
                   f'menuType={menu_type}&name={name}&platMerType={plat_mer_type}&' \
                   f'id={subsidy_order_id}&temp={cur_timestamp}'
        self.method = 'get'