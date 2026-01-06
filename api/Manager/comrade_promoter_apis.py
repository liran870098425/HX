from api.base_api import BaseManagerApi


class ComradePromoterInspectorListApi(BaseManagerApi):
    """
    同志推广员信息列表API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/inspector/list'
        self.method = 'GET'


class ComradePromoterCityTreeApi(BaseManagerApi):
    """
    同志推广员添加表单API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/city/tree'
        self.method = 'GET'


class ComradePromoterSaveApi(BaseManagerApi):
    """
    添加同志推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/save'
        self.method = 'POST'


class ComradePromoterImportApi(BaseManagerApi):
    """
    导入同志推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/import'
        self.method = 'POST'


class ComradePromoterExportInspectorApi(BaseManagerApi):
    """
    导出同志推广员API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/export/inspector'
        self.method = 'GET'


class ComradePromoterConfigApi(BaseManagerApi):
    """
    同志推广员规则配置API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/config'
        self.method = 'POST'


class ComradePromoterEditApi(BaseManagerApi):
    """
    同志推广员信息编辑按钮点击API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/edit'
        self.method = 'GET'


class ComradePromoterUpdateApi(BaseManagerApi):
    """
    同志推广员信息编辑API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/comrade/update'
        self.method = 'POST'


class ComradePromoterDeleteApi(BaseManagerApi):
    """
    同志推广员资格取消API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/delete'
        self.method = 'POST'


class ComradePromoterEnableApi(BaseManagerApi):
    """
    同志推广员资格恢复API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/street/user/promotion/100926/enable'
        self.method = 'PUT'