# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : street_promoter_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformPromoterInspectorListApi(BaseManagerApi):
    """信息列表【查】"""
    def __init__(self, promoter_type="street", tag_ids="", sex="", register_type="", pay_count="", access_type="0", date_limit="", nikename="", phone="", page=1, limit=20, keyword="", town_type="", city="", district="", town="", province="", village="", temp="1755565284"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/inspector/list?promoterType={promoter_type}&tagIds={tag_ids}&sex={sex}&registerType={register_type}&payCount={pay_count}&accessType={access_type}&dateLimit={date_limit}&nikename={nikename}&phone={phone}&page={page}&limit={limit}&keyword={keyword}&townType={town_type}&city={city}&district={district}&town={town}&province={province}&village={village}&temp={temp}'
        self.method = 'get'


class PlatformPromoterCityTreeApi(BaseManagerApi):
    """推广员添加表单【查】"""
    def __init__(self, temp="1755504577"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/city/tree?temp={temp}'
        self.method = 'get'


class PlatformPromoterSaveApi(BaseManagerApi):
    """添加推广员【增】"""
    def __init__(self, promoter_type="street", province=510115, town="柳城街道", village="1", town_type=1, name="12", phone="13333000499", work="1"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/save'
        self.method = 'post'
        self.json = {
            "promoterType": promoter_type,
            "province": province,
            "town": town,
            "village": village,
            "townType": town_type,
            "name": name,
            "phone": phone,
            "work": work
        }


class PlatformPromoterImportApi(BaseManagerApi):
    """导入【增】"""
    def __init__(self, data_list=None):
        if data_list is None:
            data_list = [
                {
                    "province": "四川省",
                    "city": "成都市",
                    "district": "温江区",
                    "town": "柳城街道",
                    "village": "c",
                    "name": 13333000000,
                    "phone": "网格员",
                    "work": "城区",
                    "townType": ""
                }
            ]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/import'
        self.method = 'post'
        self.json = {
            "list": data_list
        }


class PlatformPromoterExportInspectorApi(BaseManagerApi):
    """导出 【查】"""
    def __init__(self, tag_ids="", sex="", register_type="", pay_count="", access_type="0", date_limit="", nikename="", phone="", page=1, limit=20, keyword="", town_type="", city="", district="", town="", province="", village="", promoter_type="street", temp="1755565346"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/export/inspector?tagIds={tag_ids}&sex={sex}&registerType={register_type}&payCount={pay_count}&accessType={access_type}&dateLimit={date_limit}&nikename={nikename}&phone={phone}&page={page}&limit={limit}&keyword={keyword}&townType={town_type}&city={city}&district={district}&town={town}&province={province}&village={village}&promoterType={promoter_type}&temp={temp}'
        self.method = 'get'


class PlatformPromoterStreetConfigApi(BaseManagerApi):
    """规则配置【改】"""
    def __init__(self, role_id=100, config_list=None):
        if config_list is None:
            config_list = [
                {
                    "computationRule": 0,
                    "days": 1,
                    "goupOrDemotion": 0,
                    "id": 90,
                    "intoRoleId": 99,
                    "peopleNum": 1,
                    "whether": True
                },
                {
                    "computationRule": 2,
                    "days": 1,
                    "goupOrDemotion": 1,
                    "id": 91,
                    "intoRoleId": 99,
                    "peopleNum": 1,
                    "whether": True
                },
                {
                    "computationRule": None,
                    "days": 0,
                    "goupOrDemotion": 1,
                    "id": 92,
                    "intoRoleId": None,
                    "peopleNum": 0,
                    "whether": False
                }
            ]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/street/config'
        self.method = 'post'
        self.json = {
            "roleId": role_id,
            "configList": config_list
        }


class PlatformStreetUserPromotionSubsApi(BaseManagerApi):
    """用户分销关系查看【查】"""
    def __init__(self, user_id=100907, temp="1755566073"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/{user_id}/subs?temp={temp}'
        self.method = 'get'


class PlatformPromoterEditApi(BaseManagerApi):
    """用户信息编辑按钮点击【查】"""
    def __init__(self, user_id=100907, temp="1755566114"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/edit?id={user_id}&temp={temp}'
        self.method = 'get'


class PlatformPromoterUpdateApi(BaseManagerApi):
    """网格员信息编辑【改】"""
    def __init__(self, promoter_type="street", user_id=100907, user_id2=8434138, name="测试", phone="13333000100", town="柳城街道", village="c", work="网格员", town_type=1, province=510115, city=510100, district=510115, province_code=510000, city_code=510100, district_code=510115):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/update'
        self.method = 'post'
        self.json = {
            "promoterType": promoter_type,
            "id": user_id,
            "userId": user_id2,
            "cityList": [province_code, city_code, district_code],
            "name": name,
            "phone": phone,
            "town": town,
            "village": village,
            "work": work,
            "townType": town_type,
            "province": province,
            "city": city,
            "district": district,
            "provinceCode": province_code,
            "cityCode": city_code,
            "districtCode": district_code
        }


class PlatformPromoterDeleteApi(BaseManagerApi):
    """网格员资格取消【改】"""
    def __init__(self, user_id=100928):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/delete'
        self.method = 'post'
        self.json = {
            "id": user_id
        }


class PlatformStreetUserPromotionEnableApi(BaseManagerApi):
    """网格员资格恢复【改】"""
    def __init__(self, user_id=100928):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/{user_id}/enable'
        self.method = 'put'
        self.json = {
            "code": 200,
            "message": None,
            "data": True
        }