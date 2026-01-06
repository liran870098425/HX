# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import pymysql


class DBUtil:

    def __init__(self,host,user,password,port=3306,database=None):
        self.connect = pymysql.Connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,  # 添加数据库名称参数
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor # 这个参数的意思是把得到的数据行当做字典
    )

    def select(self, sql, params=None):
        cursor = self.connect.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit()
        cursor.close()
        return data

    def update(self, sql, params=None):
        """
        insert/update/delete
        :param sql:
        :param params:
        :return:
        """
        cursor = self.connect.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        self.connect.commit()
        cursor.close()
    def close(self):
        if self.connect:
            self.connect.close()
if __name__ == '__main__':
    db_util = DBUtil(
        host='192.168.3.161',
        port=3306,
        user='test_mall',
        password='dev_Test_2025',
        database='mall'  # 使用mall数据库
    )
    res  = db_util.select('select * from eb_coupon where id = 21 limit 1')
    print(res)
    db_util.close()