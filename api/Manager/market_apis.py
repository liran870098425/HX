# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : market_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:21
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class LiveSaveApi(BaseManagerApi):
    """添加有抽奖的直播【增】lcx"""
    def __init__(self, name="接口自动化-有抽奖", activ_name="接口自动化-抽奖活动", 
                 start_time="{{date_recent_time}}", end_time="{{date_soon_time}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/save'
        self.method = 'post'
        self.json = {
            "appShow": False,
            "appSort": 1,
            "cover": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/24/f7f22fbee7154fb9b4c1ffc3e13ff5c576bhv4bnnz.png",
            "endTime": end_time,
            "isActivity": True,
            "name": name,
            "startTime": start_time,
            "activity": {
                "activName": activ_name,
                "activityPrizes": [
                    {
                        "id": "{{live_cj_pro_id}}",
                        "productNum": 2
                    }
                ],
                "isPromoter": False,
                "pastWinState": "enable",
                "signupState": "disable",
                "reWinState": "enable",
                "regionIdList": [
                    510115,
                    510112,
                    510112007,
                    510115003
                ],
                "selectActivNoList": [],
                "winblacklist": [],
                "signupBgImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/24/f7f22fbee7154fb9b4c1ffc3e13ff5c576bhv4bnnz.png",
                "signupGzImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/24/f7f22fbee7154fb9b4c1ffc3e13ff5c576bhv4bnnz.png",
                "isLiveSignup": False
            }
        }


class LivePageApi(BaseManagerApi):
    """查看直播列表【查】lcx"""
    def __init__(self, page=1, limit=20, end_time="", start_time="", keyword=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/page?' \
                   f'page={page}&limit={limit}&endTime={end_time}&' \
                   f'startTime={start_time}&keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class LiveUpdateApi(BaseManagerApi):
    """编辑直播【改】lcx"""
    def __init__(self, live_activity_id, live_activity_name="{{live_activity_name}}", 
                 start_time="{{date_recent_time}}", end_time="{{date_soon_time}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/update/{live_activity_id}'
        self.method = 'post'
        self.json = {
            "appShow": False,
            "appSort": 1,
            "cover": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/24/f7f22fbee7154fb9b4c1ffc3e13ff5c576bhv4bnnz.png",
            "endTime": end_time,
            "isActivity": False,
            "name": live_activity_name,
            "startTime": start_time,
            "id": live_activity_id
        }


class MarketActivityDetailStatisticsApi(BaseManagerApi):
    """查看直播详情【查】lcx"""
    def __init__(self, live_activity_activ_no):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/getMarketActivityDetailStatistics?' \
                   f'activNo={live_activity_activ_no}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityTrendChartApi(BaseManagerApi):
    """查看趋势图【查】lcx"""
    def __init__(self, live_activity_activ_no):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/getMarketActivityTrendChart?' \
                   f'activNo={live_activity_activ_no}&temp={cur_timestamp}'
        self.method = 'get'


class LiveUpdateAppShowApi(BaseManagerApi):
    """APP列表展示-关闭【改】lcx"""
    def __init__(self, live_activity_id, app_show="false"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/update/appShow/{live_activity_id}?appShow={app_show}'
        self.method = 'post'


class MarketActivitySaleProductAddApi(BaseManagerApi):
    """运营直播：新增带货商品【增】lcx"""
    def __init__(self, live_product_id, live_activity_activ_no):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/saleProduct/add'
        self.method = 'post'
        self.json = {
            "0": {
                "id": live_product_id,
                "productNum": 5,
                "activNo": live_activity_activ_no
            }
        }


class MarketActivitySaleProductQueryApi(BaseManagerApi):
    """获取已添加的直播带货商品的主键id【查】lcx"""
    def __init__(self, live_activity_activ_no, page=1, limit=20, keyword=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/saleProduct/query'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "activNo": live_activity_activ_no,
            "keyword": keyword
        }


class MarketActivitySaleProductEditApi(BaseManagerApi):
    """带货商品-修改【改】lcx"""
    def __init__(self, live_product_key_id, live_product_id, product_name="直播带货自动化测试商品--勿动"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/saleProduct/edit'
        self.method = 'post'
        self.json = {
            "id": live_product_key_id,
            "productId": live_product_id,
            "sort": 1,
            "productName": product_name,
            "productPrice": "1.00",
            "livePerkPrice": 1,
            "productNum": 5,
            "productPurchaseNum": 0,
            "productRemainingNum": 5,
            "isLimitBuy": 0,
            "limitBuyNum": 0,
            "upLinkNum": 0,
            "isUpLink": 0,
            "noUpLinkNum": 5,
            "preLinkNum": 1,
            "discountRange": "1.00",
            "isLinked": False,
            "editing": True,
            "livePerkPriceEditable": True,
            "savedOnce": True
        }


class MarketActivitySaleProductUpLinkApi(BaseManagerApi):
    """带货商品上链接【增】lcx"""
    def __init__(self, live_product_key_id, live_product_id, product_name="自动化测试商品cyj-1017【勿动】"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/saleProduct/upLink'
        self.method = 'post'
        self.json = {
            "id": live_product_key_id,
            "productId": live_product_id,
            "sort": 1,
            "productName": product_name,
            "productPrice": "7.00",
            "livePerkPrice": 7,
            "productNum": 5,
            "productPurchaseNum": 0,
            "productRemainingNum": 5,
            "isLimitBuy": 0,
            "limitBuyNum": None,
            "upLinkNum": 0,
            "isUpLink": 0,
            "noUpLinkNum": 5,
            "preLinkNum": 1,
            "discountRange": "7.00",
            "isLinked": False,
            "editing": False,
            "livePerkPriceEditable": True,
            "savedOnce": False
        }


class MarketActivitySaleProductDeleteApi(BaseManagerApi):
    """删除带货商品【删】lcx"""
    def __init__(self, live_product_key_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/saleProduct/delete?' \
                   f'id={live_product_key_id}&temp={cur_timestamp}'
        self.method = 'get'


class LiveDeleteApi(BaseManagerApi):
    """删除无抽奖的直播【删】lcx"""
    def __init__(self, live_activity_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/delete/{live_activity_id}'
        self.method = 'post'


class MarketActivityWinPrizeSelectingProListApi(BaseManagerApi):
    """获取抽奖商品列表【查】lcx"""
    def __init__(self, keyword="", page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/getWinPrizeSelectingProList?' \
                   f'keyword={keyword}&page={page}&limit={limit}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityProductRuleListApi(BaseManagerApi):
    """指定区域中奖列表【查】lcx"""
    def __init__(self, live_cj_activity_activ_no, keyword=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/product/rule/list?' \
                   f'activNo={live_cj_activity_activ_no}&keyword={keyword}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityProductRuleEditApi(BaseManagerApi):
    """编辑指定中奖区域【改】lcx"""
    def __init__(self, live_cj_activity_activ_no, live_cj_activ_product_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/product/rule/edit'
        self.method = 'post'
        self.json = {
            "activNo": live_cj_activity_activ_no,
            "ruleList": [
                {
                    "activProductId": live_cj_activ_product_id,
                    "regionIds": [120000],
                    "ruleName": "2",
                    "sort": 1,
                    "ruleId": 355
                }
            ]
        }


class MarketActivityListRegionPreviewApi(BaseManagerApi):
    """中奖区域预览【查】lcx"""
    def __init__(self, live_cj_activity_activ_no, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/list/region/preview?' \
                   f'page={page}&limit={limit}&activNo={live_cj_activity_activ_no}&temp={cur_timestamp}'
        self.method = 'get'


class ExportMarketUserExcelApi(BaseManagerApi):
    """导出报名人信息【查】lcx"""
    def __init__(self, live_cj_activity_activ_no):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/export/market/user/excel'
        self.method = 'post'
        self.json = {
            "activNo": live_cj_activity_activ_no
        }


class MarketActivityBlacklistAddApi(BaseManagerApi):
    """添加中奖黑名单【增】lcx"""
    def __init__(self, phone="13378947894", live_cj_activity_activ_no=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/blacklist/add'
        self.method = 'post'
        self.json = {
            "phone": phone,
            "valid": True,
            "saving": True,
            "editing": True,
            "phoneError": "",
            "activNo": live_cj_activity_activ_no
        }


class MarketActivityListBlacklistPreviewApi(BaseManagerApi):
    """获取中奖黑名单列表【查】lcx"""
    def __init__(self, live_cj_activity_activ_no, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/list/blacklist/preview?' \
                   f'page={page}&limit={limit}&activNo={live_cj_activity_activ_no}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityBlacklistDeleteApi(BaseManagerApi):
    """删除中奖黑名单【删】lcx"""
    def __init__(self, live_blacklist_id, live_blacklist_phone, update_time="2025-10-14+16:33:02"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/blacklist/delete?' \
                   f'id={live_blacklist_id}&phone={live_blacklist_phone}&updateTime={update_time}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityPreWinUserAddApi(BaseManagerApi):
    """抽奖商品中奖候选人添加【增】lcx"""
    def __init__(self, live_cj_activity_activ_no, live_cj_activ_product_id, 
                 address="测试", name="接口测试", phone="13396329632"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/prewinuser/add'
        self.method = 'post'
        self.json = {
            "activNo": live_cj_activity_activ_no,
            "activProductId": live_cj_activ_product_id,
            "preWinNum": 1,
            "address": address,
            "fourLevelRegionCodes": 510115003,
            "name": name,
            "phone": phone,
            "regionId": 510115
        }


class MarketActivityPreWinUserListApi(BaseManagerApi):
    """获取中奖候选人列表数据【查】lcx"""
    def __init__(self, live_cj_activity_activ_no, live_cj_activ_product_id, 
                 page_num=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/prewinuser/list?' \
                   f'pageNum={page_num}&limit={limit}&activNo={live_cj_activity_activ_no}&' \
                   f'activProductId={live_cj_activ_product_id}&temp={cur_timestamp}'
        self.method = 'get'


class MarketActivityPreWinUserListDeleteApi(BaseManagerApi):
    """删除中奖候选人【删】lcx"""
    def __init__(self, win_prize_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/market/activity/prewinuser/list/delete?' \
                   f'id={win_prize_id}&temp={cur_timestamp}'
        self.method = 'get'


class LiveDeleteWithPrizeApi(BaseManagerApi):
    """删除有抽奖的直播【删】lcx"""
    def __init__(self, live_cj_activity_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/live/delete/{live_cj_activity_id}'
        self.method = 'post'