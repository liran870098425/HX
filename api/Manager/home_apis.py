# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : home_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:11
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class TodayNewUserApi(BaseManagerApi):
    """今日新增用户数【查】"""
    def __init__(self, province="", city="", district="", town="", village="", region_type="0", num="", date_limit="today"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/user/append?' \
                   f'province={province}&city={city}&district={district}&town={town}&village={village}&' \
                   f'regionType={region_type}&num={num}&dateLimit={date_limit}&temp={cur_timestamp}'
        self.method = 'get'


class TodayPromotionUserApi(BaseManagerApi):
    """今日推广用户数【查】"""
    def __init__(self, province="", city="", district="", town="", village="", region_type="0", num="", date_limit="today"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/pro/append?' \
                   f'province={province}&city={city}&district={district}&town={town}&village={village}&' \
                   f'regionType={region_type}&num={num}&dateLimit={date_limit}&temp={cur_timestamp}'
        self.method = 'get'


class PlatformTotalMerchantApi(BaseManagerApi):
    """平台总商户数【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/merchant/data?temp={cur_timestamp}'
        self.method = 'get'


class TodayUserViewApi(BaseManagerApi):
    """今日用户访问模块【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/user/view?temp={cur_timestamp}'
        self.method = 'get'


class OrderSellApi(BaseManagerApi):
    """订单总数、销售额总数、交易额总数、补贴总数【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/order/sell?temp={cur_timestamp}'
        self.method = 'get'


class PlatformOrderChartApi(BaseManagerApi):
    """平台销售数据【查】"""
    def __init__(self, year="{{year}}", month="{{mouth}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/order/chart?' \
                   f'year={year}&month={month}&temp={cur_timestamp}'
        self.method = 'get'


class PlatformOrderRegionApi(BaseManagerApi):
    """平台补贴数据【查】"""
    def __init__(self, data_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/order/region?' \
                   f'dataLimit={data_limit}&temp={cur_timestamp}'
        self.method = 'get'


class BrandRankingApi(BaseManagerApi):
    """品牌销售排名【查】"""
    def __init__(self, data_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/brand/ranking?' \
                   f'dataLimit={data_limit}&temp={cur_timestamp}'
        self.method = 'get'


class CategoryRankingApi(BaseManagerApi):
    """品类销售排名【查】"""
    def __init__(self, data_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/category/ranking?' \
                   f'dataLimit={data_limit}&temp={cur_timestamp}'
        self.method = 'get'


class ProductRankingApi(BaseManagerApi):
    """商品销售排名【查】"""
    def __init__(self, data_limit=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/product/ranking?' \
                   f'dataLimit={data_limit}&temp={cur_timestamp}'
        self.method = 'get'


class TotalPanelApi(BaseManagerApi):
    """查询在售商品、待发货订单、已退款订单、生活视频数、生活达人数、二手发布数、回收专员数、商品供应商【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/total/panel?temp={cur_timestamp}'
        self.method = 'get'


class HomeIndexApi(BaseManagerApi):
    """查询总数居、今日新增商户数、今日新增用户数、订单量、用户访问量、销售额【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/index?temp={cur_timestamp}'
        self.method = 'get'


class OperatingDataApi(BaseManagerApi):
    """查询经营数据【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/operating/data?temp={cur_timestamp}'
        self.method = 'get'


class ChannelRatioApi(BaseManagerApi):
    """查询用户渠道比例【查】"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/statistics/home/channel?temp={cur_timestamp}'
        self.method = 'get'