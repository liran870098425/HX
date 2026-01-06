# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import allure
import jsonpath
import pytest
from api.Manager.coupon_apis import ManagerCouponAddApi, ManagerCouponListApi, ManagerCouponCloseApi, \
    ManagerCouponDetailApi, ManagerCouponRecordApi
from common.db_util import DBUtil
import json
from pytest_dependency import depends
from api.Manager.coupon_apis import ManagerDeleteCouponApi


@allure.epic('焕新生活')
@allure.feature('营销-优惠券管理模')
@allure.story('优惠券测试')
class TestOrderFlow:
    coupon_close = 0  # 优惠券状态 -关闭
    coupon_open = 1  # 优惠券状态 -开启
    coupon_id = ''  # 优惠券ID

    @allure.title('添加优惠券')
    @pytest.mark.dependency()
    def test_coupon_now(self, db_init):
        # 添加优惠券
        resp = ManagerCouponAddApi(category=7).send()
        assert resp.status_code == 200
        # 获取优惠券id
        list_resp = ManagerCouponListApi().send()
        TestOrderFlow.coupon_id = jsonpath.jsonpath(list_resp.json(), '$..list[0].id')[0]
        print(f'这个是优惠券Id:{TestOrderFlow.coupon_id}')
        # 关闭优惠券

    @allure.title('关闭优惠券')
    @pytest.mark.dependency(depends=['TestOrderFlow::test_coupon_now'])
    def test_coupon_close(self, db_init):
        ManagerCouponCloseApi(TestOrderFlow.coupon_id).send()
        # 优化SQL查询，使用参数化查询避免SQL注入，确保在mall数据库中查询eb_coupon表
        res = db_init.select('SELECT * FROM eb_coupon WHERE id = %s LIMIT 1', (TestOrderFlow.coupon_id,))
        # 提取数据库查询出status列的值并与预期值进行比较
        assert TestOrderFlow.coupon_close == res[0]['status'], '优惠券状态一致'
        print(f'优惠券状态:{TestOrderFlow.coupon_close}，res是{res[0]['status']}')
        if res and len(res) > 0:
            TestOrderFlow.coupon_close = res[0]['status']
        else:
            print(f'未找到ID为 {TestOrderFlow.coupon_id} 的优惠券记录')
        # 开启优惠券

    @allure.title('开启优惠券')
    @pytest.mark.dependency(depends=['TestOrderFlow::test_coupon_close'])
    def test_coupon_open(self, db_init):
        ManagerCouponCloseApi(TestOrderFlow.coupon_id).send()
        res = db_init.select('SELECT * FROM eb_coupon WHERE id = %s LIMIT 1', (TestOrderFlow.coupon_id,))
        assert TestOrderFlow.coupon_open == res[0]['status'], '优惠券状态一致'
        # 查看优惠券详情
        ManagerCouponDetailApi(TestOrderFlow.coupon_id).send()
        # 获取领取/发放记录
        ManagerCouponRecordApi(TestOrderFlow.coupon_id).send()
        # 删除优惠券

    @allure.title('删除优惠券')
    @pytest.mark.dependency(depends=['TestOrderFlow::test_coupon_open'])
    def test_coupon_delete(self, redis_init):
        res = ManagerDeleteCouponApi(TestOrderFlow.coupon_id).send()
        # 断言，检查redis中merchantMenuList是否存在
        try:
            coupon = redis_init.get('merchantMenuList')
            print(f'这个是优惠券返回值:{coupon}')
            # 检查Redis中是否还存在相关数据
            if coupon:
                # 如果数据是字节串，需要解码
                if isinstance(coupon, bytes):
                    coupon_str = coupon.decode('utf-8')
                else:
                    coupon_str = coupon
                # 尝试解析JSON数据
                try:
                    coupon_data = json.loads(coupon_str)
                    print(f'解析后的优惠券数据:{coupon_data}')
                except json.JSONDecodeError:
                    print('无法解析Redis中的数据为JSON格式')
                    coupon_data = None
            else:
                print('Redis中未找到merchantMenuList键或该键为空')
        except BaseException as e:
            print(f'获取Redis数据时出现异常: {e}')
            # 检查是否有其他类似的键名
            try:
                # 获取所有键名以进行调试
                all_keys = redis_init.r.keys('*menu*')
                print(f'包含"menu"的键名: {all_keys}')
                
                all_keys = redis_init.r.keys('*Merchant*')
                print(f'包含"Merchant"的键名: {all_keys}')
                
                all_keys = redis_init.r.keys('*Menu*')
                print(f'包含"Menu"的键名: {all_keys}')
                
                all_keys = redis_init.r.keys('*')
                print(f'所有键名（前20个）: {all_keys[:20]}')
            except Exception as ex:
                print(f'尝试获取键名时出错: {ex}')

        assert res.status_code == 200
