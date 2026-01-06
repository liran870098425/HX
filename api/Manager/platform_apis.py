# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : platform_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformMenuCacheTreeApi(BaseManagerApi):
    """获取角色列表权限【查】"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/menu/cache/tree?temp={temp}'
        self.method = 'get'


class PlatformRoleListApi(BaseManagerApi):
    """获取管理员列表角色下拉选项【查】"""
    def __init__(self, page=1, limit=75, status=1, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/role/list?page={page}&limit={limit}&status={status}&temp={temp}'
        self.method = 'get'


class PlatformRoleSaveApi(BaseManagerApi):
    """新增角色【增】"""
    def __init__(self, role_name="冲冲冲啛啛喳喳", status=False, rules="{{rules}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/role/save'
        self.method = 'post'
        self.json = {
            "roleName": role_name,
            "status": status,
            "rules": rules
        }


class PlatformRoleInfoApi(BaseManagerApi):
    """获取已有角色权限列表【查】"""
    def __init__(self, role_id=4, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/role/info/{role_id}?temp={temp}'
        self.method = 'get'


class PlatformRoleUpdateApi(BaseManagerApi):
    """修改角色【改】"""
    def __int__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/role/update'
        self.json = {
            "id" : 4,
            "roleName": "超级管理员",
            "rules" : "{{rules}}", # 权限列表
            "status": True
        }
        self.method = 'post'



class PlatformRoleDeleteApi(BaseManagerApi):
    """删除角色【删】"""
    def __init__(self, role_id=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/role/delete/{role_id}'
        self.method = 'post'
        self.json = {

        }


class PlatformAdminSaveApi(BaseManagerApi):
    """新增管理员【增】"""
    def __init__(self, account="chenyajing0507", pwd="147852369zxc", real_name="陈亚静0507", roles="4", status=False):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/admin/save'
        self.method = 'post'
        self.json = {
            "account": account,
            "level": None,
            "pwd": pwd,
            "realName": real_name,
            "roles": roles,
            "status": status,
            "phone": None
        }


class PlatformAdminListApi(BaseManagerApi):
    """获取管理员列表【查】"""
    def __init__(self, real_name="", limit=15, page=7, temp="{{temp}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/admin/list?realName={real_name}&temp={temp}&limit={limit}&page={page}'
        self.method = 'get'


class PlatformAdminUpdateApi(BaseManagerApi):
    """编辑管理员【改】"""
    def __init__(self, admin_id="{{ma_id}}", account="chenyajing0507", phone="13333333333", pwd="", roles="4", real_name="陈亚静0507", status=False):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/admin/update'
        self.method = 'post'
        self.json = {
            "account": account,
            "phone": phone,
            "pwd": pwd,
            "roles": roles,
            "realName": real_name,
            "status": status,
            "id": admin_id
        }


class PlatformAdminDeleteApi(BaseManagerApi):
    """删除管理员【删】"""
    def __init__(self, admin_id="{{ma_id}}", temp="{{temp}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/admin/delete?id={admin_id}&temp={temp}'
        self.method = 'get'


class PlatformMenuListApi(BaseManagerApi):
    """获取新增后的权限列表【查】"""
    def __init__(self, menu_type="", name="", temp="{{temp}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/menu/list?menuType={menu_type}&name={name}&temp={temp}'
        self.method = 'get'


class PlatformMenuAddApi(BaseManagerApi):
    """新增权限【增】"""
    def __init__(self, menu_id="", parent_id=0, name="223", icon="", menu_type="M", sort=0, is_show=True, component="/operation", perms=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/menu/add'
        self.method = 'post'
        self.json = {
            "menuId": menu_id,
            "parentId": parent_id,
            "name": name,
            "icon": icon,
            "menuType": menu_type,
            "sort": sort,
            "isShow": is_show,
            "component": component,
            "perms": perms,
            "pid": 0
        }


class PlatformMenuDeleteApi(BaseManagerApi):
    """删除权限【删】"""
    def __init__(self, menu_id=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/menu/delete/{menu_id}'
        self.method = 'post'
        self.json = {}


class PlatformPromoterCityTreeApi(BaseManagerApi):
    """获取街道列表地区【查】"""
    def __init__(self, temp="1755495112"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/city/tree?temp={temp}'
        self.method = 'get'


class PlatformStreetUserAddApi(BaseManagerApi):
    """新增街道账号【增】"""
    def __init__(self, area_id=110101, account="自动化测试新增街道账号", password=433833, real_name="自动化测试名称", phone="18569480669", street_name=110101007, street_id=110101016, model_type="street_promoter", address="自动化测试地址", account_status=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/street/user/add'
        self.method = 'post'
        self.json = {
            "areaId": area_id,
            "account": account,
            "password": password,
            "realName": real_name,
            "phone": phone,
            "streetName": street_name,
            "streetId": street_id,
            "modelType": model_type,
            "address": address,
            "accountStatus": account_status
        }


class PlatformStreetUserListApi(BaseManagerApi):
    """获取新增后的街道列表【查】"""
    def __init__(self, account="", page=1, limit=20, city="", district="", town="", province="", village="", account_status="", town_type="", date_limit="", temp="{{temp}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/street/user/list?account={account}&page={page}&limit={limit}&city={city}&district={district}&town={town}&province={province}&village={village}&accountStatus={account_status}&townType={town_type}&dateLimit={date_limit}&temp={temp}'
        self.method = 'get'


class PlatformStreetUserEditApi(BaseManagerApi):
    """编辑街道账号【改】"""
    def __init__(self, street_id="{{jd_id}}", account="特通过1224", password="123456", account_status=1, real_name="ASDF1", phone="13333333333", address="ASDF", street_name="体育馆路街道", area_id=110101, model_type="comrade_promoter"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/street/user/edit'
        self.method = 'post'
        self.json = {
            "id": street_id,
            "account": account,
            "password": password,
            "accountStatus": account_status,
            "remark": None,
            "realName": real_name,
            "phone": phone,
            "address": address,
            "streetId": 110101015,
            "streetName": street_name,
            "areaId": area_id,
            "modelType": model_type
        }


class PlatformBusinessRecordGetCompanyApi(BaseManagerApi):
    """获取业务订单公司列表【查】"""
    def __init__(self, temp="1755497154"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/getCompany?temp={temp}'
        self.method = 'get'


class PlatformCollectionCompanyPullListApi(BaseManagerApi):
    """获取业务订单代收公司列表【查】"""
    def __init__(self, temp="1755497154"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/collectionCompany/pull/list?temp={temp}'
        self.method = 'get'


class PlatformBusinessRecordGetPayTypeListApi(BaseManagerApi):
    """获取业务订单支付方式【查】"""
    def __init__(self, temp="1755497154"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/getPayTypeList?temp={temp}'
        self.method = 'get'


class PlatformBusinessRecordGetLogisticsTypeListApi(BaseManagerApi):
    """获取业务订单快递方式列表【查】"""
    def __init__(self, temp="1755497154"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/getLogisticsTypeList?temp={temp}'
        self.method = 'get'


class PlatformProductCategoryCacheTreeApi(BaseManagerApi):
    """获取业务订单商品分类列表【查】"""
    def __init__(self, temp="1755497154"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/category/cache/tree?temp={temp}'
        self.method = 'get'


class PlatformBusinessRecordSaveApi(BaseManagerApi):
    """生成业务订单【增】"""
    def __init__(self, flow_area_id=91, mer_id=91, pay_type="alipay", collection_company_id=29, pay_total_price=1000, post_types=None, product_ids=None, order_end_time_start="2025-08-20", order_end_time_end="2025-08-23", receive_address=1):
        if post_types is None:
            post_types = ["SF"]
        if product_ids is None:
            product_ids = [255, 257]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/save'
        self.method = 'post'
        self.json = {
            "flowAreaId": flow_area_id,
            "merId": mer_id,
            "companyEnName": "",
            "validityTime": ["2025-08-20", "2025-08-23"],
            "payType": pay_type,
            "collectionCompanyId": collection_company_id,
            "regionIds": [],
            "peakValueStart": "14：58",
            "peakValueEnd": "15：58",
            "peakRatio": 1,
            "commissionRatio": 1,
            "productIds": product_ids,
            "payTotalPrice": pay_total_price,
            "postTypes": post_types,
            "refundPrice": "",
            "refundCategoryTypes": [],
            "peakValueRange": [],
            "orderEndTimeStart": order_end_time_start,
            "orderEndTimeEnd": order_end_time_end,
            "receiveAddress": receive_address
        }


class PlatformBusinessRecordGetListApi(BaseManagerApi):
    """获取新增后的业务订单列表【查】"""
    def __init__(self, limit=15, page=1, is_del="", record_no="", status="recordData"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/getList'
        self.method = 'post'
        self.json = {
            "limit": limit,
            "dateTime": [],
            "page": page,
            "isDel": is_del,
            "recordNo": record_no,
            "status": status
        }


class PlatformBusinessRecordDeleteApi(BaseManagerApi):
    """删除业务订单【删】"""
    def __init__(self, record_id="{{ywdd_id}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/businessRecord/delete'
        self.method = 'post'
        self.json = {
            "id": record_id
        }