# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : user_vip_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  13:21
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class VipConfigUpdateEnableStatusApi(BaseManagerApi):
    """修改会员状态-关闭【改】lcx"""
    def __init__(self, vip_id, status="DISABLE"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/config/updateEnableStatus'
        self.method = 'post'
        self.json = {
            "id": vip_id,
            "status": status
        }


class VipConfigSaveApi(BaseManagerApi):
    """添加会员【增】lcx（前置操作执行数据库删除）"""
    def __init__(self, point_rule_id=1, vip_type="VIP_CARD"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/config/save?temp={cur_timestamp}'
        self.method = 'post'
        self.json = {
            "pointRuleId": point_rule_id,
            "vipType": vip_type
        }


class VipConfigManagementListApi(BaseManagerApi):
    """获取会员规则配置列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/config/vipManagementList'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "startEndTime": []
        }


class VipConfigUpdateApi(BaseManagerApi):
    """编辑会员【改】lcx"""
    def __init__(self, vip_id, point_rule_id=1, vip_type="{{vip_Type}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/config/update'
        self.method = 'post'
        self.json = {
            "id": vip_id,
            "pointRuleId": point_rule_id,
            "vipType": vip_type
        }


class VipCartListApi(BaseManagerApi):
    """获取购卡会员列表【查】lcx"""
    def __init__(self, page=1, limit=20, buy_time=None, card_type=None, keyword="", 
                 vip_level_name=None, vip_type=None):
        if buy_time is None:
            buy_time = []
        if card_type is None:
            card_type = []
        if vip_level_name is None:
            vip_level_name = []
        if vip_type is None:
            vip_type = []
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/list'
        self.method = 'post'
        self.json = {
            "buyTime": buy_time,
            "cardType": card_type,
            "keyword": keyword,
            "vipLevelName": vip_level_name,
            "vipType": vip_type,
            "page": page,
            "limit": limit
        }


class VipCartDetailApi(BaseManagerApi):
    """查看购卡会员详情【查】lcx"""
    def __init__(self, user_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/detail?userId={user_id}&temp={cur_timestamp}'
        self.method = 'get'


class VipCartListExportApi(BaseManagerApi):
    """购卡会员导出【查】lcx"""
    def __init__(self, buy_time=None, card_type=None, keyword="", vip_level_name=None, 
                 vip_type=None, page=1, limit=20, total=40, file_name="购卡会员_0819_13_52_04"):
        if buy_time is None:
            buy_time = []
        if card_type is None:
            card_type = []
        if vip_level_name is None:
            vip_level_name = []
        if vip_type is None:
            vip_type = []
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/list/export'
        self.method = 'post'
        self.json = {
            "buyTime": buy_time,
            "cardType": card_type,
            "keyword": keyword,
            "vipLevelName": vip_level_name,
            "vipType": vip_type,
            "page": page,
            "limit": limit,
            "total": total,
            "idList": [],
            "fileName": file_name,
            "pageStart": 1,
            "pageEnd": 2,
            "exportFields": [
                {
                    "field": "userId",
                    "sort": 1,
                    "fieldName": "ID",
                    "selected": 0
                },
                {
                    "field": "userName",
                    "sort": 2,
                    "fieldName": "昵称",
                    "selected": 0
                },
                {
                    "field": "contactPhone",
                    "sort": 3,
                    "fieldName": "绑定手机号",
                    "selected": 0
                },
                {
                    "field": "vipTypeStr",
                    "sort": 4,
                    "fieldName": "会员类型",
                    "selected": 0
                },
                {
                    "field": "cardType",
                    "sort": 5,
                    "fieldName": "会员套餐",
                    "selected": 0
                },
                {
                    "field": "expirationDate",
                    "sort": 6,
                    "fieldName": "会员有效日期",
                    "selected": 0
                },
                {
                    "field": "vipPoint",
                    "sort": 7,
                    "fieldName": "积分",
                    "selected": 0
                },
                {
                    "field": "vipLevelName",
                    "sort": 8,
                    "fieldName": "会员等级",
                    "selected": 0
                },
                {
                    "field": "effectiveTime",
                    "sort": 9,
                    "fieldName": "购卡时间",
                    "selected": 0
                },
                {
                    "field": "recentOnlineTime",
                    "sort": 10,
                    "fieldName": "最近登录时间",
                    "selected": 0
                },
                {
                    "field": "vipCycle",
                    "sort": 11,
                    "fieldName": "会员周期",
                    "selected": 0
                }
            ]
        }


class VipLevelSaveApi(BaseManagerApi):
    """添加会员等级【增】lcx"""
    def __init__(self, level_name="接口自动化测试", reward_points=1000):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/level/save'
        self.method = 'post'
        self.json = {
            "userRoleIds": [],
            "levelName": level_name,
            "vipBackImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/e7649d21469649ab8ad8f8f4e74ae5338iegbdcvqu.jpg",
            "levelIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/e3b770d8381b4052ac6fd126b12c8643qpevog041q.jpg",
            "levelValueIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/a07bb4a5ceda4be68d8c9f534d8a2993d1476cz198.jpg",
            "huanxinValueIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/2932a1a72caf4590bc3b7059e6d8e8f3ymhtpz5jqp.jpg",
            "yuncaiProductIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/735512d2831e43fdab58bf4f23480dd1x6pdmo3b2l.jpg",
            "landingPagesBackImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/18/790885b545c9483ba46f933d3bda60a026t9et0b0y.jpg",
            "rewardPoints": reward_points,
            "upgradesConditionPoints": "ENABLE_POINTS"
        }


class VipLevelSearchLevelApi(BaseManagerApi):
    """添加会员等级后再查询列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/level/searchLevel'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "startEndTime": []
        }


class VipLevelUpdateApi(BaseManagerApi):
    """编辑会员等级【改】lcx"""
    def __init__(self, level_id, level_name="{{level_name}}", reward_points=80000):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/level/update'
        self.method = 'post'
        self.json = {
            "id": level_id,
            "userRoleIds": [1, 56, 57, 58, 59, 60, 61, 79],
            "levelName": level_name,
            "vipBackImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/5f8499a9e4e244c98433056038fc3288ereu72zypa.jpg",
            "levelIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/7fe82f043bda4c95b37c7abcec801e1bti9fw43hpr.jpg",
            "levelValueIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/ee9c6253d9de451cb3aad69f82fb65c43j16lq5njj.jpg",
            "huanxinValueIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/f0d0b7cb353c4d81bfc5c60b96d3a215beq4v131n2.jpg",
            "yuncaiProductIcon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/ee3dd2b2c2944190978c0cf96395eaebskxzrml2dk.jpg",
            "landingPagesBackImg": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/vipLevel/2025/08/19/4a396e4843704077a3c426089c31bc64d7owywcwbk.jpg",
            "rewardPoints": reward_points,
            "upgradesConditionPoints": "ENABLE_POINTS"
        }


class VipLevelUpdateEnableStatusApi(BaseManagerApi):
    """修改会员等级状态：开启【改】lcx"""
    def __init__(self, level_id, status="ENABLE"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/level/updateEnableStatus'
        self.method = 'post'
        self.json = {
            "id": level_id,
            "status": status
        }


class VipRuleSaveApi(BaseManagerApi):
    """添加积分规则【增】lcx"""
    def __init__(self, name="接口自动化测试", amount_spent_ratio=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/rule/save'
        self.method = 'post'
        self.json = {
            "name": name,
            "amountSpentRatio": amount_spent_ratio,
            "shopageRules": [
                {
                    "monthRange": "0-6",
                    "point": 1
                },
                {
                    "monthRange": "7-12",
                    "point": 1
                },
                {
                    "monthRange": "13-19",
                    "point": 1
                },
                {
                    "monthRange": "20-24",
                    "point": 1
                },
                {
                    "monthRange": "25-30",
                    "point": 1
                },
                {
                    "monthRange": "31-36",
                    "point": 1
                },
                {
                    "monthRange": "37",
                    "point": 1
                }
            ],
            "productCategoryRules": [
                {
                    "categoryId": 1593,
                    "pointRatio": 10
                }
            ],
            "coiledActiveRules": [
                {
                    "dayMonthRange": "everyDay"
                },
                {
                    "dayMonthRange": "oneWeek"
                },
                {
                    "dayMonthRange": "twoWeek"
                },
                {
                    "dayMonthRange": "threeWeek"
                },
                {
                    "dayMonthRange": "oneMonth"
                }
            ]
        }


class VipRuleSearchPointRuleApi(BaseManagerApi):
    """查询积分规则列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/rule/searchPointRule'
        self.method = 'post'
        self.json = {
            "startEndTime": [],
            "page": page,
            "limit": limit,
            "total": 0
        }


class VipRuleUpdateApi(BaseManagerApi):
    """编辑积分规则【改】lcx"""
    def __init__(self, points_id, points_name="{{points_name}}", amount_spent_ratio=10):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/rule/update'
        self.method = 'post'
        self.json = {
            "id": points_id,
            "name": points_name,
            "amountSpentRatio": amount_spent_ratio,
            "shopageRules": [
                {
                    "id": 29,
                    "monthRange": "0-6",
                    "point": 1
                },
                {
                    "id": 30,
                    "monthRange": "7-12",
                    "point": 2
                },
                {
                    "id": 31,
                    "monthRange": "13-19",
                    "point": 3
                },
                {
                    "id": 32,
                    "monthRange": "20-24",
                    "point": 4
                },
                {
                    "id": 33,
                    "monthRange": "25-30",
                    "point": 5
                },
                {
                    "id": 34,
                    "monthRange": "31-36",
                    "point": 6
                },
                {
                    "id": 35,
                    "monthRange": "37",
                    "point": 7
                }
            ],
            "productCategoryRules": [
                {
                    "id": 92,
                    "categoryId": 395,
                    "categoryName": "家用百货",
                    "pointRatio": 1
                }
            ],
            "coiledActiveRules": [
                {
                    "id": 21,
                    "dayMonthRange": "everyDay",
                    "point": 0
                },
                {
                    "id": 22,
                    "dayMonthRange": "oneWeek",
                    "point": 0
                },
                {
                    "id": 23,
                    "dayMonthRange": "twoWeek",
                    "point": 0
                },
                {
                    "id": 24,
                    "dayMonthRange": "threeWeek",
                    "point": 0
                },
                {
                    "id": 25,
                    "dayMonthRange": "oneMonth",
                    "point": 0
                }
            ]
        }


class VipRuleDeleteApi(BaseManagerApi):
    """删除积分规则【删】lcx"""
    def __init__(self, points_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/rule/delete/{points_id}?temp={cur_timestamp}'
        self.method = 'get'


class VipCartSaveApi(BaseManagerApi):
    """添加会员卡【增】lcx"""
    def __init__(self, card_type="EXPERIENCE", name="接口自动化测试", price=100):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/save'
        self.method = 'post'
        self.json = {
            "cardType": card_type,
            "name": name,
            "price": price,
            "vipType": "YUNCAI",
            "icon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncai/2025/08/19/bb6a6e21256440559d55b70d333941e7rf2pwk2kqu.jpg"
        }


class VipCartPageListApi(BaseManagerApi):
    """查询会员卡列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/pageList'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit,
            "createTimeList": [],
            "vipType": []
        }


class VipCartUpdateApi(BaseManagerApi):
    """编辑会员卡【改】lcx"""
    def __init__(self, cart_id, cart_name="{{cart_name}}", price=100):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/update'
        self.method = 'post'
        self.json = {
            "cartId": cart_id,
            "cardType": "EXPERIENCE",
            "name": cart_name,
            "price": price,
            "vipType": "YUNCAI",
            "icon": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncai/2025/08/19/bb6a6e21256440559d55b70d333941e7rf2pwk2kqu.jpg"
        }


class VipCartStatusApi(BaseManagerApi):
    """修改会员卡状态：打开【改】lcx"""
    def __init__(self, cart_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/status?cartId={cart_id}&temp={cur_timestamp}'
        self.method = 'get'


class VipCartDeleteApi(BaseManagerApi):
    """删除会员卡【删】lcx"""
    def __init__(self, cart_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/vip/cart/delete?cartId={cart_id}&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiCategorySaveApi(BaseManagerApi):
    """新增分类【增】lcx"""
    def __init__(self, category_name="接口自动化测试分类", product_ids=None):
        if product_ids is None:
            product_ids = [141496]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/category/save'
        self.method = 'post'
        self.json = {
            "appShowPic": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncaiProductCate/2025/08/19/d5610ac3341443e28a84b4505f4746bbkdpfwupgdx.jpg",
            "categoryName": category_name,
            "productIds": product_ids
        }


class YuncaiCategoryPageListApi(BaseManagerApi):
    """获取分类列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/category/pageList'
        self.method = 'post'
        self.json = {
            "createTimeList": [],
            "page": page,
            "limit": limit,
            "total": 0
        }


class YuncaiCategoryUpdateApi(BaseManagerApi):
    """编辑分类【改】lcx"""
    def __init__(self, category_id, category_name="{{category_Name}}", product_ids=None):
        if product_ids is None:
            product_ids = [141496]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/category/update'
        self.method = 'post'
        self.json = {
            "categoryId": category_id,
            "appShowPic": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/yuncaiProductCate/2025/08/19/d5610ac3341443e28a84b4505f4746bbkdpfwupgdx.jpg",
            "categoryName": category_name,
            "productIds": product_ids
        }


class YuncaiCategoryInfoApi(BaseManagerApi):
    """查看分类详情【查】lcx"""
    def __init__(self, category_id, keyword="", page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/category/info?' \
                   f'categoryId={category_id}&keyword={keyword}&page={page}&' \
                   f'limit={limit}&total=0&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiGroupSaveApi(BaseManagerApi):
    """新增分组【增】lcx"""
    def __init__(self, group_name="接口自动化测试", category_ids=None):
        if category_ids is None:
            category_ids = [24, 26]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/group/save'
        self.method = 'post'
        self.json = {
            "groupName": group_name,
            "categoryIds": category_ids
        }


class YuncaiGroupPageListApi(BaseManagerApi):
    """查询云采分组列表【查】lcx"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/group/pageList'
        self.method = 'post'
        self.json = {
            "createTimeList": [],
            "page": page,
            "limit": limit,
            "total": 26
        }


class YuncaiGroupStatusApi(BaseManagerApi):
    """修改云采分组状态：关闭【改】lcx"""
    def __init__(self, group_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/group/status?groupId={group_id}&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiGroupUpdateApi(BaseManagerApi):
    """编辑云采分组【改】lcx"""
    def __init__(self, group_id, group_name="{{group_Name}}", category_ids=None):
        if category_ids is None:
            category_ids = [21]
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/group/update'
        self.method = 'post'
        self.json = {
            "groupId": group_id,
            "groupName": group_name,
            "categoryIds": category_ids
        }


class YuncaiVipAddApi(BaseManagerApi):
    """添加会员【增】lcx"""
    def __init__(self, card_type="YEAR", company="测试", sec_company_type="餐饮门店", 
                 credit_limit=100, phone="17788888836", user_name="接口自动化添加", 
                 address="保和街道九寨沟路中迪中心项目部"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/add'
        self.method = 'post'
        self.json = {
            "cardType": card_type,
            "creditFlowMerId": 223,
            "notCreditFlowMerId": 843,
            "company": company,
            "secCompanyType": sec_company_type,
            "creditLimit": credit_limit,
            "phone": phone,
            "userName": user_name,
            "groupIds": [1, 56, 50, 51],
            "vipType": "",
            "address": address,
            "images": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/26/869de8ac715740d38f646481ffe43911qchys2umaa.png",
            "promoterUserId": "8434875",
            "promoterUserName": "发多少",
            "latitude": 30.629241,
            "longitude": 104.131717,
            "provinceCode": 510000,
            "cityCode": 510100,
            "districtCode": 510108,
            "townCode": "",
            "province": "四川省",
            "city": "成都市",
            "district": "成华区",
            "town": "",
            "companyType": "商户"
        }


class YuncaiVipListApi(BaseManagerApi):
    """带条件查询C端会员【查】lcx"""
    def __init__(self, keyword="{{C_vip_contactPhone}}", page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/list'
        self.method = 'post'
        self.json = {
            "cardType": [],
            "examineResult": "",
            "keyword": keyword,
            "requestTime": [],
            "sourceType": "",
            "vipLevelName": [],
            "vipType": [],
            "promoterUserNameLike": "",
            "companyLike": "",
            "isLogoff": "",
            "page": page,
            "limit": limit,
            "total": 157,
            "vipTypeCode": "C"
        }


class YuncaiVipExamineApi(BaseManagerApi):
    """审核B端会员申请【改】lcx"""
    def __init__(self, b_vip_id, credit_limit=100):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/examine'
        self.method = 'post'
        self.json = {
            "id": b_vip_id,
            "creditLimit": credit_limit,
            "vipLimitId": 11862,
            "creditFlowMerId": 223,
            "notCreditFlowMerId": 843,
            "approvalStatus": "PASS"
        }


class YuncaiVipEnableStatusEditApi(BaseManagerApi):
    """修改C端会员状态-开启再调用一次【改】lcx"""
    def __init__(self, c_vip_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/enableStatus/edit?id={c_vip_id}&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiVipCreditStatusEditApi(BaseManagerApi):
    """修改C端会员授信状态-开启【改】lcx"""
    def __init__(self, c_vip_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/creditStatus/edit?id={c_vip_id}&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiVipInfoEditApi(BaseManagerApi):
    """编辑B端会员【改】lcx"""
    def __init__(self, b_vip_id, phone="{{B_vip_phone}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/info/edit'
        self.method = 'post'
        self.json = {
            "id": b_vip_id,
            "cardType": "YEAR",
            "creditFlowMerId": 223,
            "notCreditFlowMerId": 843,
            "company": "测试",
            "secCompanyType": "餐饮门店",
            "creditLimit": 100,
            "phone": phone,
            "userName": "接口自动化添加",
            "vipLimitId": 11862,
            "groupIds": [1, 50, 51, 56],
            "vipType": "PLAT_CREDIT",
            "address": "保和街道九寨沟路中迪中心项目部",
            "images": "https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/09/26/869de8ac715740d38f646481ffe43911qchys2umaa.png",
            "promoterUserId": "8434875",
            "promoterUserName": "发多少",
            "latitude": "30.629241",
            "longitude": "104.131717",
            "provinceCode": 510000,
            "cityCode": 510100,
            "districtCode": 510108,
            "townCode": "",
            "province": "四川省",
            "city": "成都市",
            "district": "成华区",
            "town": "",
            "companyType": "商户"
        }


class YuncaiVipDetailApi(BaseManagerApi):
    """查看C端会员详情【查】lcx"""
    def __init__(self, c_vip_user_id):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/detail?userId={c_vip_user_id}&temp={cur_timestamp}'
        self.method = 'get'


class YuncaiVipListExportApi(BaseManagerApi):
    """导出指定C端会员【查】lcx"""
    def __init__(self, keyword="{{C_vip_contactPhone}}", page=1, limit=20, file_name="会员用户_0926_13_24_24"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/yuncai/vip/list/export'
        self.method = 'post'
        self.json = {
            "cardType": [],
            "examineResult": "",
            "keyword": keyword,
            "requestTime": [],
            "sourceType": "",
            "vipLevelName": [],
            "vipType": [],
            "promoterUserNameLike": "",
            "companyLike": "",
            "isLogoff": "",
            "page": page,
            "limit": limit,
            "total": 1,
            "vipTypeCode": "C",
            "idList": [],
            "fileName": file_name,
            "pageStart": 1,
            "pageEnd": 1,
            "exportFields": [
                {
                    "field": "userId",
                    "sort": 1,
                    "fieldName": "ID",
                    "selected": 0
                },
                {
                    "field": "userName",
                    "sort": 2,
                    "fieldName": "姓名",
                    "selected": 0
                },
                {
                    "field": "contactPhone",
                    "sort": 3,
                    "fieldName": "绑定手机号",
                    "selected": 0
                }
            ]
        }