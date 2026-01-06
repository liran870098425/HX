from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformStreetUserPromotionRecordApi(BaseManagerApi):
    """分佣记录信息获取API"""
    def __init__(self, page=1, limit=20, total=0, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/record?page={page}&limit={limit}&total={total}&temp={temp}'
        self.method = 'get'


class PlatformStreetUserPromotionRecordStatisticsApi(BaseManagerApi):
    """统计数据查看API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/record/statistics?temp={temp}'
        self.method = 'get'


class PlatformStreetUserPromotionRecordExportFieldsApi(BaseManagerApi):
    """导出字段获取API"""
    def __init__(self, type="platform_user_integral_export", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/record/export/fields?type={type}&temp={temp}'
        self.method = 'get'


class PlatformStreetUserPromotionRecordExportApi(BaseManagerApi):
    """导出申请API"""
    def __init__(self, page=1, limit="{{fyjl_limit}}", total="{{fyjl_total}}", ids=None, isAll=1, fileName="分佣记录_0821_09_35_36", pageStart=1, pageEnd="{{fyjl_ymid}}", exportFields=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/street/user/promotion/record/export'
        self.method = 'post'
        if ids is None:
            ids = []
        if exportFields is None:
            exportFields = [
                {
                    "id": None,
                    "field": "{{fyjl_dcid}}",
                    "fieldName": "{{fyjl_fieldname}}",
                    "sort": 1,
                    "selected": None,
                    "createTime": None,
                    "updateTime": None,
                    "templateId": None
                }
            ]
        self.json = {
            "page": page,
            "limit": limit,
            "total": total,
            "ids": ids,
            "isAll": isAll,
            "fileName": fileName,
            "pageStart": pageStart,
            "pageEnd": pageEnd,
            "exportFields": exportFields
        }