# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : platform_user_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformUserListV2Api(BaseManagerApi):
    """用户-用户管理-更多-配置角色-页码数量设置--曾【查】"""
    def __init__(self, page=2, limit=60, sort_field="0", sort_type="1"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/list/v2'
        self.method = 'post'
        self.json = {
            "activeBegin": "",
            "activeEnd": "",
            "avgPriceBegin": "",
            "avgPriceEnd": "",
            "balanceBegin": "",
            "balanceEnd": "",
            "city": "",
            "district": "",
            "exchangeMoneyBegin": "",
            "exchangeMoneyEnd": "",
            "lastLoginTimeBegin": "",
            "lastLoginTimeEnd": "",
            "level": "",
            "limit": limit,
            "page": page,
            "province": "",
            "registerBegin": "",
            "registerEnd": "",
            "registerType": "",
            "sortField": sort_field,
            "sortType": sort_type,
            "tagIdList": [],
            "userSign": ""
        }


class PlatformUserSetTagApi(BaseManagerApi):
    """用户-用户管理-更多-配置角色-设置标签-标签设置--曾【改】"""
    def __init__(self, tag_id_list=None, user_id_list=None):
        if tag_id_list is None:
            tag_id_list = ["{{yhlb_bq_id}}"]
        if user_id_list is None:
            user_id_list = ["{{yhlb_userid}}"]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/set/tag'
        self.method = 'post'
        self.json = {
            "tagIdList": tag_id_list,
            "delTagIdList": [],
            "userIdList": user_id_list
        }


class PlatformUserExportApi(BaseManagerApi):
    """用户-用户管理-数据导出--曾【查】"""
    def __init__(self, page_start=1, page_end=42, file_name="用户列表_0818_14_39_40", limit=20, page=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/export/user/export'
        self.method = 'post'
        self.json = {
            "activeBegin": "",
            "activeEnd": "",
            "avgPriceBegin": "",
            "avgPriceEnd": "",
            "balanceBegin": "",
            "balanceEnd": "",
            "city": "",
            "district": "",
            "exchangeMoneyBegin": "",
            "exchangeMoneyEnd": "",
            "lastLoginTimeBegin": "",
            "lastLoginTimeEnd": "",
            "level": "",
            "limit": limit,
            "page": page,
            "province": "",
            "registerBegin": "",
            "registerEnd": "",
            "registerType": "",
            "sortField": "0",
            "sortType": "1",
            "tagIdList": [],
            "userSign": "",
            "userIdList": [],
            "fileName": file_name,
            "pageStart": page_start,
            "pageEnd": page_end,
            "exportFields": [
                {
                    "field": "avatar",
                    "sort": 1,
                    "fieldName": "用户头像",
                    "selected": 0
                },
                {
                    "field": "nickname",
                    "sort": 2,
                    "fieldName": "用户昵称",
                    "selected": 0
                },
                {
                    "field": "id",
                    "sort": 3,
                    "fieldName": "用户ID",
                    "selected": 0
                },
                {
                    "field": "phone",
                    "sort": 4,
                    "fieldName": "手机号码",
                    "selected": 0
                },
                {
                    "field": "vipLevel",
                    "sort": 5,
                    "fieldName": "会员等级",
                    "selected": 0
                },
                {
                    "field": "role",
                    "sort": 6,
                    "fieldName": "角色",
                    "selected": 0
                },
                {
                    "field": "balance",
                    "sort": 7,
                    "fieldName": "积分",
                    "selected": 0
                },
                {
                    "field": "exchangeMoney",
                    "sort": 8,
                    "fieldName": "焕新币",
                    "selected": 0
                },
                {
                    "field": "avgPrice",
                    "sort": 9,
                    "fieldName": "客单价",
                    "selected": 0
                },
                {
                    "field": "registerType",
                    "sort": 10,
                    "fieldName": "注册类型",
                    "selected": 0
                },
                {
                    "field": "createTime",
                    "sort": 11,
                    "fieldName": "注册时间",
                    "selected": 0
                },
                {
                    "field": "area",
                    "sort": 12,
                    "fieldName": "所在地区",
                    "selected": 0
                },
                {
                    "field": "tag",
                    "sort": 13,
                    "fieldName": "标签",
                    "selected": 0
                }
            ]
        }


class PlatformUserDetailV2Api(BaseManagerApi):
    """用户-用户管理-详情-基本信息查看--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", temp="1755499343"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/detail/v2/{user_id}?id={user_id}&temp={temp}'
        self.method = 'get'


class PlatformUserIntegralRecordApi(BaseManagerApi):
    """用户-用户管理-详情-积分信息查看 --曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=20, page=1, temp="1755499343"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/integral/record/{user_id}?id={user_id}&temp={temp}&userid={user_id}&limit={limit}&page={page}'
        self.method = 'get'


class PlatformUserBalanceRecordApi(BaseManagerApi):
    """用户-用户管理-详情-焕新币账户查看--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=20, page=1, temp="1755500635"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/balance/record/{user_id}?id={user_id}&temp={temp}&userid={user_id}&limit={limit}&page={page}'
        self.method = 'get'


class PlatformUserActionApi(BaseManagerApi):
    """用户-用户管理-详情-用户行为查看 --曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", temp="1755500635"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/action/{user_id}?temp={temp}&userid={user_id}'
        self.method = 'get'


class PlatformUserAddressApi(BaseManagerApi):
    """用户-用户管理-详情-收件地址查看--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=5000, page=1, temp="1755500635"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/address/{user_id}?userid={user_id}&limit={limit}&page={page}&temp={temp}'
        self.method = 'get'


class PlatformUserBillHeaderApi(BaseManagerApi):
    """用户-用户管理-详情-发票抬头查看--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=5000, page=1, temp="1755500635"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/bill/header/{user_id}?userid={user_id}&limit={limit}&page={page}&temp={temp}'
        self.method = 'get'


class PlatformUserModifyLogApi(BaseManagerApi):
    """用户-用户管理-详情-修改日志查看--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=20, page=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/modify/log'
        self.method = 'post'
        self.json = {
            "userid": user_id,
            "limit": limit,
            "page": page,
            "timeType": "op_time",
            "timeBegin": "",
            "timeEnd": ""
        }


class PlatformUserRolePageListApi(BaseManagerApi):
    """用户-用户管理-更多-配置角色-列表信息--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", limit=10, page=1, temp="1755500635", status=1, promoterls_show=True):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/role/page/list?userid={user_id}&limit={limit}&page={page}&temp={temp}&status={status}&promoterlsShow={str(promoterls_show).lower()}'
        self.method = 'get'


class PlatformUserRoleRightsTypeApi(BaseManagerApi):
    """用户-用户管理-更多-配置角色-角色列表--曾【查】"""
    def __init__(self, user_id="{{yhlb_userid}}", temp="1755587106"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/role/rights/type?temp={temp}&userId={user_id}'
        self.method = 'get'


class PlatformUserSetRoleApi(BaseManagerApi):
    """用户-用户管理-更多-配置角色-角色设置关闭--曾【改】"""
    def __init__(self, user_id="{{yhlb_userid}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/set/role'
        self.method = 'post'
        self.json = {
            "roleIdList": [],
            "userId": user_id
        }


class PlatformUserModifyExchangeMoneyApi(BaseManagerApi):
    """用户-用户管理-更多-修改焕新币-减少--曾【改】"""
    def __init__(self, user_id="{{yhlb_userid}}", amount="-0.01", mode="sub", temp="1755501669"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/modify/exchange/money?userid={user_id}&temp={temp}&amount={amount}&mode={mode}'
        self.method = 'get'


class PlatformUserTagAllListApi(BaseManagerApi):
    """用户-用户管理-更多-设置标签--曾【查】"""
    def __init__(self, temp="1755501729"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/tag/all/list?temp={temp}'
        self.method = 'get'


class PlatformUserOfflinePayApi(BaseManagerApi):
    """用户-用户管理-更多-配置角色-关闭线下支付--曾【改】"""
    def __init__(self, user_id="{{yhlb_userid}}", status=0):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/offline/pay'
        self.method = 'post'
        self.json = {
            "status": status,
            "uid": [user_id]
        }