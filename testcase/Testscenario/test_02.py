# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_02.py
# @author   : 李然 
# @Time     :  16:45
# @Copyright: 焕新生活

import allure
import pytest
from api.Manager import ManagerCouponAddApi ,ProductCategoryListApi
from api.Manager.product_category_apis import ProductCategoryAddApi
from api.Merchant.product_apis import ProductSaveApi, ProductUpApi



@allure.epic('优惠券场景')
@allure.feature('优惠券模块-优惠券列表')
@allure.story('优惠券测试')
class TestProductCoupon:
    pid = '' #分类ID
    product_id = '' #商品ID
    def test_product_category_add(self,db_init):
        allure.dynamic.title('添加商品分类')
        # 添加一级分类
        api = ProductCategoryAddApi(level=1)
        resp = api.send()
        TestProductCoupon.pid = db_init.select('select id from eb_product_category where name = %s limit 1', (api.json['name'],))[0]['id']
        pytest.assume(resp.status_code == 200)
        # 添加二级分类
        api = ProductCategoryAddApi(level=2)
        api.json['pid'] = TestProductCoupon.pid  # 直接修改字典中的pid值
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        # 添加三级分类
        TestProductCoupon.pid = db_init.select('select id from eb_product_category where name = %s limit 1', (api.json['name'],))[0]['id']
        api = ProductCategoryAddApi(level=3)
        api.json['pid'] = TestProductCoupon.pid  # 直接修改字典中的pid值
        resp = api.send()
        TestProductCoupon.pid = \
        TestProductCoupon.pid = db_init.select('select id from eb_product_category where name = %s limit 1', (api.json['name'],))[0]['id']
        pytest.assume(resp.status_code == 200)

    @allure.title('添加商品')
    def test_product_add(self,db_init):
        api = ProductSaveApi()
        api.json['categoryId'] = TestProductCoupon.pid
        resp = api.send()
        TestProductCoupon.product_id = db_init.select('select id from eb_product where name = %s limit 1', (api.json['name'],))[0]['id']
        print(f"这个是商品ID：{TestProductCoupon.product_id}")
        pytest.assume(resp.status_code == 200)
        print(f"添加商品 - Response2:", resp.json())

    @allure.title('上架商品')
    def test_product_on_sale(self):
        api = ProductUpApi(product_id=TestProductCoupon.product_id)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"上架商品 - Response2:", resp.json())

    @allure.title('添加优惠券')
    def test_coupon_add(self):
        api = ManagerCouponAddApi(category=7)
        # 修改useGoods参数为1
        api.json['useGoods'] = 1
        # 追加categoryIds参数
        api.json['categoryIds'] = [TestProductCoupon.pid]
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品分类 - Response3:", resp.json())
    @allure.title('获取商品分类')
    def test_coupon_list(self):
        api = ProductCategoryListApi()
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(api.json)
        print(f"商品分类 - Response4:", resp.json())