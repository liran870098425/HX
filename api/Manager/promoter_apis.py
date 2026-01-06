# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : promoter_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformPromoterListApi(BaseManagerApi):
    """列表信息查看【查】"""
    def __init__(self, page=1, limit=20, promoter_type="all", temp="1755504029", date_limit="", keyword="", city="", district="", town="", province="", village="", town_type="", order="", sort="", start_time="", end_time=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/list?dateLimit={date_limit}&keyword={keyword}&page={page}&limit={limit}&city={city}&district={district}&town={town}&province={province}&village={village}&townType={town_type}&order={order}&sort={sort}&promoterType={promoter_type}&startTime={start_time}&endTime={end_time}&temp={temp}'
        self.method = 'get'


class PlatformPromoterTotalApi(BaseManagerApi):
    """统计数据查看【查】"""
    def __init__(self, promoter_type="all", temp="1755504029"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/total?promoterType={promoter_type}&temp={temp}'
        self.method = 'get'


class PlatformPromoterExportApi(BaseManagerApi):
    """导出【查】"""
    def __init__(self, date_limit="", province="", city="", district="", town="", village="", keyword="", town_type="", parent_keyword="", promoter_type="all", temp="1755504288"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promoter/export?dateLimit={date_limit}&province={province}&city={city}&district={district}&town={town}&village={village}&keyword={keyword}&townType={town_type}&parentKeyword={parent_keyword}&promoterType={promoter_type}&temp={temp}'
        self.method = 'get'


class PlatformPromotedPeopleOrderListApi(BaseManagerApi):
    """推广数据查看【查】"""
    def __init__(self, page=1, limit=10, date_limit="", type_val="0", keyword="", id_val="{{tgytgtj_id}}", temp="1755504340"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promotedPeople/order/list?page={page}&limit={limit}&dateLimit={date_limit}&type={type_val}&keyword={keyword}&id={id_val}&temp={temp}'
        self.method = 'get'


class PlatformPromotedPeopleListApi(BaseManagerApi):
    """推广人数据查看 Copy【查】"""
    def __init__(self, page=1, limit=10, date_limit="", type_val="0", keyword="", id_val="{{tgytgtj_id1}}", temp="1755504383"):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/promotedPeople/list?page={page}&limit={limit}&dateLimit={date_limit}&type={type_val}&keyword={keyword}&id={id_val}&temp={temp}'
        self.method = 'get'


class PlatformPromoterTransferPromoterApi(BaseManagerApi):
    """更换上级 Copy【改】"""
    def __init__(self, id_list=None, old_promoter_id="{{tgytgtj_id1}}", new_promoter_id="{{tgytgtj_id}}"):
        if id_list is None:
            id_list = ["{{tgytj-zyid1}}"]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/transfer/promoter'
        self.method = 'post'
        self.json = {
            "idList": id_list,
            "oldPromoterId": old_promoter_id,
            "newPromoterId": new_promoter_id
        }