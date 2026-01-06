# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : product_reply_apis.py
# @author   : 李然 
# @Time     :  11:34
# @Copyright: 焕新生活
from api.base_api import BaseMerchantApi
from common.random_util import cur_timestamp


class ProductReplyVirtualApi(BaseMerchantApi):
    """添加自评【增】"""
    def __init__(self, product_id=143435, comment="很好", nickname="接口自动化", 
                 avatar="https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png",
                 pics=None, star=5, attr_value_id=391179, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/reply/virtual'
        self.method = 'post'
        
        if pics is None:
            pics = ["https://oss-dev.likehuanxin.com:7460/cd-huanxin-test/crmebimage/public/content/2025/09/17/824eb6450a33462f90cee52000d378a3op2oe0w02o.png"]
        
        default_data = {
            "avatar": avatar,
            "productId": product_id,
            "comment": comment,
            "nickname": nickname,
            "pics": pics,
            "star": star,
            "attrValueId": attr_value_id
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductReplyListApi(BaseMerchantApi):
    """商品评价列表【查】"""
    def __init__(self, page=1, limit=20, is_reply="", date_limit="", nickname="", 
                 keyword="", is_all="1", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/reply/list?' \
                   f'page={page}&limit={limit}&isReply={is_reply}&dateLimit={date_limit}&' \
                   f'nickname={nickname}&keyword={keyword}&isAll={is_all}&temp={cur_timestamp}'
        self.method = 'get'


class ProductReplyCommentApi(BaseMerchantApi):
    """回复评价【改】"""
    def __init__(self, comment_id, merchant_reply_content="自动化测试回复评价", **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/reply/comment'
        self.method = 'post'
        
        default_data = {
            "id": comment_id,
            "merchantReplyContent": merchant_reply_content
        }
        
        default_data.update(kwargs)
        self.json = default_data


class ProductReplyDeleteApi(BaseMerchantApi):
    """删除商品评价【删】"""
    def __init__(self, comment_id, **kwargs):
        super().__init__()
        self.url = f'{self.host}/api/admin/merchant/product/reply/delete/{comment_id}'
        self.method = 'post'