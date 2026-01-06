# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import mimetypes
import os

import requests

from common.logger import GetLogger


class RequestsClient:
    session = requests.session()
    def __init__(self):
        self.url = None
        self.method =None
        self.headers =None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self):
        # 发起之前记录接口请求信息
        GetLogger.get_logger().debug(f'======================================================')
        GetLogger.get_logger().debug(f'接口url:{self.url}')
        GetLogger.get_logger().debug(f'接口method:{self.method}')
        GetLogger.get_logger().debug(f'接口headers:{self.headers}')
        GetLogger.get_logger().debug(f'接口params:{self.params}')
        GetLogger.get_logger().debug(f'接口data:{self.data}')
        GetLogger.get_logger().debug(f'接口json:{self.json}')
        GetLogger.get_logger().debug(f'接口files:{self.files}')
        if self.files:
            # 由于不知道文件路径那个参数到底叫什么，所以我们需要遍历files字典中的每个key,value
            # 判断这个value的值是否一个存在的路径，如果是我们就处理
            for key,value in self.files.items():
                if isinstance(value,str) and os.path.exists(value):
                    # 说明对应的key，value就是目标文件参数
                    filename = os.path.basename(value)
                    file_type = mimetypes.guess_type(filename)[0]
                    self.files[key] = (filename,open(file=value,mode='rb'),file_type)

        try:
            self.resp = RequestsClient.session.request(
                method=self.method,
                url = self.url,
                headers = self.headers,
                data = self.data,
                params = self.params,
                json = self.json,
                files = self.files,
               # verify=False # 该参数表示忽略https的证书校验
            )
            GetLogger.get_logger().debug(f'接口响应状态码:{self.resp.status_code}')
            GetLogger.get_logger().debug(f'接口响应body:{self.resp.text}')
        except BaseException as e:
            GetLogger.get_logger().exception('接口发起失败')
            raise BaseException(f'接口发起失败:{e}')
        return self.resp