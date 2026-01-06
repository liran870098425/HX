# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : user_audit_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformUserAuditPageV2Api(BaseManagerApi):
    """列表信息-拒绝【查】"""
    def __init__(self, page=1, limit=20, type_val="2"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/audit/page/v2'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "auditTimeBegin": "",
            "auditTimeEnd": "",
            "submitTimeBegin": "",
            "submitTimeEnd": "",
            "type": type_val,
            "userSign": ""
        }


class PlatformUserStatisticsAuditPageV2Api(BaseManagerApi):
    """统计数据查看【查】"""
    def __init__(self, page=1, limit=20, type_val="0"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/statistics/audit/page/v2'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "auditTimeBegin": "",
            "auditTimeEnd": "",
            "submitTimeBegin": "",
            "submitTimeEnd": "",
            "type": type_val,
            "userSign": ""
        }


class PlatformUserAuditApi(BaseManagerApi):
    """审核-通过【改】"""
    def __init__(self, user_id="{{yhsh_userid}}", audit_id="{{yhsh_id}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/audit'
        self.method = 'post'
        self.json = {
            "userId": user_id,
            "userInfoReviewRequests": [
                {
                    "id": audit_id,
                    "reviewStatus": "PASS",
                    "updateType": "AVATAR"
                }
            ]
        }


class PlatformUserTagListApi(BaseManagerApi):
    """审核按钮 Copy【查】"""
    def __init__(self, page=1, limit=20, temp="1755502857"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/tag/list?temp={temp}&page={page}&limit={limit}'
        self.method = 'get'