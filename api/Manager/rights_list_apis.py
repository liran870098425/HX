from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformRightsTypeListApi(BaseManagerApi):
    """
    权益类型获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/rights/type/list'
        self.method = 'GET'


class PlatformUserRightsListApi(BaseManagerApi):
    """
    列表数据获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/list'
        self.method = 'GET'


class PlatformUserRoleModelModelTreeApi(BaseManagerApi):
    """
    新增推广权益-业务模块获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/model/model/tree'
        self.method = 'GET'


class PlatformProductCategoryCacheTreeApi(BaseManagerApi):
    """
    新增推广权益-商品分类获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/product/category/cache/tree'
        self.method = 'GET'


class PlatformIconConfigActivityPullDownApi(BaseManagerApi):
    """
    新增页面权益-活动专题获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/icon/config/activity/pull/down'
        self.method = 'GET'


class PlatformUserRightsUpdateApi(BaseManagerApi):
    """
    添加推广类权益-权益修改API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/update'
        self.method = 'PUT'


class PlatformUserRolePageListApi(BaseManagerApi):
    """
    角色id获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/page/list'
        self.method = 'GET'


class PlatformUserRoleRightsConfigApi(BaseManagerApi):
    """
    角色权益绑定API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/config'
        self.method = 'POST'


class PlatformUserRightsAsslistApi(BaseManagerApi):
    """
    权益绑定查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/asslist'
        self.method = 'GET'


class PlatformUserRightsAssociationDisassociateApi(BaseManagerApi):
    """
    权益绑定取消API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/association/disassociate'
        self.method = 'GET'