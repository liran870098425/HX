


from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformOrderAllPayTypeApi(BaseManagerApi):
    """支付方式获取--曾API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/order/all/pay/type?temp={temp}'
        self.method = 'get'


class PlatformOrderPlatformOrderSelectMerchantApi(BaseManagerApi):
    """商户信息获取 API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/order/platform/order/select/merchant?temp={temp}'
        self.method = 'get'


class PlatformOrderPlatformOrderSelectSupplierApi(BaseManagerApi):
    """供应商信息获取 API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/order/platform/order/select/supplier?temp={temp}'
        self.method = 'get'


class PlatformOrderPlatformOrderSelectBrandApi(BaseManagerApi):
    """品牌信息搜索API"""
    def __init__(self, code=200, message=None, data=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/platform/order/select/brand'
        self.method = 'post'
        if data is None:
            data = [
                {
                    "id": 187,
                    "name": "奥普（AUPU）",
                    "icon": "",
                    "sort": 1,
                    "isShow": True,
                    "isDel": False,
                    "createTime": "2024-04-10 18:01:24",
                    "updateTime": "2024-07-08 19:05:31",
                    "categoryId": None,
                    "score": 0,
                    "status": None,
                    "merchantId": None,
                    "rejectReason": None
                }
            ]
        self.json = {
            "code": code,
            "message": message,
            "data": data
        }


class PlatformOrderPostPlatformMoneyStatisticsApi(BaseManagerApi):
    """统计数据获取API"""
    def __init__(self, keyWord="", categoryIds=None, limit=15, orderNo="", page=1, paid="", payType=None, refundNo="", refundTime=None, regionId=None, status="all", refundStatus=None, statusList=None, supplierIds=None, brandIds=None, userKeyWord="", version=0, check=False, merchantIds=None, productCategory=None, isTicket=None, subsidyType="", couponId="", companyName=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/post/platform/money/statistics'
        self.method = 'post'
        if categoryIds is None:
            categoryIds = []
        if payType is None:
            payType = []
        if refundTime is None:
            refundTime = []
        if regionId is None:
            regionId = []
        if refundStatus is None:
            refundStatus = []
        if statusList is None:
            statusList = []
        if supplierIds is None:
            supplierIds = []
        if brandIds is None:
            brandIds = []
        if merchantIds is None:
            merchantIds = []
        if productCategory is None:
            productCategory = []
        self.json = {
            "keyWord": keyWord,
            "categoryIds": categoryIds,
            "limit": limit,
            "orderNo": orderNo,
            "page": page,
            "paid": paid,
            "payType": payType,
            "refundNo": refundNo,
            "refundTime": refundTime,
            "regionId": regionId,
            "status": status,
            "refundStatus": refundStatus,
            "statusList": statusList,
            "supplierIds": supplierIds,
            "brandIds": brandIds,
            "userKeyWord": userKeyWord,
            "version": version,
            "check": check,
            "merchantIds": merchantIds,
            "productCategory": productCategory,
            "isTicket": isTicket,
            "subsidyType": subsidyType,
            "couponId": couponId,
            "companyName": companyName
        }


class PlatformOrderStatusNumApi(BaseManagerApi):
    """数量信息统计API"""
    def __init__(self, keyWord="", categoryIds=None, limit=15, orderNo="", page=1, paid="", payType=None, refundNo="", refundTime=None, regionId=None, status="all", refundStatus=None, statusList=None, supplierIds=None, brandIds=None, userKeyWord="", version=0, check=False, merchantIds=None, productCategory=None, isTicket=None, subsidyType="", couponId="", companyName=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/status/num'
        self.method = 'post'
        if categoryIds is None:
            categoryIds = []
        if payType is None:
            payType = []
        if refundTime is None:
            refundTime = []
        if regionId is None:
            regionId = []
        if refundStatus is None:
            refundStatus = []
        if statusList is None:
            statusList = []
        if supplierIds is None:
            supplierIds = []
        if brandIds is None:
            brandIds = []
        if merchantIds is None:
            merchantIds = []
        if productCategory is None:
            productCategory = []
        self.json = {
            "keyWord": keyWord,
            "categoryIds": categoryIds,
            "limit": limit,
            "orderNo": orderNo,
            "page": page,
            "paid": paid,
            "payType": payType,
            "refundNo": refundNo,
            "refundTime": refundTime,
            "regionId": regionId,
            "status": status,
            "refundStatus": refundStatus,
            "statusList": statusList,
            "supplierIds": supplierIds,
            "brandIds": brandIds,
            "userKeyWord": userKeyWord,
            "version": version,
            "check": check,
            "merchantIds": merchantIds,
            "productCategory": productCategory,
            "isTicket": isTicket,
            "subsidyType": subsidyType,
            "couponId": couponId,
            "companyName": companyName
        }


class PlatformOrderListApi(BaseManagerApi):
    """列表信息获取API"""
    def __init__(self, keyWord="", categoryIds=None, limit=15, orderNo="", page=1, paid="", payType=None, refundNo="", refundTime=None, regionId=None, status="all", refundStatus=None, statusList=None, supplierIds=None, brandIds=None, userKeyWord="", version=0, check=False, merchantIds=None, productCategory=None, isTicket=None, subsidyType="", couponId="", companyName=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/list'
        self.method = 'post'
        if categoryIds is None:
            categoryIds = []
        if payType is None:
            payType = []
        if refundTime is None:
            refundTime = []
        if regionId is None:
            regionId = []
        if refundStatus is None:
            refundStatus = []
        if statusList is None:
            statusList = []
        if supplierIds is None:
            supplierIds = []
        if brandIds is None:
            brandIds = []
        if merchantIds is None:
            merchantIds = []
        if productCategory is None:
            productCategory = []
        self.json = {
            "keyWord": keyWord,
            "categoryIds": categoryIds,
            "limit": limit,
            "orderNo": orderNo,
            "page": page,
            "paid": paid,
            "payType": payType,
            "refundNo": refundNo,
            "refundTime": refundTime,
            "regionId": regionId,
            "status": status,
            "refundStatus": refundStatus,
            "statusList": statusList,
            "supplierIds": supplierIds,
            "brandIds": brandIds,
            "userKeyWord": userKeyWord,
            "version": version,
            "check": check,
            "merchantIds": merchantIds,
            "productCategory": productCategory,
            "isTicket": isTicket,
            "subsidyType": subsidyType,
            "couponId": couponId,
            "companyName": companyName
        }


class PlatformOrderInfoApi(BaseManagerApi):
    """订单详情查看API"""
    def __init__(self, orderNo="{{dd-orderNo}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/order/info?temp={temp}&orderNo={orderNo}'
        self.method = 'get'


class PlatformOrderDdOrderNoInvoiceListApi(BaseManagerApi):
    """订单审核状态API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/order/dd-orderNo/invoice/list?temp={temp}'
        self.method = 'get'


class PlatformOrderUserPhoneApi(BaseManagerApi):
    """查看用户绑定手机号API"""
    def __init__(self, orderNo="{{dd-orderNo}}", phoneType=1, isShowPhone=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/order/user/phone'
        self.method = 'post'
        self.json = {
            "orderNo": orderNo,
            "phoneType": phoneType,
            "isShowPhone": isShowPhone
        }


class PlatformExportSelectFieldsApi(BaseManagerApi):
    """导出字段获取API"""
    def __init__(self, type="platform_refund_order_export_type", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/export/select/fields?temp={temp}&type={type}'
        self.method = 'get'


class PlatformExportOrderExcelRecCustomApi(BaseManagerApi):
    """下载申请提交API"""
    def __init__(self, keyWord="", categoryIds=None, limit=15, orderNo="", page=1, paid="", payType=None, refundNo="", refundTime=None, regionId=None, status="all", refundStatus=None, statusList=None, supplierIds=None, brandIds=None, userKeyWord="", version=0, check=False, merchantIds=None, productCategory=None, isTicket=None, subsidyType="", couponId="", companyName="", orderEndTime="2025-10-24 23:59:59", orderStartTime="2025-9-24 00:00:00", orderIdList=None, fileName="订单列表_1024_10_54_24", pageStart=1, pageEnd=39, exportFields=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/export/order/excel/rec/custom'
        self.method = 'post'
        if categoryIds is None:
            categoryIds = []
        if payType is None:
            payType = []
        if refundTime is None:
            refundTime = []
        if regionId is None:
            regionId = []
        if refundStatus is None:
            refundStatus = []
        if statusList is None:
            statusList = []
        if supplierIds is None:
            supplierIds = []
        if brandIds is None:
            brandIds = []
        if merchantIds is None:
            merchantIds = []
        if productCategory is None:
            productCategory = []
        if orderIdList is None:
            orderIdList = []
        if exportFields is None:
            exportFields = [
                {
                    "field": "orderNo",
                    "sort": 1,
                    "fieldName": "订单号",
                    "selected": 0
                },
                {
                    "field": "consigneeName",
                    "sort": 2,
                    "fieldName": "收货人",
                    "selected": 0
                },
                {
                    "field": "productName",
                    "sort": 3,
                    "fieldName": "商品信息",
                    "selected": 0
                },
                {
                    "field": "productNum",
                    "sort": 4,
                    "fieldName": "商品数量",
                    "selected": 0
                },
                {
                    "field": "productPrice",
                    "sort": 5,
                    "fieldName": "商品价格",
                    "selected": 0
                },
                {
                    "field": "payPrice",
                    "sort": 6,
                    "fieldName": "实际支付金额",
                    "selected": 0
                },
                {
                    "field": "subsidyMoney",
                    "sort": 7,
                    "fieldName": "补贴金额",
                    "selected": 0
                },
                {
                    "field": "finalPrice",
                    "sort": 8,
                    "fieldName": "成交价",
                    "selected": 0
                },
                {
                    "field": "payType",
                    "sort": 9,
                    "fieldName": "支付方式",
                    "selected": 0
                },
                {
                    "field": "status",
                    "sort": 10,
                    "fieldName": "订单状态",
                    "selected": 0
                },
                {
                    "field": "paidStr",
                    "sort": 11,
                    "fieldName": "支付状态",
                    "selected": 0
                },
                {
                    "field": "userId",
                    "sort": 18,
                    "fieldName": "用户Id",
                    "selected": 0
                },
                {
                    "field": "userPhone",
                    "sort": 19,
                    "fieldName": "用户绑定手机号",
                    "selected": 0
                },
                {
                    "field": "consigneePhone",
                    "sort": 20,
                    "fieldName": "收货人电话",
                    "selected": 0
                },
                {
                    "field": "shippingType",
                    "sort": 26,
                    "fieldName": "配送方式",
                    "selected": 0
                },
                {
                    "field": "payee",
                    "sort": 27,
                    "fieldName": "收款单位",
                    "selected": 0
                },
                {
                    "field": "refundNo",
                    "sort": 28,
                    "fieldName": "退款单号",
                    "selected": 0
                },
                {
                    "field": "spreadPhone",
                    "sort": 29,
                    "fieldName": "推广人手机号",
                    "selected": 0
                },
                {
                    "field": "deliveryRemark",
                    "sort": 30,
                    "fieldName": "发货备注",
                    "selected": 0
                },
                {
                    "field": "userRemark",
                    "sort": 31,
                    "fieldName": "用户备注",
                    "selected": 0
                },
                {
                    "field": "merchantRemark",
                    "sort": 32,
                    "fieldName": "商户备注",
                    "selected": 0
                },
                {
                    "field": "brandName",
                    "sort": 33,
                    "fieldName": "品牌",
                    "selected": 0
                },
                {
                    "field": "supplierName",
                    "sort": 34,
                    "fieldName": "供应商",
                    "selected": 0
                },
                {
                    "field": "deliveryNum",
                    "sort": 35,
                    "fieldName": "发货数量",
                    "selected": 0
                },
                {
                    "field": "refundNum",
                    "sort": 36,
                    "fieldName": "退款中数量",
                    "selected": 0
                },
                {
                    "field": "refundSuccessNum",
                    "sort": 37,
                    "fieldName": "退款成功数量",
                    "selected": 0
                },
                {
                    "field": "deliveryCompany",
                    "sort": 38,
                    "fieldName": "物流公司",
                    "selected": 0
                },
                {
                    "field": "trackingON",
                    "sort": 39,
                    "fieldName": "物流单号",
                    "selected": 0
                },
                {
                    "field": "deliveryName",
                    "sort": 40,
                    "fieldName": "发货人",
                    "selected": 0
                },
                {
                    "field": "deliveryModifyName",
                    "sort": 43,
                    "fieldName": "物流修改人",
                    "selected": 0
                },
                {
                    "field": "oldDeliveryCompany",
                    "sort": 46,
                    "fieldName": "原物流公司",
                    "selected": 0
                },
                {
                    "field": "oldTrackingON",
                    "sort": 47,
                    "fieldName": "原物流单号",
                    "selected": 0
                },
                {
                    "field": "newDeliveryCompany",
                    "sort": 48,
                    "fieldName": "现物流公司",
                    "selected": 0
                },
                {
                    "field": "newTrackingON",
                    "sort": 49,
                    "fieldName": "现物流单号",
                    "selected": 0
                },
                {
                    "field": "refundApprover",
                    "sort": 50,
                    "fieldName": "退款审批人",
                    "selected": 0
                },
                {
                    "field": "refundApproverResult",
                    "sort": 53,
                    "fieldName": "退款审批结果",
                    "selected": 0
                },
                {
                    "field": "merchantName",
                    "sort": 54,
                    "fieldName": "商户名称",
                    "selected": 0
                },
                {
                    "field": "productAttr",
                    "sort": 55,
                    "fieldName": "商品规格",
                    "selected": 0
                },
                {
                    "field": "productId",
                    "sort": 56,
                    "fieldName": "商品id",
                    "selected": 0
                },
                {
                    "field": "productModel",
                    "sort": 57,
                    "fieldName": "商品型号",
                    "selected": 0
                },
                {
                    "field": "productCategory",
                    "sort": 58,
                    "fieldName": "商品类型",
                    "selected": 0
                },
                {
                    "field": "exchangeType",
                    "sort": 59,
                    "fieldName": "焕新币类型",
                    "selected": 0
                },
                {
                    "field": "exchangeMoney",
                    "sort": 60,
                    "fieldName": "焕新币金额",
                    "selected": 0
                },
                {
                    "field": "primaryClass",
                    "sort": 61,
                    "fieldName": "一级分类",
                    "selected": 0
                },
                {
                    "field": "secondaryClass",
                    "sort": 62,
                    "fieldName": "二级分类",
                    "selected": 0
                },
                {
                    "field": "threeLevelClass",
                    "sort": 63,
                    "fieldName": "三级分类",
                    "selected": 0
                },
                {
                    "field": "couponNames",
                    "sort": 66,
                    "fieldName": "补贴券",
                    "selected": 0
                },
                {
                    "field": "CSCouponInfo",
                    "sort": 69,
                    "fieldName": "补贴信息",
                    "selected": 0
                },
                {
                    "field": "realName",
                    "sort": 70,
                    "fieldName": "国补用户姓名",
                    "selected": 0
                },
                {
                    "field": "idCard",
                    "sort": 71,
                    "fieldName": "国补用户身份证",
                    "selected": 0
                },
                {
                    "field": "userRelPhone",
                    "sort": 72,
                    "fieldName": "用户注册手机号",
                    "selected": 0
                },
                {
                    "field": "govCategoryName",
                    "sort": 73,
                    "fieldName": "国补品类",
                    "selected": 0
                },
                {
                    "field": "govRatio",
                    "sort": 74,
                    "fieldName": "国补比例",
                    "selected": 0
                },
                {
                    "field": "govMoney",
                    "sort": 75,
                    "fieldName": "国补金额",
                    "selected": 0
                },
                {
                    "field": "paymentName",
                    "sort": 76,
                    "fieldName": "支付宝姓名",
                    "selected": 0
                },
                {
                    "field": "paymentAccount",
                    "sort": 77,
                    "fieldName": "支付宝账号",
                    "selected": 0
                },
                {
                    "field": "addressProvince",
                    "sort": 21,
                    "fieldName": "省",
                    "selected": 0
                },
                {
                    "field": "addressCity",
                    "sort": 22,
                    "fieldName": "市",
                    "selected": 0
                },
                {
                    "field": "addressDistrict",
                    "sort": 23,
                    "fieldName": "区/县",
                    "selected": 0
                },
                {
                    "field": "addressStreet",
                    "sort": 24,
                    "fieldName": "街道",
                    "selected": 0
                },
                {
                    "field": "addressDetail",
                    "sort": 25,
                    "fieldName": "收货地址",
                    "selected": 0
                },
                {
                    "field": "createDate",
                    "sort": 12,
                    "fieldName": "创建日期",
                    "selected": 0
                },
                {
                    "field": "createTime",
                    "sort": 13,
                    "fieldName": "创建时间",
                    "selected": 0
                },
                {
                    "field": "payDate",
                    "sort": 14,
                    "fieldName": "支付日期",
                    "selected": 0
                },
                {
                    "field": "payTime",
                    "sort": 15,
                    "fieldName": "支付时间",
                    "selected": 0
                },
                {
                    "field": "refundDate",
                    "sort": 16,
                    "fieldName": "退款日期",
                    "selected": 0
                },
                {
                    "field": "refundTime",
                    "sort": 17,
                    "fieldName": "退款时间",
                    "selected": 0
                },
                {
                    "field": "deliveryDate",
                    "sort": 41,
                    "fieldName": "发货日期",
                    "selected": 0
                },
                {
                    "field": "deliveryTime",
                    "sort": 42,
                    "fieldName": "发货时间",
                    "selected": 0
                },
                {
                    "field": "deliveryModifyDate",
                    "sort": 44,
                    "fieldName": "物流修改日期",
                    "selected": 0
                },
                {
                    "field": "deliveryModifyTime",
                    "sort": 45,
                    "fieldName": "物流修改时间",
                    "selected": 0
                },
                {
                    "field": "refundApproverDate",
                    "sort": 51,
                    "fieldName": "退款审批日期",
                    "selected": 0
                },
                {
                    "field": "refundApproverTime",
                    "sort": 52,
                    "fieldName": "退款审批时间",
                    "selected": 0
                },
                {
                    "field": "receivingDate",
                    "sort": 64,
                    "fieldName": "收货日期",
                    "selected": 0
                },
                {
                    "field": "receivingTime",
                    "sort": 65,
                    "fieldName": "收货时间",
                    "selected": 0
                },
                {
                    "field": "yunCaiCategoryName",
                    "sort": 78,
                    "fieldName": "云采商品类目",
                    "selected": 0
                },
                {
                    "field": "ycRegAddr",
                    "sort": 79,
                    "fieldName": "云采会员注册地址",
                    "selected": 0
                },
                {
                    "field": "company",
                    "sort": 80,
                    "fieldName": "店铺名称",
                    "selected": 0
                },
                {
                    "field": "promoterUserName",
                    "sort": 80,
                    "fieldName": "对接人姓名",
                    "selected": 0
                },
                {
                    "field": "orderTime",
                    "sort": 81,
                    "fieldName": "下单时间",
                    "selected": 0
                }
            ]
        self.json = {
            "keyWord": keyWord,
            "categoryIds": categoryIds,
            "limit": limit,
            "orderNo": orderNo,
            "page": page,
            "paid": paid,
            "payType": payType,
            "refundNo": refundNo,
            "refundTime": refundTime,
            "regionId": regionId,
            "status": status,
            "refundStatus": refundStatus,
            "statusList": statusList,
            "supplierIds": supplierIds,
            "brandIds": brandIds,
            "userKeyWord": userKeyWord,
            "version": version,
            "check": check,
            "merchantIds": merchantIds,
            "productCategory": productCategory,
            "isTicket": isTicket,
            "subsidyType": subsidyType,
            "couponId": couponId,
            "companyName": companyName,
            "orderEndTime": orderEndTime,
            "orderStartTime": orderStartTime,
            "orderIdList": orderIdList,
            "fileName": fileName,
            "pageStart": pageStart,
            "pageEnd": pageEnd,
            "exportFields": exportFields
        }


class PlatformMerchantListApi(BaseManagerApi):
    """商户名称 API"""
    def __init__(self, limit=10, page=1, keywords="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/merchant/list?temp={temp}&limit={limit}&page={page}&keywords={keywords}'
        self.method = 'get'


class PlatformAfterOrderStatusNumApi(BaseManagerApi):
    """统计数据获取API"""
    def __init__(self, page=1, limit=20, afterSalesType="", dateLimit="", keywords="", merId="", merchantName="", orderNo="", processingState=9, saleNo="", businessRecord="false", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/order/status/num?page={page}&limit={limit}&afterSalesType={afterSalesType}&dateLimit={dateLimit}&keywords={keywords}&merId={merId}&merchantName={merchantName}&orderNo={orderNo}&processingState={processingState}&saleNo={saleNo}&businessRecord={businessRecord}&temp={temp}'
        self.method = 'get'


class PlatformAfterOrderTypeListApi(BaseManagerApi):
    """售后类型API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/order/type/list?temp={temp}'
        self.method = 'get'


class PlatformAfterOrderListApi(BaseManagerApi):
    """列表信息-待处理API"""
    def __init__(self, page=1, limit=20, afterSalesType="", dateLimit="", keywords="", merId="", merchantName="", orderNo="", processingState=0, saleNo="", businessRecord="false", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/order/list?page={page}&limit={limit}&afterSalesType={afterSalesType}&dateLimit={dateLimit}&keywords={keywords}&merId={merId}&merchantName={merchantName}&orderNo={orderNo}&processingState={processingState}&saleNo={saleNo}&businessRecord={businessRecord}&temp={temp}'
        self.method = 'get'


class PlatformAfterOrderExportApi(BaseManagerApi):
    """订单导出API"""
    def __init__(self, page=1, limit=20, afterSalesType="", dateLimit="", keywords="", merId="", merchantName="", orderNo="", processingState=9, saleNo="", saleNos=None, businessRecord=False):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/after/order/export'
        self.method = 'post'
        if saleNos is None:
            saleNos = ["{{dd_saleNo}}"]
        self.json = {
            "page": page,
            "limit": limit,
            "afterSalesType": afterSalesType,
            "dateLimit": dateLimit,
            "keywords": keywords,
            "merId": merId,
            "merchantName": merchantName,
            "orderNo": orderNo,
            "processingState": processingState,
            "saleNo": saleNo,
            "saleNos": saleNos,
            "businessRecord": businessRecord
        }


class PlatformRefundOrderListApi(BaseManagerApi):
    """列表信息API"""
    def __init__(self, refundStatus=9, dateLimit="", orderNo="", refundOrderNo="", page=1, limit=20, startTime="", endTime="", keyword="", saleNo="", type="PLATFORM", businessRecord="false", isAll=1, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/refund/order/list?refundStatus={refundStatus}&dateLimit={dateLimit}&orderNo={orderNo}&refundOrderNo={refundOrderNo}&page={page}&limit={limit}&startTime={startTime}&endTime={endTime}&keyword={keyword}&saleNo={saleNo}&type={type}&businessRecord={businessRecord}&isAll={isAll}&temp={temp}'
        self.method = 'get'


class PlatformRefundOrderStatusNumApi(BaseManagerApi):
    """统计数据API"""
    def __init__(self, refundStatus=9, dateLimit="", orderNo="", refundOrderNo="", page=1, limit=20, startTime="", endTime="", keyword="", saleNo="", type="PLATFORM", businessRecord="false", isAll=1, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/refund/order/status/num?refundStatus={refundStatus}&dateLimit={dateLimit}&orderNo={orderNo}&refundOrderNo={refundOrderNo}&page={page}&limit={limit}&startTime={startTime}&endTime={endTime}&keyword={keyword}&saleNo={saleNo}&type={type}&businessRecord={businessRecord}&isAll={isAll}&temp={temp}'
        self.method = 'get'


class PlatformRefundOrderDetailTkdRefundOrderNoApi(BaseManagerApi):
    """详情查看API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/refund/order/detail/tkd_refundOrderNo?temp={temp}'
        self.method = 'get'


class PlatformRefundOrderMarkApi(BaseManagerApi):
    """订单备注API"""
    def __init__(self, remark="1", refundOrderNo="{{tkd_refundOrderNo}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/refund/order/mark'
        self.method = 'post'
        self.json = {
            "remark": remark,
            "refundOrderNo": refundOrderNo
        }


class PlatformRefundOrderOrderExcelCustomApi(BaseManagerApi):
    """导出申请API"""
    def __init__(self, refundStatus=9, dateLimit="", orderNo="", refundOrderNo="", page=1, limit=20, merId=None, startTime="", endTime="", keyword="", saleNo="", type="PLATFORM", refundOrderIds=None, businessRecord=False, refundOrderNoList=None, isAll=1, fileName="退款单列表_0821_13_47_18", pageStart=1, pageEnd=136, exportFields=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/refund/order/order/excel/custom'
        self.method = 'post'
        if refundOrderIds is None:
            refundOrderIds = []
        if refundOrderNoList is None:
            refundOrderNoList = []
        if exportFields is None:
            exportFields = [
                {
                    "field": "saleNo",
                    "sort": 1,
                    "fieldName": "售后单号",
                    "selected": 0
                },
                {
                    "field": "refundOrderNo",
                    "sort": 2,
                    "fieldName": "退款单号",
                    "selected": 0
                },
                {
                    "field": "orderNo",
                    "sort": 3,
                    "fieldName": "订单号",
                    "selected": 0
                },
                {
                    "field": "nickName",
                    "sort": 4,
                    "fieldName": "用户昵称",
                    "selected": 0
                },
                {
                    "field": "refundPrice",
                    "sort": 5,
                    "fieldName": "退款金额",
                    "selected": 0
                },
                {
                    "field": "refundStatus",
                    "sort": 6,
                    "fieldName": "退款状态",
                    "selected": 0
                },
                {
                    "field": "afterSalesType",
                    "sort": 7,
                    "fieldName": "售后类型",
                    "selected": 0
                },
                {
                    "field": "returnGoodsType",
                    "sort": 8,
                    "fieldName": "退货类型",
                    "selected": 0
                },
                {
                    "field": "createTime",
                    "sort": 9,
                    "fieldName": "创建时间",
                    "selected": 0
                },
                {
                    "field": "merRemark",
                    "sort": 10,
                    "fieldName": "商家备注",
                    "selected": 0
                },
                {
                    "field": "productName",
                    "sort": 11,
                    "fieldName": "商品名称",
                    "selected": 0
                },
                {
                    "field": "deliveryTime",
                    "sort": 12,
                    "fieldName": "发货时间",
                    "selected": 0
                },
                {
                    "field": "platformRemark",
                    "sort": 13,
                    "fieldName": "平台备注",
                    "selected": 0
                },
                {
                    "field": "merName",
                    "sort": 14,
                    "fieldName": "商户名称",
                    "selected": 0
                },
                {
                    "field": "userPhone",
                    "sort": 15,
                    "fieldName": "用户电话",
                    "selected": 0
                },
                {
                    "field": "shippingType",
                    "sort": 16,
                    "fieldName": "配送方式",
                    "selected": 0
                },
                {
                    "field": "consigneePhone",
                    "sort": 17,
                    "fieldName": "收货电话",
                    "selected": 0
                },
                {
                    "field": "consigneeName",
                    "sort": 18,
                    "fieldName": "收货人",
                    "selected": 0
                },
                {
                    "field": "consigneeAddress",
                    "sort": 19,
                    "fieldName": "收货地址",
                    "selected": 0
                },
                {
                    "field": "payNum",
                    "sort": 20,
                    "fieldName": "商品总数",
                    "selected": 0
                },
                {
                    "field": "paid",
                    "sort": 21,
                    "fieldName": "支付状态",
                    "selected": 0
                },
                {
                    "field": "payType",
                    "sort": 22,
                    "fieldName": "支付方式",
                    "selected": 0
                },
                {
                    "field": "payTime",
                    "sort": 23,
                    "fieldName": "支付时间",
                    "selected": 0
                },
                {
                    "field": "totalPrice",
                    "sort": 24,
                    "fieldName": "商品总价",
                    "selected": 0
                },
                {
                    "field": "platCouponPrice",
                    "sort": 25,
                    "fieldName": "平台优惠金额",
                    "selected": 0
                },
                {
                    "field": "gainIntegral",
                    "sort": 26,
                    "fieldName": "赠送积分",
                    "selected": 0
                },
                {
                    "field": "finalPrice",
                    "sort": 27,
                    "fieldName": "实际支付金额",
                    "selected": 0
                },
                {
                    "field": "useIntegral",
                    "sort": 28,
                    "fieldName": "抵除抵扣积分",
                    "selected": 0
                },
                {
                    "field": "isCompulsoryRefund",
                    "sort": 29,
                    "fieldName": "是否强制退款",
                    "selected": 0
                }
            ]
        self.json = {
            "refundStatus": refundStatus,
            "dateLimit": dateLimit,
            "orderNo": orderNo,
            "refundOrderNo": refundOrderNo,
            "page": page,
            "limit": limit,
            "merId": merId,
            "startTime": startTime,
            "endTime": endTime,
            "keyword": keyword,
            "saleNo": saleNo,
            "type": type,
            "refundOrderIds": refundOrderIds,
            "businessRecord": businessRecord,
            "refundOrderNoList": refundOrderNoList,
            "isAll": isAll,
            "fileName": fileName,
            "pageStart": pageStart,
            "pageEnd": pageEnd,
            "exportFields": exportFields
        }


class PlatformAfterOrderRefundIssueListApi(BaseManagerApi):
    """列表信息API"""
    def __init__(self, platformType=2, status=-1, dateLimit="", saleNo="", orderNo="", page=1, limit=20, workNo="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/order/refund/issue/list?platformType={platformType}&status={status}&dateLimit={dateLimit}&saleNo={saleNo}&orderNo={orderNo}&page={page}&limit={limit}&workNo={workNo}&temp={temp}'
        self.method = 'get'


class PlatformAfterOrderRefundIssueStatusNumApi(BaseManagerApi):
    """统计数据API"""
    def __init__(self, platformType=2, status=-1, dateLimit="", saleNo="", orderNo="", page=1, limit=20, workNo="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/order/refund/issue/status/num?platformType={platformType}&status={status}&dateLimit={dateLimit}&saleNo={saleNo}&orderNo={orderNo}&page={page}&limit={limit}&workNo={workNo}&temp={temp}'
        self.method = 'get'


class PlatformAfterOrderRefundIssueExportApi(BaseManagerApi):
    """导出申请 API"""
    def __init__(self, platformType=2, status=-1, dateLimit="", saleNo="", orderNo="", page=1, limit=20, merId=None, workNo="", workNoList=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/after/order/refund/issue/export'
        self.method = 'post'
        if workNoList is None:
            workNoList = ["{{tkdd-id}}"]
        self.json = {
            "platformType": platformType,
            "status": status,
            "dateLimit": dateLimit,
            "saleNo": saleNo,
            "orderNo": orderNo,
            "page": page,
            "limit": limit,
            "merId": merId,
            "workNo": workNo,
            "workNoList": workNoList
        }


class PlatformAfterSaleCompensateTypeApi(BaseManagerApi):
    """赔付类型API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/type?temp={temp}'
        self.method = 'get'


class PlatformAfterSaleCompensateWayApi(BaseManagerApi):
    """赔付方式 API"""
    def __init__(self, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/way?temp={temp}'
        self.method = 'get'


class PlatformAfterSaleCompensateListApi(BaseManagerApi):
    """列表信息API"""
    def __init__(self, page=1, limit=20, approvalResult=None, compensateStatus=None, compensateTimes=None, compensateType="", compensateWay="", createTimes=None, merId="", orderNo="", workNo="", ids=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/list'
        self.method = 'post'
        if compensateTimes is None:
            compensateTimes = []
        if createTimes is None:
            createTimes = []
        if ids is None:
            ids = []
        self.json = {
            "page": page,
            "limit": limit,
            "approvalResult": approvalResult,
            "compensateStatus": compensateStatus,
            "compensateTimes": compensateTimes,
            "compensateType": compensateType,
            "compensateWay": compensateWay,
            "createTimes": createTimes,
            "merId": merId,
            "orderNo": orderNo,
            "workNo": workNo,
            "ids": ids
        }


class PlatformAfterSaleCompensateStatisticsApi(BaseManagerApi):
    """统计信息API"""
    def __init__(self, page=1, limit=20, approvalResult=None, compensateStatus=None, compensateTimes=None, compensateType="", compensateWay="", createTimes=None, merId="", orderNo="", workNo="", ids=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/statistics'
        self.method = 'post'
        if compensateTimes is None:
            compensateTimes = []
        if createTimes is None:
            createTimes = []
        if ids is None:
            ids = []
        self.json = {
            "page": page,
            "limit": limit,
            "approvalResult": approvalResult,
            "compensateStatus": compensateStatus,
            "compensateTimes": compensateTimes,
            "compensateType": compensateType,
            "compensateWay": compensateWay,
            "createTimes": createTimes,
            "merId": merId,
            "orderNo": orderNo,
            "workNo": workNo,
            "ids": ids
        }


class PlatformAfterSaleCompensateDetailApi(BaseManagerApi):
    """详情查看API"""
    def __init__(self, id="{{pffl_ddid}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/detail?temp={temp}&id={id}'
        self.method = 'get'


class PlatformAfterSaleCompensateExportApi(BaseManagerApi):
    """导出--曾API"""
    def __init__(self, page=1, limit=20, approvalResult=None, compensateStatus=None, compensateTimes=None, compensateType="", compensateWay="", createTimes=None, merId="", orderNo="", workNo="", ids=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/after/sale/compensate/export'
        self.method = 'post'
        if compensateTimes is None:
            compensateTimes = []
        if createTimes is None:
            createTimes = []
        if ids is None:
            ids = ["{{pffl_ddid}}"]
        self.json = {
            "page": page,
            "limit": limit,
            "approvalResult": approvalResult,
            "compensateStatus": compensateStatus,
            "compensateTimes": compensateTimes,
            "compensateType": compensateType,
            "compensateWay": compensateWay,
            "createTimes": createTimes,
            "merId": merId,
            "orderNo": orderNo,
            "workNo": workNo,
            "ids": ids
        }