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
    """删除权益 Copy API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/list?temp={temp}&page={page}&limit={limit}&total={total}'
        self.method = 'get'


class PlatformUserRoleModelModelTreeApi(BaseManagerApi):
    """新增商品价格权益-业务模块获取API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/role/model/model/tree?temp={temp}'
        self.method = 'get'


class PlatformUserRightsProductTypesApi(BaseManagerApi):
    """新增商品权益-商品类型获取 API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/productTypes?temp={temp}'
        self.method = 'get'


class PlatformUserRightsDiscountTypesApi(BaseManagerApi):
    """新增推广权益-折扣类型获取 API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/discountTypes?temp={temp}'
        self.method = 'get'


class PlatformUserRightsSaveApi(BaseManagerApi):
    """添加推广类权益-分组商品添加API"""
    def __init__(self, modelId="", rightsTypeId="", rightsTypeName="", rightsName="", externalType="portion", productPriceRuleRequests=None, productIds=None, importProductIds=None, excludeProductIds=None, importExcludeProductIds=None, timeType="day", rightsValidity="permanent", rightsDescribe="", discountName=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/rights/save'
        self.method = 'post'
        if productPriceRuleRequests is None:
            productPriceRuleRequests = [
                {
                    "code": "normal",
                    "name": "普通商品",
                    "ruleType": "percentage",
                    "discountValue": 1
                },
                {
                    "code": "YUN_CAI",
                    "name": "云采商品",
                    "ruleType": "percentage",
                    "discountValue": 1
                }
            ]
        if productIds is None:
            productIds = [143477]
        if importProductIds is None:
            importProductIds = []
        if excludeProductIds is None:
            excludeProductIds = []
        if importExcludeProductIds is None:
            importExcludeProductIds = []
        self.json = {
            "modelId": modelId,
            "rightsTypeId": rightsTypeId,
            "rightsTypeName": rightsTypeName,
            "rightsName": rightsName,
            "rightsProductPriceAddRequest": {
                "externalType": externalType,
                "productPriceRuleRequests": productPriceRuleRequests,
                "productIds": productIds,
                "importProductIds": importProductIds,
                "excludeProductIds": excludeProductIds,
                "importExcludeProductIds": importExcludeProductIds
            },
            "timeType": timeType,
            "rightsValidity": rightsValidity,
            "rightsDescribe": rightsDescribe,
            "discountName": discountName
        }


class PlatformUserRightsQylbQyid3Api(BaseManagerApi):
    """新增推广权益-推广权益详情查看API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/qylb_qyid3?temp={temp}&page={page}&limit={limit}&total={total}'
        self.method = 'get'


class PlatformUserRightsUpdateApi(BaseManagerApi):
    """添加推广类权益-权益修改API"""
    def __init__(self, id="", modelId="", rightsTypeId="", rightsTypeName="", rightsName="", externalType="portion", productPriceRuleRequests=None, productIds=None, importProductIds=None, excludeProductIds=None, importExcludeProductIds=None, timeType="day", rightsValidity="permanent", rightsDescribe="", discountName=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/user/rights/update'
        self.method = 'put'
        if productPriceRuleRequests is None:
            productPriceRuleRequests = [
                {
                    "code": "normal",
                    "name": "普通商品",
                    "ruleType": "percentage",
                    "discountValue": 1
                },
                {
                    "code": "YUN_CAI",
                    "name": "云采商品",
                    "ruleType": "percentage",
                    "discountValue": 1
                }
            ]
        if productIds is None:
            productIds = [143477]
        if importProductIds is None:
            importProductIds = []
        if excludeProductIds is None:
            excludeProductIds = []
        if importExcludeProductIds is None:
            importExcludeProductIds = []
        self.json = {
            "id": id,
            "modelId": modelId,
            "rightsTypeId": rightsTypeId,
            "rightsTypeName": rightsTypeName,
            "rightsName": rightsName,
            "rightsProductPriceAddRequest": {
                "externalType": externalType,
                "productPriceRuleRequests": productPriceRuleRequests,
                "productIds": productIds,
                "importProductIds": importProductIds,
                "excludeProductIds": excludeProductIds,
                "importExcludeProductIds": importExcludeProductIds
            },
            "timeType": timeType,
            "rightsValidity": rightsValidity,
            "rightsDescribe": rightsDescribe,
            "discountName": discountName
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
    def __init__(self, roleRightsId="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/rights/association/disassociate?roleRightsId={roleRightsId}&temp={temp}'
        self.method = 'get'