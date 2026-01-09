# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_02.py
# @author   : 李然 
# @Time     :  16:45
# @Copyright: 焕新生活
import time

import allure
import pytest
from api.Manager import ManagerCouponAddApi, ProductCategoryListApi, ManagerDeleteCouponApi
from api.Manager.product_apis import MerchantPortAttributeAddApi, MerchantPortAttributeListApi, ProductTagSaveApi, \
    ProductBrandListApi, ProductBrandAddApi, ProductBrandDeleteApi
from api.Manager.product_category_apis import ProductCategoryAddApi, ProductCategoryDeleteApi
from api.Merchant.brand_apis import BrandAddApi
from api.Merchant.product_apis import ProductSaveApi, ProductUpApi, ProductDeleteApi
from api.Merchant.supplier_apis import SupplierAddAccountApi, SupplierAccountListApi, SupplierBrandAddApi
from common.assert_utils import AssertUtils
from common.json_util import extract_json
import jsonpath
import json

@allure.epic('优惠券场景')
@allure.feature('优惠券模块-优惠券列表')
@allure.story('优惠券测试')
class TestProductCoupon:
    pid = '' #分类
    product_id = '' #商品ID
    main_attr = '' # 重要属性ID
    second_attr = '' # 次要属性ID
    supplier_id = ''  #供应商ID
    categoryIds =  '' # 品牌ID
    supplier_name =  '' # 供应商名称
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

    @allure.title('商户添加品牌')
    def test_product_brand_add(self,db_init):
        api = BrandAddApi()
        # 修复参数设置，使用正确的键名
        api.json['categoryIds'] = TestProductCoupon.pid
        api.json['categoryIdData'] = [TestProductCoupon.pid]
        # TestProductCoupon.brand_name = extract_json(api.json,'name')
        resp = api.send()
        # 检查响应状态码和内容类型，避免JSONDecodeError
        pytest.assume(resp.status_code == 200)
        # 检查响应内容是否为空
        if resp.text.strip():
            print(f"添加品牌 - Response:", resp.json())
        else:
            print(f"添加品牌 - Response: 空响应")
            pytest.assume(False, "API返回空响应")
    @allure.title('平台添加品牌')
    def test_product_brand_add_platform(self,db_init):
        api = ProductBrandAddApi(category_id_data = TestProductCoupon.pid)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        TestProductCoupon.brand_name = extract_json(api.json, 'name')
        print(f'品牌名称：{TestProductCoupon.brand_name}')
        print(f"获取平台品牌 - Response:", resp.json())
    @allure.title('获取品牌列表')
    def test_product_brand_list(self):
        api = ProductBrandListApi(name= TestProductCoupon.brand_name)
        resp = api.send()
        TestProductCoupon.categoryIds = extract_json(resp.json(),'$.data.list[0].id')
        print(f'品牌ID：{TestProductCoupon.categoryIds}')
        pytest.assume(resp.status_code == 200)
        print(f"获取品牌 - Response:", resp.json())

    @allure.title('添加商品标签')
    def test_product_tag_add(self, db_init):
        api = ProductTagSaveApi(play_products = TestProductCoupon.pid)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"添加商品标签 - Response:", resp.json())
    @allure.title('添加供应商')
    def test_product_supplier_add(self, db_init):
        api = SupplierAddAccountApi()
        TestProductCoupon.supplier_name = extract_json(api.json, 'supplierName')
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"添加供应商 - Response:", resp.json())
    @allure.title('获取供应商品列表')
    def test_product_supplier_list(self):
        api = SupplierAccountListApi(keyword = TestProductCoupon.supplier_name)
        resp = api.send()
        TestProductCoupon.supplier_id = extract_json(resp.json(), 'data.list[0].supplierId')
        pytest.assume(resp.status_code == 200)
        print(f"获取供应商品列表 - Response:", resp.json())
    @allure.title('添加品牌-供应商')
    def test_product_brand_supplier_add(self):
        api = SupplierBrandAddApi(supplier_id=TestProductCoupon.supplier_id, brand_id = TestProductCoupon.categoryIds)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"添加品牌-供应商 - Response:", resp.json())
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
        api.json['brandId']  = TestProductCoupon.categoryIds
        api.json['supplierId'] = TestProductCoupon.supplier_id
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
    def test_coupon_add(self, db_init):
        api = ManagerCouponAddApi(category=7)
        # 修改useGoods参数为1
        api.json['useGoods'] = 1
        # 追加categoryIds参数
        api.json['categoryIds'] = [TestProductCoupon.pid]
        api.json['receiveType'] = 2
        resp = api.send()
        TestProductCoupon.coupon_id = db_init.select('select id from eb_coupon where name = %s limit 1', (api.json['name'],))[0]['id']
        pytest.assume(resp.status_code == 200)
        print(f"优惠券ID:{TestProductCoupon.coupon_id}")
        print(f"商品分类 - Response3:", resp.json())

    @allure.title('删除优惠券')
    def test_coupon_delete(self, redis_init):
        res = ManagerDeleteCouponApi(TestProductCoupon.coupon_id).send()
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
    @allure.title('删除商品')
    def test_product_delete(self, redis_init):
        res = ProductDeleteApi(product_id=TestProductCoupon.product_id).send()
        # 断言，检查redis中merchantMenuList是否存在
        pytest.assume(res.status_code == 200)
        print(f"删除商品 - Response4:", res.json())

    @allure.title('删除品牌')
    def test_brand_delete(self, redis_init):
        res = ProductBrandDeleteApi(brand_id=TestProductCoupon.categoryIds).send()
        # 断言，检查redis中merchantMenuList是否存在
        time.sleep(5)
        pytest.assume(res.status_code == 200)
        print(f"删除品牌 - Response6:", res.json())
    @allure.title('删除商品分类')
    def test_product_category_delete(self, redis_init):
        res = ProductCategoryDeleteApi(categoryid = TestProductCoupon.pid).send()
        # 断言，检查redis中merchantMenuList是否存在
        pytest.assume(res.status_code == 200)
        pytest.assume(res.json())
        AssertUtils.assert_status_code(actual_code = res.status_code, expected_code =200,case_desc = '删除商品分类接口，状态码断言200')
        AssertUtils.assert_response_field(resp_json = res.json(), required_fields = ['code', 'message', 'data'], case_desc = '删除商品分类接口，接口相应核心字段断言')
        AssertUtils.assert_value_equal(actual = res.json()['code'], expected = 6202, check_desc = '删除商品分类接口，code断言')
        AssertUtils.assert_value_in(actual=res.json()['message'], container = '有品牌关联该分类，无法删除' , check_desc = '删除商品分类接口，message断言')
        print(f"删除商品分类 - Response5:", res.json())


