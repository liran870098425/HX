# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_02.py
# @author   : 李然 
# @Time     :  16:45
# @Copyright: 焕新生活

import allure
import pytest
from api.Manager import ManagerCouponAddApi ,ProductCategoryListApi
from api.Manager.product_apis import MerchantPortAttributeAddApi, MerchantPortAttributeListApi
from api.Manager.product_category_apis import ProductCategoryAddApi
from api.Merchant.brand_apis import BrandAddApi
from api.Merchant.product_apis import ProductSaveApi, ProductUpApi
from common.json_util import extract_json


@allure.epic('优惠券场景')
@allure.feature('优惠券模块-优惠券列表')
@allure.story('优惠券测试')
class TestProductCoupon:
    pid = '' #分类ID
    product_id = '' #商品ID
    main_attr = '' # 重要属性ID
    second_attr = '' # 次要属性ID
    @allure.title('添加商品分类')
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
        TestProductCoupon.pid = db_init.select('select id from eb_product_category where name = %s limit 1', (api.json['name'],))[0]['id']
        pytest.assume(resp.status_code == 200)

    @allure.title('添加品牌')
    def test_product_brand_add(self,db_init):
        api = BrandAddApi()
        # 修复参数设置，使用正确的键名
        api.json['categoryIds'] = TestProductCoupon.pid
        api.json['categoryIdData'] = [TestProductCoupon.pid]
        resp = api.send()
        # 检查响应状态码和内容类型，避免JSONDecodeError
        pytest.assume(resp.status_code == 200)
        # 检查响应内容是否为空
        if resp.text.strip():
            print(f"添加品牌 - Response:", resp.json())
        else:
            print(f"添加品牌 - Response: 空响应")
            pytest.assume(False, "API返回空响应")
    @allure.title('添加商品属性')
    def test_product_attr_add(self, db_init):
        api = MerchantPortAttributeAddApi(categoryId=TestProductCoupon.pid)
        api.json['categoryId'] = TestProductCoupon.pid
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"添加商品属性 - Response:", resp.json())

    @allure.title('商品属性列表')
    def test_product_attr_list(self):
        api = MerchantPortAttributeListApi(categoryId=TestProductCoupon.pid)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品属性列表 - Response:", resp.json())
        
        # 解析响应数据，区分主要属性和次要属性
        resp_data = resp.json()
        if 'data' in resp_data and resp_data['data']:
            attributes = resp_data['data']
            
            # 分别提取主要属性（levelType=1）和次要属性（levelType=2）
            main_attrs = [attr for attr in attributes if attr.get('levelType') == 1]
            second_attrs = [attr for attr in attributes if attr.get('levelType') == 2]
            
            # 获取第一个主要属性ID，如果存在
            if main_attrs:
                TestProductCoupon.main_attr = main_attrs[0]['id']
                print(f"重要的属性ID：{TestProductCoupon.main_attr}")
            else:
                print("未找到主要属性")
                TestProductCoupon.main_attr = None
            
            # 获取第一个次要属性ID，如果存在
            if second_attrs:
                TestProductCoupon.second_attr = second_attrs[0]['id']
                print(f"次要属性ID：{TestProductCoupon.second_attr}")
            else:
                print("未找到次要属性")
                TestProductCoupon.second_attr = None
        else:
            print("商品属性列表为空")
            TestProductCoupon.main_attr = None
            TestProductCoupon.second_attr = None

    @allure.title('添加商品')
    def test_product_add(self, db_init):
        # 使用所有主要属性ID和次要属性ID
        api = ProductSaveApi(main_attrId=TestProductCoupon.main_attr, second_attrId=TestProductCoupon.second_attr)
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
