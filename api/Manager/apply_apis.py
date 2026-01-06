
from api.base_api import BaseManagerApi


class PlatformCityRegionFindCityRegionTreeApi(BaseManagerApi):
    """
    地址获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/region/findCityRegionTree'
        self.method = 'GET'


class PlatformPromoterGetApplyApi(BaseManagerApi):
    """
    未通过列表信息API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/get/apply'
        self.method = 'POST'


class PlatformStreetUserPromotionEnableApi(BaseManagerApi):
    """
    网格员审核拒绝API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/street/user/promotion/100914/enable'
        self.method = 'PUT'


class PlatformPromoterInspectApplyApi(BaseManagerApi):
    """
    网格员审核通过API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/inspect/apply/316/1'
        self.method = 'PUT'