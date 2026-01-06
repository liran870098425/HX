# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import jsonpath
from jsonpath_ng import parse, Index, Fields

from common.logger import GetLogger


def update_value_to_json(json_object, json_path=None, new_value=None, add_new=None):
    """

    :param json_object:
    :param json_path: 要更新的路径
    :param new_value: 目标参数对应的测试数据，如果new_value等于$del则代表要删除目标字段
    :param add_new: 要追加的新参数和值的字典，例如 {"new_field": "new_value"}
    :return:
    """
    # 如果add_new参数不为空，则添加新的键值对
    if add_new and isinstance(add_new, dict):
        for key, value in add_new.items():
            json_object[key] = value
        return json_object

    # 原有的更新功能
    if json_path is not None:
        jsonpath_expr = parse(json_path) # 把传进来的json_path表达式转成jsonpath表达式对象

        matches = jsonpath_expr.find(json_object) #通过jsonpath去匹配目录
        for match in matches:
            path = match.path # 获取当前匹配结果的路径
            if isinstance(path, Index): #判断他是不是一个索引对象路径
                if new_value == '$del':
                    del match.context.value[match.path.index]
                else:
                    match.context.value[match.path.index] = new_value
            elif isinstance(path, Fields): #判断他是不是一个字段对象路径
                if new_value == '$del':
                    del match.context.value[match.path.fields[0]]
                else:
                    match.context.value[match.path.fields[0]] = new_value
    return json_object


def extract_json(json_object,json_path,index=0):
    logger = GetLogger.get_logger()
    res = jsonpath.jsonpath(json_object,json_path)

    # res如果提取到了，那么值就是一个有数据的列表，如果没匹配到他的值就是Fasle
    if res:
        logger.info(f'通过{json_path}匹配到的结果是:{res}')
        if index<0:
            # 如果index小于0，则认为你想要所有的匹配结果
            return res
        else:
            # 如果不小于0，那么你传几，就嗲表你要的是匹配结果的某一个
            return res[index]
    else:
        logger.exception(f'通过{json_path}没有匹配到结果')

if __name__ == '__main__':
    json_object = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "",
            "goods_name": "沙陌炒锅20250323班",
            "sn": "sn00001",
            "price": "300",
            "mktprice": "298",
            "cost": "10",
            "weight": "1",
            "goods_gallery_list": [
                {
                    "img_id": -1,
                    "original": "http://59.36.173.55:7000/statics/attachment/goods/2025/5/25/9/34212733.png",
                    "sort": 0
                }
            ],
            "quantity": 99999999,
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "market_enable": 1,
            "template_id": 0,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "shop_cat_id": 0,
            "meta_description": "",
            "meta_keywords": "",
            "page_title": "",
            "goods_params_list": [],
            "sku_list": [],
            "intro": "<p>这是说明</p>"
        }

    # 测试原有功能
    json_object = update_value_to_json(json_object,'$.goods_name','')
    print(json_object)
    json_object = update_value_to_json(json_object,'$.goods_gallery_list[0].sort',1)
    print(json_object)

    # 测试新增的追加功能
    json_object = update_value_to_json(json_object, add_new={"new_field": "new_value", "another_field": "another_value"})
    print(json_object)