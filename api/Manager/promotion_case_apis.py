from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformPromoterMotivationGetMotivationConfigApi(BaseManagerApi):
    """获取限制信息API"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/getMotivationConfig'
        self.method = 'get'


class PlatformPromoterMotivationGrantApi(BaseManagerApi):
    """grantAPI"""
    def __init__(self, code=200, message=None, data=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/grant'
        self.method = 'post'
        self.json = {
            "code": code,
            "message": message,
            "data": data
        }


class PlatformPromoterMotivationGetMotivationPlanEnumsApi(BaseManagerApi):
    """活动状态获取API"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/getMotivationPlanEnums'
        self.method = 'get'


class PlatformPromoterMotivationPageAllApi(BaseManagerApi):
    """列表数据获取 CopyAPI"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/page/all'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit
        }


class PlatformPromoterMotivationCommissionPageJljhHdidApi(BaseManagerApi):
    """活动详情查看API"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/commission/page/jljh_hdid?page={page}&limit={limit}'
        self.method = 'get'


class PlatformPromoterMotivationJljhHdidApi(BaseManagerApi):
    """活动方案信息查看API"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/jljh_hdid'
        self.method = 'get'


class PlatformPromoterNormalPageApi(BaseManagerApi):
    """推广角色获取API"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/normal/page?page={page}&limit={limit}'
        self.method = 'get'


class PlatformPromoterMotivationCommitApi(BaseManagerApi):
    """添加活动API"""
    def __init__(self, promoters=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/commit'
        self.method = 'post'
        if promoters is None:
            promoters = [
                {
                    "userId": 8434138,
                    "provinceCode": 510000,
                    "cityCode": 510100,
                    "districtCode": 510115,
                    "name": "测试",
                    "phone": "13333000100",
                    "town": "柳城街道",
                    "townCode": "510115001",
                    "village": "c",
                    "work": None,
                    "townType": None,
                    "subCount": 30,
                    "province": "四川省",
                    "city": "成都市",
                    "district": "温江区",
                    "promoterType": "street",
                    "promoterTypeStr": "街道推广",
                    "minPersonCount": 0,
                    "maxPercent": 90,
                    "motivateNum": 1,
                    "motivatePrice": 1,
                    "totalMotivatePrice": 1,
                    "commissionStartTime": " {{$date.now|addDays(1)|format('yyyy-MM-dd')}} 00:00:00",
                    "commissionEndTime": "{{$date.now|addDays(2)|format('yyyy-MM-dd')}} 23:59:59",
                    "promoterId": 100907
                }
            ]
        self.json = promoters


class PlatformPromoterMotivationOverApi(BaseManagerApi):
    """删除活动--曾API"""
    def __init__(self, activityIds=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/over'
        self.method = 'post'
        if activityIds is None:
            activityIds = ["{{jljh1_hdid1}}"]
        self.json = activityIds


class PlatformPromoterMotivationPageApi(BaseManagerApi):
    """列表数据获取API"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/page'
        self.method = 'post'
        self.json = {
            "page": page,
            "limit": limit
        }


class PlatformPromoterMotivationCommissionPageJljh1HdidApi(BaseManagerApi):
    """活动详情查看API"""
    def __init__(self, page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/commission/page/jljh1_hdid?page={page}&limit={limit}'
        self.method = 'get'


class PlatformPromoterMotivationJljh1HdidApi(BaseManagerApi):
    """活动方案信息查看API"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/promoter/motivation/jljh1_hdid'
        self.method = 'get'