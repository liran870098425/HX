from api.base_api import BaseManagerApi


class PlatformPromoterExceptionNumberStatsApi(BaseManagerApi):
    """
    统计数据-状态API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/number/stats'
        self.method = 'POST'


class PlatformPromoterExceptionDateStatsApi(BaseManagerApi):
    """
    统计数据-异常人数API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/date/stats'
        self.method = 'POST'


class PlatformPromoterExceptionRecordingListApi(BaseManagerApi):
    """
    信息列表-未封API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/recordingList'
        self.method = 'POST'


class PlatformPromoterExceptionRuleListApi(BaseManagerApi):
    """
    异常数据设置查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/rule/list'
        self.method = 'GET'


class PlatformPromoterExceptionRuleEditApi(BaseManagerApi):
    """
    异常数据设置API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/rule/edit'
        self.method = 'POST'


class PlatformExportSelectFieldsApi(BaseManagerApi):
    """
    导出字段选择API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/export/select/fields'
        self.method = 'GET'


class PlatformPromoterExceptionPromoterExceptionRecordingExportCustomFieldApi(BaseManagerApi):
    """
    导出API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/promoter/exception/recording/export/custom/field'
        self.method = 'POST'


class PlatformPromoterExceptionWhiteListListApi(BaseManagerApi):
    """
    白名单数据查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/white/list/list'
        self.method = 'POST'


class PlatformPromoterExceptionWhiteListRuleListApi(BaseManagerApi):
    """
    规避内容获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/white/list/rule/list'
        self.method = 'GET'


class PlatformPromoterExceptionWhiteListSaveApi(BaseManagerApi):
    """
    白名单数据添加API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/white/list/save'
        self.method = 'POST'


class PlatformPromoterExceptionWhiteListRemoveApi(BaseManagerApi):
    """
    移出白名单API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/promoter/exception/white/list/remove'
        self.method = 'GET'