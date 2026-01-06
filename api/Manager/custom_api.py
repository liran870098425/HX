from api.base_api import BaseManagerApi


class PlatformCityCustomListApi(BaseManagerApi):
    """
    自定义地区列表数据查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/custom/list'
        self.method = 'POST'


class PlatformCityCustomSaveApi(BaseManagerApi):
    """
    自定义地区添加API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/custom/save'
        self.method = 'POST'


class PlatformCityCustomGetRegionApi(BaseManagerApi):
    """
    自定义地区编辑表单API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/custom/getRegion'
        self.method = 'GET'


class PlatformCityCustomUpdateApi(BaseManagerApi):
    """
    自定义地区修改API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/custom/update'
        self.method = 'POST'


class PlatformCityCustomDeleteApi(BaseManagerApi):
    """
    自定义地区删除API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/city/custom/delete'
        self.method = 'GET'