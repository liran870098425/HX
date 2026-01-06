from api.base_api import BaseManagerApi


class PlatformSystemUserLevelListApi(BaseManagerApi):
    """
    用户等级列表信息查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/list'
        self.method = 'GET'


class PlatformSystemUserLevelSaveApi(BaseManagerApi):
    """
    用户等级添加API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/save'
        self.method = 'POST'


class PlatformSystemUserLevelUpdateApi(BaseManagerApi):
    """
    用户等级修改API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/update'
        self.method = 'POST'


class PlatformSystemUserLevelDeleteApi(BaseManagerApi):
    """
    用户等级删除API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/delete/yhdj_id'
        self.method = 'POST'


class PlatformSystemUserLevelUpdateConfigApi(BaseManagerApi):
    """
    用户等级配置开启API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/update/config'
        self.method = 'POST'


class PlatformSystemUserLevelGetRuleApi(BaseManagerApi):
    """
    用户等级说明查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/get/rule'
        self.method = 'GET'


class PlatformSystemUserLevelUpdateRuleApi(BaseManagerApi):
    """
    用户等级说明提交API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/system/user/level/update/rule'
        self.method = 'POST'