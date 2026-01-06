from api.base_api import BaseManagerApi



class PlatformPromoterOverviewDistrictListApi(BaseManagerApi):
    """
    推广员概览区县列表信息查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/overview/district/list'
        self.method = 'GET'


class PlatformPromoterOverviewTownListApi(BaseManagerApi):
    """
    推广员概览镇列表信息查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/overview/town/list'
        self.method = 'GET'


class PlatformPromoterOverviewVillageListApi(BaseManagerApi):
    """
    推广员概览村列表信息查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/overview/village/list'
        self.method = 'GET'


class PlatformPromoterOverviewDistrictExcelListApi(BaseManagerApi):
    """
    推广员概览区县导出API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/overview/district/excel/list'
        self.method = 'GET'