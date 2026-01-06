# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_coupon_case.py
# @author   : 李然 huangxinshenghuo
# @Time     :  11:44
# @Copyright: 焕新生活

# 修复PowerShell字符编码问题：Excel工作表名称在系统中显示为带空格的特殊字符

import allure
import pytest
from api.Manager.coupon_apis import ManagerCouponAddApi
from common.file_load import read_excel, write_yaml, load_yaml_file
from common.json_util import update_value_to_json
from paths_manager import mtxshop_data_xlsx, mtxshop_data_yaml, coupon_data_xlsx, coupon_data_yaml

# 首先获取Excel中所有工作表名称，然后使用正确的名称
import openpyxl
wb = openpyxl.load_workbook(mtxshop_data_xlsx)
sheet_names = wb.sheetnames
actual_sheet_name = sheet_names[0]  # 应该是实际的工作表名称

# @allure.epic('营销测试')
# @allure.feature('优惠券管理模块-优惠券列表')
# @allure.story('添加优惠券测试')
class TestCouponApi:
#     test_data = read_excel(mtxshop_data_xlsx, actual_sheet_name)
#     @allure.title('添加优惠券excel')
#     @pytest.mark.parametrize('casename,category,expect_status,extra_col1,extra_col2', test_data)
#     def test_coupon_now(self,casename,category,expect_status,extra_col1,extra_col2):
#         #添加优惠券
#         allure.dynamic.title(casename)
#         api = ManagerCouponAddApi(category=category)
#         resp = api.send()
#         # 修复pytest.assume参数数量问题
#         pytest.assume(resp.status_code == expect_status, f'期望值{expect_status}, 实际值{resp.status_code}')
#         pytest.assume(resp.json().get('code') == 200, f'期望值{200}, 实际值{resp.json().get("code")}')

    test_data = read_excel(coupon_data_xlsx, '添加优惠券接口')
    @allure.title('添加优惠券excel')
    @pytest.mark.parametrize('casename,category,expect_status', test_data)
    def test_coupon_now2(self,casename,category,expect_status):
        allure.dynamic.title(casename)
        api = ManagerCouponAddApi(category=category)
        resp = api.send()
        pytest.assume(resp.status_code==expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.json().get('code')==200,f'期望值:{200},实际值:{resp.json().get("code")}')


    test_data = load_yaml_file(coupon_data_yaml)['添加优惠券接口']
    @allure.title('添加优惠券xml')
    @pytest.mark.parametrize('casename,category,new_params,expect_status,expect_body', test_data)
    def test_coupon_now1(self,casename,category,new_params,expect_status,expect_body):
        allure.dynamic.title(casename)
        api = ManagerCouponAddApi(category=category)
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
            # 兼容原有功能
            for json_path, new_value in new_params.items():
                api.json = update_value_to_json(api.json, json_path, new_value)

        resp = api.send()

        pytest.assume(resp.status_code==expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body, f'期望值:{expect_body},实际值:{resp.text}')