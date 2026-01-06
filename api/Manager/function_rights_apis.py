from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformRightsTypeListApi(BaseManagerApi):
    """权益类型获取API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/rights/type/list?page={page}&limit={limit}&total={total}&temp={temp}'
        self.method = 'get'


class PlatformUserRightsListApi(BaseManagerApi):
    """搜索API"""
    def __init__(self, rightTypeId="", page=1, limit=20, total=42, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/list?rightTypeId={rightTypeId}&page={page}&limit={limit}&total={total}&temp={temp}'
        self.method = 'get'


class PlatformUserRoleModelModelTreeApi(BaseManagerApi):
    """新增功能权益-业务模块获取API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/role/model/model/tree?temp={temp}'
        self.method = 'get'


class PlatformSplitCommProGroupGetServiceGroupDropListApi(BaseManagerApi):
    """新增推广权益-商品分类获取API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/splitCommProGroup/getServiceGroupDropList?temp={temp}'
        self.method = 'get'


class PlatformUserRightsQylbQyid2Api(BaseManagerApi):
    """权益详情查看API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/qylb_qyid2?temp={temp}&page={page}&limit={limit}&total={total}'
        self.method = 'get'


class PlatformUserRightsUpdateApi(BaseManagerApi):
    """添加推广类权益-权益修改API"""
    def __init__(self, id="", modelId="", rightsTypeId="", rightsTypeName="", rightsName="", timeType="day", rightsValidity="permanent", rightsDescribe="", rightsFunction="cash_on_delivery", paymentTime=2, externalIds=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/rights/update'
        self.method = 'put'
        if externalIds is None:
            externalIds = [36]
        self.json = {
            "id": id,
            "modelId": modelId,
            "rightsTypeId": rightsTypeId,
            "rightsTypeName": rightsTypeName,
            "rightsName": rightsName,
            "timeType": timeType,
            "rightsValidity": rightsValidity,
            "rightsDescribe": rightsDescribe,
            "rightsServiceAddRequest": {
                "rightsFunction": rightsFunction,
                "paymentTime": paymentTime,
                "externalIds": externalIds
            }
        }


class PlatformUserRolePageListApi(BaseManagerApi):
    """角色id获取API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/role/page/list?temp={temp}&page={page}&limit={limit}&total={total}'
        self.method = 'get'


class PlatformUserRoleRightsConfigApi(BaseManagerApi):
    """角色权益绑定API"""
    def __init__(self, roleId="", rightsIds=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/role/rights/config'
        self.method = 'post'
        if rightsIds is None:
            rightsIds = []
        self.json = {
            "roleId": roleId,
            "rightsIds": rightsIds
        }


class PlatformUserRightsAsslistApi(BaseManagerApi):
    """权益绑定查看API"""
    def __init__(self, page=1, limit=20, total=0, assId="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/asslist?temp={temp}&page={page}&limit={limit}&total={total}&assId={assId}'
        self.method = 'get'


class PlatformUserRightsAssociationDisassociateApi(BaseManagerApi):
    """权益绑定取消API"""
    def __init__(self, page=1, limit=20, total=0, roleRightsId="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/association/disassociate?temp={temp}&page={page}&limit={limit}&total={total}&roleRightsId={roleRightsId}'
        self.method = 'get'