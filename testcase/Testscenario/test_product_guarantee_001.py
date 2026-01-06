# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_product_guarantee_001.py
# @author   : 李然 
# @Time     :  14:15
# @Copyright: 焕新生活
import allure
import jsonpath
from api.Manager.product_apis import ProductGuaranteeAddApi, ProductGuaranteeListApi, ProductGuaranteeUpdateApi, \
    ProductGuaranteeDeleteApi
import pytest


@allure.epic('商品')
@allure.feature('服务保障')
@allure.story('测试服务保障')
class TestProductGuarantee:
    gurantee_id =  ''
    @allure.title('增加商品服务保障')
    @pytest.mark.dependency(name = 'test_product_guarantee_add')
    def test_product_guarantee_add(self,db_init):
        api = ProductGuaranteeAddApi()
        gurantee_name = jsonpath.jsonpath(api.json, '$.name')[0]
        print(f'这个是商品服务保障名字：{gurantee_name}')
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品服务保障 - Response:", resp.json())
        # 等待数据同步到数据库
        import time
        time.sleep(1)
        guarantee_result = db_init.select('select id from eb_product_guarantee where name = %s limit 1', (gurantee_name,))
        TestProductGuarantee.gurantee_id  = guarantee_result[0]['id']
        print(f"商品服务保障id是:{TestProductGuarantee.gurantee_id}")

    @allure.title('查询商品服务保障')
    def test_product_guarantee_list(self,db_init):
        api = ProductGuaranteeListApi()
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品服务保障 - Response:", resp.json())
    @allure.title('跟新商品服务保障')
    @pytest.mark.dependency(depends=['test_product_guarantee_add'])
    def test_product_guarantee_update(self,db_init):
        api = ProductGuaranteeUpdateApi(guarantee_id= TestProductGuarantee.gurantee_id)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品服务保障 - Response:", resp.json())
    @allure.title('删除商品服务保障')
    @pytest.mark.dependency(depends=['test_product_guarantee_add'])
    def test_product_guarantee_delete(self,db_init):
        api = ProductGuaranteeDeleteApi(guarantee_id= TestProductGuarantee.gurantee_id)
        resp = api.send()
        pytest.assume(resp.status_code == 200)
        print(f"商品服务保障 - Response:", resp.json())
