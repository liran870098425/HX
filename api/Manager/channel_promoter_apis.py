from api.base_api import BaseManagerApi



class ChannelPromoterInspectorListApi(BaseManagerApi):
    """
    渠道推广员信息列表API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/inspector/list'
        self.method = 'GET'


class ChannelPromoterCityTreeApi(BaseManagerApi):
    """
    渠道推广员添加表单API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/city/tree'
        self.method = 'GET'


class ChannelPromoterSaveApi(BaseManagerApi):
    """
    添加渠道推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/save'
        self.method = 'POST'


class ChannelPromoterImportApi(BaseManagerApi):
    """
    导入渠道推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/import'
        self.method = 'POST'


class ChannelPromoterExportInspectorApi(BaseManagerApi):
    """
    导出渠道推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/export/inspector'
        self.method = 'GET'


class ChannelPromoterConfigApi(BaseManagerApi):
    """
    渠道推广员规则配置API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/config'
        self.method = 'POST'


class ChannelPromoterEditApi(BaseManagerApi):
    """
    渠道推广员信息编辑按钮点击API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/edit'
        self.method = 'GET'


class ChannelPromoterUpdateApi(BaseManagerApi):
    """
    渠道推广员信息编辑API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/channel/update'
        self.method = 'POST'


class ChannelPromoterDeleteApi(BaseManagerApi):
    """
    渠道推广员资格取消API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/delete'
        self.method = 'POST'


class ChannelPromoterEnableApi(BaseManagerApi):
    """
    渠道推广员资格恢复API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/street/user/promotion/100917/enable'
        self.method = 'PUT'