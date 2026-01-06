# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_productcategory_case.py
# @author   : 李然 
# @Time     :  17:25
# @Copyright: 焕新生活
import allure
import jsonpath
import pytest

from api.Manager.product_category_apis import ProductCategoryAddApi
from common.file_load import load_yaml_file
from common.json_util import update_value_to_json
from paths_manager import product_category_data


class TestProductCategoryApi:

    test_data = load_yaml_file(product_category_data)['添加商品分类接口']
    
    @allure.epic('商品分类管理')
    @allure.feature('商品分类模块-分类列表')
    @allure.story('添加商品分类测试')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,level,new_params,expect_status', test_data)
    def test_product_category_add(self, casename, level, new_params, expect_status):
        allure.dynamic.title(casename)
        api = ProductCategoryAddApi(level=level)  # 使用默认值或从配置中获取值
        # 检查是否包含add_new参数
        if 'add_new' in new_params:
            # 使用新增功能
            add_new_data = new_params['add_new']
            api.json = update_value_to_json(api.json, add_new=add_new_data)
            
            # 处理其他更新参数（如果存在）
            for json_path, new_value in new_params.items():
                if json_path != 'add_new':
                    api.json = update_value_to_json(api.json, json_path, new_value)
        else:
            # 兼容原有功能，遍历new_params字典进行更新
            for json_path, new_value in new_params.items():
                api.json = update_value_to_json(api.json, json_path, new_value)
        
        res = api.send()
        pytest.assume(res.status_code == expect_status)
        print(f"{casename} - Response:", res.json())