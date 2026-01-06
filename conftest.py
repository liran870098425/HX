# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import time
from typing import List

import jsonpath
import pytest
from xdist.plugin import worker_id

from api.Merchant.login_apis import MerchantLoginApi
from api.base_api import BaseBuyerApi, BaseManagerApi, BaseMerchantApi
# from api.buyer.cart_apis import BuyNowApi
# from api.buyer.checkout_params_apis import SetOrderPayTypeApi, SetOrderAddressIdApi
# from api.buyer.create_trade_apis import CreateTradeApi
# from api.buyer.login_apis import BuyerLoginApi
# from api.buyer.member_address_apis import AddAddressApi
# from api.buyer.order_apis import OrderRogApi
# from api.manager.goods_apis import GoodsBatchAuditApi
from api.Manager.login_apis import ManagerLoginApi
# from api.seller.goods_apis import AddGoodsApi, GoodsUnderApi, GoodsRecycleApi, GoodsDeleteApi
# from api.seller.login_apis import SellerLoginApi
# from api.seller.order_apis import OrderDeliveryApi, OrderPayApi
from common.db_util import DBUtil
from common.file_load import load_yaml_file, write_yaml
from common.json_util import extract_json
from common.logger import GetLogger
from common.redis_util import RedisUtil
from paths_manager import common_yaml_path, redis_yaml_path, db_yaml_path


# 重写pytest内置的钩子函数，来解决pycharm控制台上看到的用例中文乱码
def pytest_collection_modifyitems(items:List['Item'],config:"Config"):
    try:
        addopts = config.getini('addopts') # 获取pytest.ini中addopts的值
        # -sv --alluredir report/data --clean-alluredir -n 2 --dist=each
        if '--dist=each' in addopts:
            # 此时就说明你要用的是多进程并发的each模式，我要得到当前进程的worker_id
            worker_id = config.workerinput.get('workerid')
        else:
            worker_id = None
    except:
        worker_id = None

    # items对象是pytest收集到的所有测试用例对象，他相当于列表
    for item in items:
        # item 就代表一条用例对象
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
        if worker_id:
            item.originalname = item.originalname.encode('utf-8').decode('unicode-escape')+worker_id


@pytest.fixture(scope='session',autouse=True)
def aalogger_init(worker_id):
    GetLogger.get_logger(worker_id).info('日志初始化成功')

# 初始化数据库连接和关闭
@pytest.fixture(scope='session',autouse=False)
def db_init():
    db_info = load_yaml_file(db_yaml_path)
    db_util = DBUtil(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['username'],
        password=db_info['password'],
        database=db_info.get('database', None)  # 添加数据库名称参数，如果配置中没有则默认为None
    )
    yield db_util
    db_util.close()

# 初始化redis连接
@pytest.fixture(scope='session',autouse=False)
def redis_init():
    redis_info = load_yaml_file(redis_yaml_path)
    redis_util = RedisUtil(
        host=redis_info['host'],
        port=redis_info['port'],
        pwd=redis_info['password'],
        decode_responses=False,
        db=0
    )
    yield redis_util

# @pytest.fixture(scope='session',autouse=True)
# def buyer_login(worker_id): # 注意这和worker_id是pytest-xdist插件提供的，你得先安装pytest-xdist
#     # 读取配置文件的基本信息
#     common_info = load_yaml_file(common_yaml_path)
#     usernames = common_info['buyerName'] # 获取的是个列表
#     passwords = common_info['buyerPassword'] # 获取的是个列表
#     if worker_id=='master':
#         api = BuyerLoginApi(usernames[0], passwords[0])
#     else:
#         # gw0/gw1/gw2
#         index = int(worker_id[2:])
#         api = BuyerLoginApi(usernames[index], passwords[index])
#     # if worker_id=='gw0' or worker_id=='master':
#     #     api = BuyerLoginApi('shamo','mtx_9607')
#     # elif worker_id=='gw1':
#     #     api = BuyerLoginApi('shamo123', 'mtx9607')
#     resp = api.send()
#     # print(resp.text)
#     BaseBuyerApi.buyer_token = extract_json(resp.json(),'$.access_token')
#     BaseBuyerApi.uid = extract_json(resp.json(),'$.uid')

@pytest.fixture(scope='session',autouse=True)
def Merchant_login():
    # 读取配置文件的基本信息
    common_info = load_yaml_file(common_yaml_path)
    # 使用正确的配置字段名（从配置文件看应该是sellerName和sellerPassword）
    username = common_info.get('sellerName', 'default_seller')
    password = common_info.get('sellerPassword', 'default_password')
    api = MerchantLoginApi(username, password)
    resp = api.send()
    # print(resp.text)
    resp_json = resp.json()
    # 修复错误的JSON路径访问，使用jsonpath提取token
    token = jsonpath.jsonpath(resp_json, '$..token')
    if token:
        BaseMerchantApi.Merchant_token = token[0]
    else:
        # 如果没有找到token，尝试直接访问token字段
        BaseMerchantApi.Merchant_token = resp_json.get('token')


@pytest.fixture(scope='session',autouse=True)
def manager_login():
    # 读取配置文件的基本信息
    common_info = load_yaml_file(common_yaml_path)
    username = common_info['managerName']
    password = common_info['managerPassword']
    api = ManagerLoginApi(username,password)
    resp = api.send()
    # print(resp.text)
    resp_json = resp.json()
    # 修复错误的JSON路径访问，使用jsonpath提取token
    token = jsonpath.jsonpath(resp_json, '$..token')
    print(token)
    if token:
        BaseManagerApi.manager_token = token[0]  # 取列表第一个元素作为字符串
    else:
        # 如果没有找到token，尝试直接访问data.token字段
        data = resp_json.get('data', {})
        BaseManagerApi.manager_token = data.get('token')

# @pytest.fixture(scope='class',autouse=False)
# def init_order_params(db_init):
#     # 设置订单的支付方式为货到付款
#     SetOrderPayTypeApi().send()
#     # 设置订单收货地址
#     # 从数据库查询当前买家用户名下的收货地址数据，如果数据库有数据，则从数据库中拿到地址id
#     # 如果数据库没有数据，那么我们就新增一个收货地址，从新增接口响应中提取地址id
#     res = db_init.select(f'select addr_id from mtxshop_member.es_member_address where member_id={BaseBuyerApi.uid}')
#     if len(res)>0:
#         address_id = res[0]['addr_id']
#     else:
#         # 调用添加收货地址接口，造一条数据
#         resp = AddAddressApi().send()
#         address_id = jsonpath.jsonpath(resp.json(),'$..addr_id')[0]
#     SetOrderAddressIdApi(address_id=address_id).send()

# @pytest.fixture(scope='class',autouse=False)
# def goods_data(db_init):
#     # 添加商品
#     resp = AddGoodsApi().send()
#     # 提取goods_id作为后续接口使用
#     goods_id = resp.json()['goods_id']
#     # 管理员审核商品
#     GoodsBatchAuditApi(goods_ids=[goods_id]).send()
#     # 审核完成后产生sku_id，审核接口的响应是空的
#     # 可以在数据库中查询出该商品对应的sku_id
#     res = db_init.select(f'select sku_id from mtxshop_goods.es_goods_sku where goods_id={goods_id}')
#     sku_id = res[0]['sku_id']
#     yield goods_id,sku_id
#     # 后置处理，数据清除
#     GoodsUnderApi(goods_ids=[goods_id]).send()
#     GoodsRecycleApi(goods_ids=[goods_id]).send()
#     GoodsDeleteApi(goods_ids=[goods_id]).send()
#
# @pytest.fixture(scope='class',autouse=False)
# def order_data(request,goods_data,init_order_params):
#     order_status = request.param # 拿到fixture的外部传参，赋值给order_status这个变量
#     sku_id = goods_data[1]
#     BuyNowApi(sku_id=sku_id).send()
#     resp = CreateTradeApi().send()
#     order_sn = extract_json(resp.json(),'$..sn')
#     pay_price = extract_json(resp.json(),'$..total_price')
#     time.sleep(2)
#     if order_status=='已发货':
#         OrderDeliveryApi(order_sn=order_sn).send()
#     elif order_status=='已收货':
#         OrderDeliveryApi(order_sn=order_sn).send()
#         OrderRogApi(order_sn=order_sn).send()
#     elif order_status=='已收款':
#         OrderDeliveryApi(order_sn=order_sn).send()
#         OrderRogApi(order_sn=order_sn).send()
#         OrderPayApi(order_sn=order_sn,pay_price=pay_price).send()
#     yield sku_id,order_sn,order_status

def pytest_terminal_summary(terminalreporter,exitstatus,config):
    # 统计测试结果
    passed = len(terminalreporter.stats.get('passed',[]))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    total = passed+failed+error+skipped

    write_yaml('result.yml',{'total':total,"passed":passed,"failed":failed,"error":error,"skipped":skipped})


if __name__ == '__main__':
    s = 'gw1'
    print(s[2:])

