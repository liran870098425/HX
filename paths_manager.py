# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活


import os
# 获取当前文件所在的目录，这个目录其实就是项目根目录
project_path = os.path.dirname(__file__)

# 再根据project来拼接数据文件绝对路径
coupon_data_xlsx = f'{project_path}/data/coupon_data.xlsx'
coupon_data_yaml = f'{project_path}/data/coupon_data.yml'
product_category_data = f'{project_path}/data/product_category_data.yml'
mtxshop_data_yaml = f'{project_path}/data/mtxshop_data.yml'
mtxshop_data_xlsx = f'{project_path}/data/mtxshop_data.xlsx'

common_yaml_path = f'{project_path}/config/common.yml'
http_yaml_path = f'{project_path}/config/http.yml'
db_yaml_path = f'{project_path}/config/db.yml'
redis_yaml_path = f'{project_path}/config/redis.yml'

file_path = f'{project_path}/data/logo.png'