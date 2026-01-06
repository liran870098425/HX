# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : user_tag_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformUserTagListApi(BaseManagerApi):
    """列表信息查看 Copy【查】"""
    def __init__(self, page=1, limit=20, temp="1755574434"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/tag/list?temp={temp}&page={page}&limit={limit}'
        self.method = 'get'


class PlatformUserTagSaveApi(BaseManagerApi):
    """添加标签【增】"""
    def __init__(self, name="1"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/tag/save'
        self.method = 'post'
        self.json = {
            "name": name
        }


class PlatformUserTagUpdateApi(BaseManagerApi):
    """修改标签【改】"""
    def __init__(self, tag_id="{{liebiao_id}}", name="12"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/tag/update'
        self.method = 'post'
        self.json = {
            "id": tag_id,
            "name": name
        }


class PlatformUserTagDeleteApi(BaseManagerApi):
    """删除标签 【删】"""
    def __init__(self, tag_id="{{liebiao_id}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/tag/delete/{tag_id}'
        self.method = 'post'
        self.json = {}