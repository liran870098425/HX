from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformUserRightsListApi(BaseManagerApi):
    """
    删除权益API
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


class PlatformUserRoleRightsPullDownApi(BaseManagerApi):
    """
    新增推广权益-推广角色获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/pull/down'
        self.method = 'GET'


class PlatformSplitCommProGroupGetGroupDropListApi(BaseManagerApi):
    """
    新增推广权益-分佣商品分组获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/splitCommProGroup/getGroupDropList'
        self.method = 'GET'


class PlatformSplitCommProductListApi(BaseManagerApi):
    """
    新增推广权益-分佣商品获取API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/splitCommProduct/list'
        self.method = 'GET'


class PlatformUserRightsDetailApi(BaseManagerApi):
    """
    新增推广权益-推广权益详情查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/169'
        self.method = 'GET'


class PlatformUserRightsSaveApi(BaseManagerApi):
    """
    添加推广类权益-添加权益API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/rights/save'
        self.method = 'POST'


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