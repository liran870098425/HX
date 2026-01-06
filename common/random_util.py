# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import datetime
import time
import random
from faker import Faker
fake = Faker(locale='zh_CN')

# 随机生成一个手机号
def rdm_phone_number():
    return fake.phone_number()

# 随机生成当前日期时间
def cur_date_time(): # 2025-05-25 16:13:46
    return fake.date_time_between_dates()

# 随机生成日期，指定日期格式
def rdm_date(pattern='%Y-%m-%d'):
    return fake.date(pattern=pattern)

# 生成当前时间戳
def cur_timestamp(level='s'):
    if level=='s':
        return int(time.time()) # 10位时间戳，精确到秒
    elif level=='ms':
        return int(time.time()*1000) # 13位时间戳，精确到毫秒
    else:
        raise Exception(f'{level}不支持')

# 生成一个指定时间段的时间戳
def gen_timestamp(start_date='+0d',end_date='+1d'):
    date_time = fake.date_time_between(start_date,end_date)
    print(date_time)
    return int(time.mktime(date_time.timetuple()))

# 计算两个时间戳间隔多少天
def get_days_difference(timestamp1,timestamp2):
    # 转成datetime对象
    date1 = datetime.datetime.fromtimestamp(timestamp1)
    date2 = datetime.datetime.fromtimestamp(timestamp2)
    # 计算差值
    diff = date2-date1
    # 提取差值部分
    days = diff.days
    return abs(days)

# 生成当前日期+2天的日期
def rdm_date_plus_2days(pattern='%Y-%m-%d'):
    """
    生成当前日期+2天的日期
    :param pattern: 日期格式，默认为 '%Y-%m-%d'
    :return: 格式化后的日期字符串
    """
    return fake.date_between(start_date='+2d', end_date='+2d').strftime(pattern)
# 新增一个函数，生成一个五位的随机数
def rdm_five_digit():
    """
    生成一个五位的随机数
    :return: 五位随机数
    """
    five_digit_num = random.randint(10000, 99999)
    return five_digit_num



if __name__ == '__main__':
    print(rdm_phone_number())
    print(cur_date_time())
    print(rdm_date('%Y/%m/%d'))
    print(f'这个是当前时间：{cur_timestamp()}')
    print(gen_timestamp(start_date='-30d', end_date='-10d'))
    print(rdm_date_plus_2days())  # 测试新增的函数
    print(rdm_date_plus_2days('%Y-%m-%d %H:%M:%S'))  # 测试带时间格式的函数