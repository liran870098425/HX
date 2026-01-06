# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_product_category_001.py
# @author   : 李然 
# @Time     :  11:12
# @Copyright: 焕新生活
import allure
import jsonpath
import pytest
from api.Manager.product_category_apis import ProductCategoryAddApi, ProductCategoryListApi, ProductCategoryDeleteApi

@allure.epic('商品')
@allure.feature('商品分类模块-分类列表')
@allure.story('商品分类测试')
class TestProductCategoryApi:
    product_name = '' # 商品分类名称
    product_id = ''# 商品分类ID
    @allure.title('添加商品分类')
    @pytest.mark.dependency(name='test_product_category_add')
    def test_product_category_add(self):
        allure.dynamic.title('添加商品分类')
        api = ProductCategoryAddApi(level=1)
        # 从请求体中获取将要创建的分类名称
        result = jsonpath.jsonpath(api.json, '$.name')
        print(f"商品分类名称是:{result}")
        if result:
            TestProductCategoryApi.product_name = result[0]
        else:
            TestProductCategoryApi.product_name = '新增分类'
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"添加商品分类 - Response:", resp.json())

    @allure.title('获取商品分类列表')
    @pytest.mark.dependency(depends=["test_product_category_add"])
    def test_product_category_list(self, db_init):
        api = ProductCategoryListApi()
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        category_result = db_init.select('SELECT * FROM eb_product_category WHERE name = %s LIMIT 1', (TestProductCategoryApi.product_name,))
        if category_result:
            TestProductCategoryApi.product_id = category_result[0]['id']
            print(f"商品分类id是:{TestProductCategoryApi.product_id}")
        else:
            print(f"警告: 未能在数据库中找到名为 {TestProductCategoryApi.product_name} 的分类")
            pytest.fail(f"未能获取到新增的分类ID: {TestProductCategoryApi.product_name}")
        print(f"获取商品分类列表 - Response:", resp.json())
    @allure.title('删除商品分类')
    @pytest.mark.dependency(depends=["test_product_category_add"])
    def test_product_category_delete(self, db_init):
        api = ProductCategoryDeleteApi(TestProductCategoryApi.product_id)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"删除成功- Response:", resp.json())