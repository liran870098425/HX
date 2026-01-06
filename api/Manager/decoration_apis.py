# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : decoration_apis.py
# @author   : 李然 huangxinshenghuo
# @Time     :  16:38
# @Copyright: 焕新生活
from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class AddProductConfigStyleApi(BaseManagerApi):
    """新增商品详情配置【增】lcx"""
    def __init__(self, config_name="商品详情配置自动化测试", config_images="https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/08/19/34b6d94d8caa40d990d9e7c41e5af2db9hvm39tb61.png", config_description=[], status=1, rule_form="", config_type=1, config_position=0, config_goods=0, region_id=0):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/config/style/add'
        self.method = 'post'
        self.data = {
            "configName": config_name,
            "configImages": config_images,
            "configDescription": config_description,
            "status": status,
            "ruleForm": rule_form,
            "configType": config_type,
            "configPosition": config_position,
            "configGoods": config_goods,
            "regionId": region_id
        }


class GetProductConfigStyleListApi(BaseManagerApi):
    """获取商品详情配置列表【查】lcx"""
    def __init__(self, page=1, limit=20, config_type=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/config/style/list'
        self.method = 'post'
        self.data = {
            "page": page,
            "limit": limit,
            "configType": config_type
        }


class UpdateProductConfigStyleStatusApi(BaseManagerApi):
    """修改商品详情配置状态:关闭【改】lcx"""
    def __init__(self, id="{{details_id}}", status="0", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/config/style/open?id={id}&status={status}&temp={temp}'
        self.method = 'get'


class UpdateProductConfigStyleApi(BaseManagerApi):
    """编辑商品详情配置【改】lcx"""
    def __init__(self, id="{{details_id}}", config_name="{{details_configName}}", config_type=1, config_goods=0, config_images="https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/product/2025/08/19/34b6d94d8caa40d990d9e7c41e5af2db9hvm39tb61.png", config_bg_image="", config_text_image="", config_small_image="", config_description=None, status=0, config_position=0, region_id=0):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/config/style/update'
        self.method = 'post'
        self.data = {
            "id": id,
            "configName": config_name,
            "configType": config_type,
            "configGoods": config_goods,
            "configImages": config_images,
            "configBgImage": config_bg_image,
            "configTextImage": config_text_image,
            "configSmallImage": config_small_image,
            "configDescription": config_description,
            "status": status,
            "configPosition": config_position,
            "regionId": region_id
        }


class DeleteProductConfigStyleApi(BaseManagerApi):
    """删除商品详情配置【删】lcx"""
    def __init__(self, id="{{details_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/config/style/delete?id={id}&temp={temp}'
        self.method = 'get'


class EditActivityStrategyApi(BaseManagerApi):
    """编辑活动策略【改】lcx"""
    def __init__(self, name="{{strategy_name}}", trigger_position="START_TRIGGER", display_frequency="CONDITIONAL_TRIGGER", display_interval=0, display_operation=[], trigger_page="11", product_id_list="", product_condition="", product_id_list_file_name="", product_id_list_file_path="", target_user_type="ALL_USER", target_region_ids=[], target_label_types=[], product_category_product_category_id=None, product_category_is_search=False, product_category_is_collect=False, product_category_is_cart=False, product_category_is_buy=False, product_category_is_share=False, product_brand_product_brand_id=None, product_brand_is_search=False, product_brand_is_collect=False, product_brand_is_cart=False, product_brand_is_buy=False, product_brand_is_share=False, coupons=[], active_person=[], country=[], purchase=[], cus_price=[], id=76, begin_time="2025-08-20 00:00:00", end_time="2025-09-30 23:59:59", status=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/edit'
        self.method = 'post'
        self.data = {
            "name": name,
            "triggerPosition": trigger_position,
            "displayFrequency": display_frequency,
            "displayInterval": display_interval,
            "displayOperation": display_operation,
            "triggerPage": trigger_page,
            "productIdList": product_id_list,
            "productCondition": product_condition,
            "productIdListFileName": product_id_list_file_name,
            "productIdListFilePath": product_id_list_file_path,
            "target": {
                "userType": target_user_type,
                "regionIds": target_region_ids,
                "labelTypes": target_label_types,
                "gridType": None,
                "integration": None
            },
            "productCategory": {
                "productCategoryId": product_category_product_category_id,
                "isSearch": product_category_is_search,
                "isCollect": product_category_is_collect,
                "isCart": product_category_is_cart,
                "isBuy": product_category_is_buy,
                "isShare": product_category_is_share,
                "times": []
            },
            "productBrand": {
                "productBrandId": product_brand_product_brand_id,
                "isSearch": product_brand_is_search,
                "isCollect": product_brand_is_collect,
                "isCart": product_brand_is_cart,
                "isBuy": product_brand_is_buy,
                "isShare": product_brand_is_share,
                "times": []
            },
            "coupons": coupons,
            "activePerson": active_person,
            "country": country,
            "purchase": purchase,
            "cusPrice": cus_price,
            "id": id,
            "beginTime": begin_time,
            "endTime": end_time,
            "status": status
        }


class GetActivityStrategyPageApi(BaseManagerApi):
    """获取活动策略列表最后一页【查】lcx"""
    def __init__(self, page="{{strategy_total_Page}}", limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/page'
        self.method = 'post'
        self.data = {
            "page": page,
            "limit": limit
        }


class CreateActivityPopBoxApi(BaseManagerApi):
    """新增活动弹框【增】lcx"""
    def __init__(self, background_pic="https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/user/2025/08/20/f9a09780c85242288a997e977350a502kz4ijb9yda.png", coupons=[], is_system_default_get=1, jump_outside_url="", jump_page="", jump_position="ONLY_SHOW", jump_type=0, name="自动化测试弹框", product_brand_name="", product_category_name=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/create'
        self.method = 'post'
        self.data = {
            "backgroundPic": background_pic,
            "coupons": coupons,
            "isSystemDefaultGet": is_system_default_get,
            "jumpOutsideUrl": jump_outside_url,
            "jumpPage": jump_page,
            "jumpPosition": jump_position,
            "jumpType": jump_type,
            "name": name,
            "productBrandName": product_brand_name,
            "productCategoryName": product_category_name
        }


class GetActivityPopBoxPageApi(BaseManagerApi):
    """查询活动弹框列表最后一页【查】lcx"""
    def __init__(self, page="{{pop_up_pages}}", limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/page'
        self.method = 'post'
        self.data = {
            "page": page,
            "limit": limit
        }


class TurnOnActivityPopBoxApi(BaseManagerApi):
    """开启活动弹框【改】lcx"""
    def __init__(self, id="{{pop_up_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/turnOn?id={id}&temp={temp}'
        self.method = 'get'


class TurnOffActivityPopBoxApi(BaseManagerApi):
    """关闭弹框【改】lcx"""
    def __init__(self, id="{{pop_up_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/turnOff?id={id}&temp={temp}'
        self.method = 'get'


class BindActivityPopBoxApi(BaseManagerApi):
    """活动策略关联弹框【改】lcx"""
    def __init__(self, pop_box_id="{{pop_up_id}}", activity_id="{{strategy_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/bindPopBox?popBoxId={pop_box_id}&activityId={activity_id}&temp={temp}'
        self.method = 'get'


class UnbindActivityPopBoxApi(BaseManagerApi):
    """活动策略解除关联弹窗【改】lcx"""
    def __init__(self, activity_id="{{strategy_id}}", pop_bpx_id="{{pop_up_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/unBindPopBox?activityId={activity_id}&popBpxId={pop_bpx_id}&temp={temp}'
        self.method = 'get'


class GetActivityInfoApi(BaseManagerApi):
    """查看活动策略详情【查】lcx"""
    def __init__(self, id="{{strategy_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/info?id={id}&temp={temp}'
        self.method = 'get'


class GetPopBoxInfoApi(BaseManagerApi):
    """查看活动弹框详情【查】lcx"""
    def __init__(self, id="{{pop_up_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/get?id={id}&temp={temp}'
        self.method = 'get'


class DeleteActivityApi(BaseManagerApi):
    """删除活动【删】lcx"""
    def __init__(self, id="{{strategy_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/delete?id={id}&temp={temp}'
        self.method = 'get'


class DeletePopBoxApi(BaseManagerApi):
    """删除弹框【删】lcx"""
    def __init__(self, id="{{pop_up_id}}", temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/pop/box/delete?id={id}&temp={temp}'
        self.method = 'get'


class ImportHomeRecommendProductApi(BaseManagerApi):
    """批量导入首页推荐商品【增】lcx"""
    def __init__(self, file="file://C:\\Users\\John\\Desktop\\首页商品导入模版-自动化测试.xlsx"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/product/import/excel'
        self.method = 'post'
        self.files = {
            'file': file
        }


class AddActivityPageApi(BaseManagerApi):
    """添加活动页【增】lcx"""
    def __init__(self, activity_code="741258", activity_name="自动化添加", end_date="{{end_time}}", start_date="{{start_time}}", detail_config_json='{"backgroundConfig":{"backgroundColor":"#ff0000","backgroundImage":[]},"data":[{"key":"carouselImage-1755669936060","component":"carouselImage","title":"","margin":{"top":0,"bottom":0,"left":0,"right":0},"autoplaySpeed":4,"showResource":[]},{"key":"singleImage-1755669936060","component":"singleImage","title":"","margin":{"top":0,"bottom":0,"left":0,"right":0},"showResource":[{"imagePath":"","value":""}]},{"key":"slideProduct-1755669936060","component":"slideProduct","title":"","titleColor":"FF0000","margin":{"top":0,"bottom":0,"left":0,"right":0},"isShow":false,"showResource":[]},{"key":"singleWaterfallFlow-1755669936060","component":"singleWaterfallFlow","title":"","titleColor":"FF0000","margin":{"top":0,"bottom":0,"left":0,"right":0},"isShow":false,"showResource":[]}]}'):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/add'
        self.method = 'post'
        self.data = {
            "activityCode": activity_code,
            "activityName": activity_name,
            "endDate": end_date,
            "startDate": start_date,
            "detailConfigJson": detail_config_json
        }


class GetActivityPageListApi(BaseManagerApi):
    """查看活动页列表【查】lcx """
    def __init__(self, activity_status=[], page=1, limit=20, total=0, sort="desc", sort_field="update_time"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/page'
        self.method = 'post'
        self.data = {
            "activityStatus": activity_status,
            "page": page,
            "limit": limit,
            "total": total,
            "sort": sort,
            "sortField": sort_field
        }


class EditActivityPageApi(BaseManagerApi):
    """编辑活动页【改】lcx"""
    def __init__(self, id="{{activity_id}}", activity_code="{{activity_Code}}", activity_name="{{activity_Name}}", end_date="{{end_time}}", start_date="{{start_time}}", detail_config_json='{"backgroundConfig":{"backgroundColor":"#ff0000","backgroundImage":[]},"data":[{"key":"carouselImage-1756880075422","component":"carouselImage","title":"","margin":{"top":0,"bottom":0,"left":0,"right":0},"autoplaySpeed":4,"showResource":[]},{"key":"singleImage-1756880075422","component":"singleImage","title":"","margin":{"top":0,"bottom":0,"left":0,"right":0},"showResource":[{"imagePath":"","value":""}]},{"key":"slideProduct-1756880075422","component":"slideProduct","title":"","titleColor":"FF0000","margin":{"top":0,"bottom":0,"left":0,"right":0},"isShow":false,"showResource":[]},{"key":"singleWaterfallFlow-1756880075422","component":"singleWaterfallFlow","title":"","titleColor":"FF0000","margin":{"top":0,"bottom":0,"left":0,"right":0},"isShow":false,"showResource":[]}]}'):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/edit'
        self.method = 'post'
        self.data = {
            "id": id,
            "activityCode": activity_code,
            "activityName": activity_name,
            "endDate": end_date,
            "startDate": start_date,
            "detailConfigJson": detail_config_json
        }


class CopyActivityPageApi(BaseManagerApi):
    """复制活动页【改】lcx"""
    def __init__(self, id="{{activity_id}}", activity_code="123", activity_name="自动化复制活动", end_date="{{end_time}}", start_date="{{start_time}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/copy'
        self.method = 'post'
        self.data = {
            "id": id,
            "activityCode": activity_code,
            "activityName": activity_name,
            "endDate": end_date,
            "startDate": start_date
        }


class DeleteCopyActivityPageApi(BaseManagerApi):
    """删除复制的活动【删】lcx"""
    def __init__(self, temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/delete/copy_activity_id?temp={temp}'
        self.method = 'get'


class DeleteAddedActivityPageApi(BaseManagerApi):
    """删除添加的活动【删】lcx"""
    def __init__(self, temp=cur_timestamp):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/activity/config/delete/activity_id?temp={temp}'
        self.method = 'get'