from api.base_api import BaseManagerApi
from common.random_util import cur_timestamp


class PlatformFinanceMerchantClosingConfigEditApi(BaseManagerApi):
    """编辑设置【改】lcxAPI"""
    def __init__(self, guaranteedAmount=150, transferMaxAmount=5000, transferMinAmount=10, merchantShareNode="complete", merchantShareFreezeTime=7):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/finance/merchant/closing/config/edit'
        self.method = 'post'
        self.json = {
            "guaranteedAmount": guaranteedAmount,
            "transferMaxAmount": transferMaxAmount,
            "transferMinAmount": transferMinAmount,
            "merchantShareNode": merchantShareNode,
            "merchantShareFreezeTime": merchantShareFreezeTime
        }


class PlatformFinanceFundsFlowApi(BaseManagerApi):
    """资金流水列表【查】lcxAPI"""
    def __init__(self, orderNo="", dateLimit="", page=1, limit=20, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/finance/funds/flow?orderNo={orderNo}&dateLimit={dateLimit}&page={page}&limit={limit}&temp={temp}'
        self.method = 'get'


class PlatformFinanceSummaryFinancialStatementsApi(BaseManagerApi):
    """流水汇总列表【查】lcxAPI"""
    def __init__(self, page=1, limit=20, dateLimit="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/finance/summary/financial/statements?page={page}&limit={limit}&dateLimit={dateLimit}&temp={temp}'
        self.method = 'get'


class PlatformPlatRecListPageApi(BaseManagerApi):
    """对账管理列表查询【查】lcxAPI"""
    def __init__(self, recType="ordinary", limit=20, page=1, recStatus="", partnerStampStatus="", platformStampStatus="", provRegionId=0, citiRegionId=0, distRegionId=0, keyword="", startTime="", endTime=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/plat/rec/list/page'
        self.method = 'post'
        self.json = {
            "recType": recType,
            "limit": limit,
            "page": page,
            "recStatus": recStatus,
            "partnerStampStatus": partnerStampStatus,
            "platformStampStatus": platformStampStatus,
            "provRegionId": provRegionId,
            "citiRegionId": citiRegionId,
            "distRegionId": distRegionId,
            "keyword": keyword,
            "startTime": startTime,
            "endTime": endTime
        }


class PlatformPlatRecDetailApi(BaseManagerApi):
    """对账明细【查】lcxAPI"""
    def __init__(self, recType="ordinary", orderNo="", id="{{bill_id}}", limit=20, page=1, startTime="", endTime="", keyword="", productType="", orderType="all", isAll=1, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/plat/rec/detail?recType={recType}&orderNo={orderNo}&id={id}&limit={limit}&page={page}&startTime={startTime}&endTime={endTime}&keyword={keyword}&productType={productType}&orderType={orderType}&isAll={isAll}&temp={temp}'
        self.method = 'get'


class PlatformPlatRecBillPushApi(BaseManagerApi):
    """对账推送【改】lcxAPI"""
    def __init__(self, serialNo="{{serial_No}}"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/plat/rec/bill/push'
        self.method = 'post'
        self.json = {
            "serialNo": serialNo
        }


class PlatformPlatRecExportApi(BaseManagerApi):
    """导出账单【查】lcxAPI"""
    def __init__(self, recType="ordinary", limit=20, page=1, recStatus="", partnerStampStatus="", platformStampStatus="", provRegionId=0, citiRegionId=0, distRegionId=0, keyword="", startTime="", endTime="", serialNoArr=None):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/plat/rec/export'
        self.method = 'post'
        if serialNoArr is None:
            serialNoArr = []
        self.json = {
            "recType": recType,
            "limit": limit,
            "page": page,
            "recStatus": recStatus,
            "partnerStampStatus": partnerStampStatus,
            "platformStampStatus": platformStampStatus,
            "provRegionId": provRegionId,
            "citiRegionId": citiRegionId,
            "distRegionId": distRegionId,
            "keyword": keyword,
            "startTime": startTime,
            "endTime": endTime,
            "serialNoArr": serialNoArr
        }


class PlatformWithdrawListApi(BaseManagerApi):
    """查询提现列表【查】lcxAPI"""
    def __init__(self, checkUser="", applyTime=None, withdrawNo="", userId="", withdrawStatus="", page=1, limit=20):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/withdraw/list'
        self.method = 'post'
        if applyTime is None:
            applyTime = []
        self.json = {
            "checkUser": checkUser,
            "applyTime": applyTime,
            "withdrawNo": withdrawNo,
            "userId": userId,
            "withdrawStatus": withdrawStatus,
            "page": page,
            "limit": limit
        }


class PlatformWithdrawGetWithdrawDetailApi(BaseManagerApi):
    """查看提现详情【查】lcxAPI"""
    def __init__(self, id="{{withdraw_id}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/withdraw/getWithdrawDetail?id={id}&temp={temp}'
        self.method = 'get'


class PlatformHxCoinRecordAddApplyApi(BaseManagerApi):
    """发放申请（CDK编码）【增】lcxAPI"""
    def __init__(self, note="测试", name="自动化CDK发放", signUpTotal="", singleAmount="250", townType=None, work="", timeVal=None, detail="", signUpDeadline="", activityPoster="", streetNum="", importFileName="", importFileUrl="", issuedWay=1, issuedQuantity="1", endTime="{{date_soon}}", beginTime="{{date_recent}}", fileName="", phoneList=None, totalAmount="250.00"):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/hx/coin/record/add/apply'
        self.method = 'post'
        if timeVal is None:
            timeVal = ["{{date_recent}}", "{{date_soon}}"]
        if phoneList is None:
            phoneList = []
        self.json = {
            "note": note,
            "name": name,
            "signUpTotal": signUpTotal,
            "singleAmount": singleAmount,
            "townType": townType,
            "work": work,
            "timeVal": timeVal,
            "detail": detail,
            "signUpDeadline": signUpDeadline,
            "activityPoster": activityPoster,
            "streetNum": streetNum,
            "importFileName": importFileName,
            "importFileUrl": importFileUrl,
            "issuedWay": issuedWay,
            "issuedQuantity": issuedQuantity,
            "endTime": endTime,
            "beginTime": beginTime,
            "fileName": fileName,
            "phoneList": phoneList,
            "totalAmount": totalAmount
        }


class PlatformHxCoinRecordListApi(BaseManagerApi):
    """发放列表-cdk【查】lcx API"""
    def __init__(self, limit=15, dateLimit=None, keyword="", page=1, city="", district="", town="", province="", village="", townType="", order="", sort="", status=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/hx/coin/record/list'
        self.method = 'post'
        if dateLimit is None:
            dateLimit = []
        self.json = {
            "limit": limit,
            "dateLimit": dateLimit,
            "keyword": keyword,
            "page": page,
            "city": city,
            "district": district,
            "town": town,
            "province": province,
            "village": village,
            "townType": townType,
            "order": order,
            "sort": sort,
            "status": status
        }


class PlatformHxCoinRecordReviewPassApi(BaseManagerApi):
    """审核cdk发放（通过）【改】lcxAPI"""
    def __init__(self, rid="{{cdkgrant_id}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/hx/coin/record/review/pass?rid={rid}&temp={temp}'
        self.method = 'get'


class PlatformHxCoinRecordDownloadPhoneApi(BaseManagerApi):
    """手机账号发送记录里面导入文件查看【查】lcxAPI"""
    def __init__(self, rid="{{grant_id}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/hx/coin/record/download/phone?rid={rid}&temp={temp}'
        self.method = 'get'


class PlatformHxCoinPhoneRecordListApi(BaseManagerApi):
    """查看手机账号发送记录【查】lcxAPI"""
    def __init__(self, rid="{{grant_id}}", page=1, limit=20, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/hx/coin/phone/record/list?rid={rid}&page={page}&limit={limit}&temp={temp}'
        self.method = 'get'


class PlatformUserModifyExchangeMoneyApi(BaseManagerApi):
    """调修改焕新币的接口把手机号发放那个用户发的焕新币减掉【改】lcxAPI"""
    def __init__(self, amount="-{{single_Amount}}", userid="{{grant_uid}}", mode="sub", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/user/modify/exchange/money?amount={amount}&userid={userid}&mode={mode}&temp={temp}'
        self.method = 'get'


class PlatformHxCoinRecordDownloadCdkApi(BaseManagerApi):
    """下载兑换记录里面的CDK文档【查】lcxAPI"""
    def __init__(self, rid="{{cdkgrant_id}}", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/hx/coin/record/download/cdk?rid={rid}&temp={temp}'
        self.method = 'get'


class PlatformHxCoinCdkExchangeRecordApi(BaseManagerApi):
    """查看兑换记录【查】lcxAPI"""
    def __init__(self, rid="{{cdkgrant_id}}", page=1, limit=20, temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/hx/coin/cdk/exchange/record?rid={rid}&page={page}&limit={limit}&temp={temp}'
        self.method = 'get'


class PlatformAutoTicketListApi(BaseManagerApi):
    """开票列表查询【查】lcxAPI"""
    def __init__(self, status=-1, merName="", companyName="", taxNumber="", taxOfficeId="", taxOfficePhone="", createTime="", rejectionReason="", page=1, limit=20, dateLimit="", platformType=2, saleNo="", orderNo="", workNo="", sex="", temp=""):
        super().__init__()
        if not temp:
            temp = cur_timestamp
        self.url = f'{self.host}/api/admin/platform/auto/ticket/list?status={status}&merName={merName}&companyName={companyName}&taxNumber={taxNumber}&taxOfficeId={taxOfficeId}&taxOfficePhone={taxOfficePhone}&createTime={createTime}&rejectionReason={rejectionReason}&page={page}&limit={limit}&dateLimit={dateLimit}&platformType={platformType}&saleNo={saleNo}&orderNo={orderNo}&workNo={workNo}&sex={sex}&temp={temp}'
        self.method = 'get'


class PlatformAutoTicketExportApi(BaseManagerApi):
    """开票列表指定第一条数据导出【查】lcxAPI"""
    def __init__(self, id=None, status=-1, merName="", companyName="", taxNumber="", taxOfficeId="", taxOfficePhone="", createTime="", rejectionReason="", page=1, limit=20, dateLimit="", ids=None, platformType=2, saleNo="", orderNo="", merId=None, workNo="", workNoList=None, sex=""):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/auto/ticket/export'
        self.method = 'post'
        if ids is None:
            ids = ["{{ticket_id}}"]
        if workNoList is None:
            workNoList = []
        self.json = {
            "id": id,
            "status": status,
            "merName": merName,
            "companyName": companyName,
            "taxNumber": taxNumber,
            "taxOfficeId": taxOfficeId,
            "taxOfficePhone": taxOfficePhone,
            "createTime": createTime,
            "rejectionReason": rejectionReason,
            "page": page,
            "limit": limit,
            "dateLimit": dateLimit,
            "ids": ids,
            "platformType": platformType,
            "saleNo": saleNo,
            "orderNo": orderNo,
            "merId": merId,
            "workNo": workNo,
            "workNoList": workNoList,
            "sex": sex
        }


class PlatformAutoTicketExamineApi(BaseManagerApi):
    """审核：同意【改】lcxAPI"""
    def __init__(self, id="{{ticket_id}}", status=1):
        super().__init__()
        self.url = f'{self.host}/api/admin/platform/auto/ticket/examine'
        self.method = 'post'
        self.json = {
            "id": id,
            "status": status
        }