from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformUserRolePageListApi(BaseManagerApi):
    """
    角色列表查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/page/list'
        self.method = 'GET'


class PlatformUserRoleAddApi(BaseManagerApi):
    """
    添加推广角色API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/add'
        self.method = 'POST'


class PlatformUserRoleStatusApi(BaseManagerApi):
    """
    开启角色API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/status'
        self.method = 'GET'


class PlatformUserRoleRightsConfigLeftApi(BaseManagerApi):
    """
    已配置权限API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/config/left'
        self.method = 'GET'


class PlatformUserRoleRightsConfigTypeApi(BaseManagerApi):
    """
    可配置权益类型API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/config/type'
        self.method = 'GET'


class PlatformUserRoleRightsConfigOffsideApi(BaseManagerApi):
    """
    商品价格类权益API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/config/offside'
        self.method = 'GET'


class PlatformUserRoleRightsConfigApi(BaseManagerApi):
    """
    角色权益关联API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/config'
        self.method = 'POST'


class PlatformUserRoleDetailApi(BaseManagerApi):
    """
    角色编辑列表API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/detail'
        self.method = 'GET'


class PlatformUserRoleEditApi(BaseManagerApi):
    """
    角色编辑API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/edit'
        self.method = 'POST'


class PlatformUserRoleRightsInfoApi(BaseManagerApi):
    """
    角色-详情-账号信息API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/user/role/rights/info'
        self.method = 'GET'


class PlatformRightsTypeTypePageApi(BaseManagerApi):
    """
    角色类型列表查看API
    """
    # CRUD标识，用于权限控制
    _crud = 'r'  # read操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/rights/type/type/page'
        self.method = 'GET'


class PlatformRightsTypeAddApi(BaseManagerApi):
    """
    角色类型添加API
    """
    # CRUD标识，用于权限控制
    _crud = 'c'  # create操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/rights/type/add'
        self.method = 'POST'


class PlatformRightsTypeEditApi(BaseManagerApi):
    """
    角色类型修改API
    """
    # CRUD标识，用于权限控制
    _crud = 'u'  # update操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/rights/type/edit'
        self.method = 'POST'


class PlatformRightsTypeDeleteApi(BaseManagerApi):
    """
    角色类型列表删除API
    """
    # CRUD标识，用于权限控制
    _crud = 'd'  # delete操作
    
    def __init__(self):
        super().__init__()
        self.path = '/api/admin/platform/rights/type/delete'
        self.method = 'GET'