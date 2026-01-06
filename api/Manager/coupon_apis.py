# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : coupon_apis.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import rdm_date, cur_date_time, rdm_date_plus_2days, cur_timestamp
import datetime


class ManagerCouponAddApi(BaseManagerApi):
    # 添加优惠券
    def __init__(self,category):

        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/add'
        self.method = 'post'
        # 在实例化时动态生成时间值，确保每次创建实例时都获取最新时间
        # 由于cur_date_time()不接受参数，我们需要使用datetime来格式化当前时间
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_plus_2_days = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')
        
        self.json = {
                            "ratio": "11",
                            "useGoods": 0,
                            "id": "",
                            "provinces": [],
                            "cities": [],
                            "districts": [],
                            "name": "测试补贴券",
                            "category": category, #类别 1-商家券, 2-商品券, 3-通用券，4-品类券，5-品牌券，6-跨店券,7-补贴
                            "money": 1,
                            "minPrice": 0,
                            "receiveType": 1,
                            "subsidyType": 0,#补贴券类型 0-平台通用券 1-地方专用券, 2-平台抵扣卷, 3-地方政府卷
                            "isSuperposition": False,#是否允许叠加(0:False，1:true)
                            "subsidyManner": 0,#补贴方式： 0-立减，1-立返
                            "isTimeReceive": True,
                            "receiveStartTime": current_time,  # 领取开始时间，当前时间
                            "receiveEndTime": current_plus_2_days,  # 领取结束时间，当前日期+2天
                            "isFixedTime": True,
                            "day": 1,
                            "useStartTime": current_time,  # 使用开始时间，当前时间
                            "useEndTime": current_plus_2_days,  # 使用结束时间，当前日期+2天
                            "isLimited": False,#是否限量, 默认0 否， 1是
                            "total": 1,
                            "num": 1,
                            "isRepeated": False,#是否可重复领取
                            "linkedData": None,
                            "status": True,
                            "isAutoReceive": True,
                            "validityTime": [
                                current_time,  # 有效期开始时间，当前时间
                                current_plus_2_days  # 有效期结束时间，当前日期+2天
                            ],
                            "collectionTime": [
                                current_time,  # 收集时间开始，当前时间
                                current_plus_2_days  # 收集时间结束，当前日期+2天
                            ],
                            "regionIds": [],
                            "lastTotal": "",
                            "cid": "",
                            "groupNames": [
                                "这个是组名"
                            ],
                            "topTypeId": "",
                            "warningType": "",
                            "activityRegulations": [
                                {
                                    "title": "",
                                    "content": "这个是内容",
                                    "headline": "这个是活动细"
                                }
                            ],
                            "useRegistrations": [
                                {
                                    "title": "",
                                    "content": "这个是使用须知内容",
                                    "headline": "这个是使用须"
                                }
                            ],
                            "sameProductMaxAmount": 2000,
                            "singleProductMaxAmount": 2000
                        }


class ManagerDeleteCouponApi(BaseManagerApi):
    # 删除优惠券,id为优惠券id
    def __init__(self, id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/delete'
        self.method = 'post'
        self.json = {"id": id, "loseEfficacyStatus": 1}

class ManagerCouponListApi(BaseManagerApi):
    # 获取优惠券列表
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/subsidy/list?page=1&limit=80&category=&name=&status=&receiveType=&subsidyType=&temp='
        self.method = 'get'

# 关闭优惠券
class ManagerCouponCloseApi(BaseManagerApi):
    def __init__(self,id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/switch/{id}'
        self.method = 'post'
#查看优惠券详情
class ManagerCouponDetailApi(BaseManagerApi):
    def __init__(self,id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/detail/{id}?temp={cur_timestamp}'
        self.method = 'get'

#获取领取/发放记录
class ManagerCouponRecordApi(BaseManagerApi):
    def __init__(self,id):
        super().__init__()
        self.url = f'{self.host}/api/api/admin/platform/coupon/subsidy/user/list?total=1&issuedNum=0&usedNum=0&totalMoney=0&usedMoney=0.00&createTime=2025-12-30+09:52:47&createUser=%E8%B6%85%E7%BA%A7%E7%AE%A1%E7%90%86%E5%91%98&isLimited=false&id={id}&name=&merIds=&page=1&limit=20&temp={cur_timestamp}'
        self.method = 'get'