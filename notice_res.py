# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import sys

import jsonpath
import requests

from common.file_load import load_yaml_file


class JenkinsStatus:

    def send(self,build_url):
        url = f'{build_url}/api/json'
        method = 'get'
        resp = requests.request(method=method,url=url)
        return resp

class FeiShuNotice:

    def send(self,job_name,build_number,result,user,build_url):
        self.res = load_yaml_file('result.yml')
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/8efc5287-babb-476b-9158-d1d061e99744'
        method = 'post'
        json = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": f"{job_name}第{build_number}次测试完成",
                        "content": [
                            [{
                                "tag": "text",
                                "text": f"状态:{result}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"用例总数:{self.res['total']}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"成功:{self.res['passed']}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"失败:{self.res['failed']}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"跳过:{self.res['skipped']}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"错误:{self.res['error']}"
                            }],
                            [{
                                "tag": "text",
                                "text": f"执行人:{user}"
                            }],
                            [{
                                "tag": "a",
                                "text": f"查看报告",
                                "href":f"{build_url}/allure"
                            }],
                        ]
                    }
                }
            }
        }
        resp = requests.request(method=method,url=url,json=json)
        return resp
class DingDingNotice:
    def send(self,job_name,build_number,result,user,build_url):
        self.res = load_yaml_file('result.yml')
        url = 'https://oapi.dingtalk.com/robot/send?access_token=eda69535b902dfc3f009aba101c407cf11e1e68e758b194d4a232f42f1ad1aca'
        method = 'post'
        json = {
            "msgtype": "markdown",
            "markdown": {
                "title":f"### {job_name}测试完成",
                "text": f"### {job_name}测试完成 \n - 任务：第{build_number}次\n - 状态：{result} \n - 用例总数: {self.res['total']} \n - 成功: {self.res['passed']} \n - 失败: {self.res['failed']} \n - 错误: {self.res['error']} \n - 跳过: {self.res['skipped']} \n - 执行人: {user}  \n[查看报告]({build_url}/allure) "
            }
        }
        resp = requests.request(method=method,
                         url=url,
                         json = json)
        return resp

class WxNotice:

    def send(self,job_name,build_number,result,user,build_url):
        res = load_yaml_file('result.yml')
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=28c595dc-f030-43d6-bef4-e3280a7568de'
        method = 'post'
        json = {
            "msgtype": "markdown",
            "markdown": {
                "content": f"#### {job_name}测试完成 \n"
                           f"- 任务:第{build_number}次 \n"
                           f"- 状态:{result} \n"
                           f"- 用例总数:{res['total']} \n"
                           f"- 成功:{res['passed']} \n"
                           f"- 失败:{res['failed']} \n"
                           f"- 错误:{res['error']} \n"
                           f"- 跳过:{res['skipped']} \n"
                           f"- 执行人:{user} \n"
                           f"- [查看报告]({build_url}/allure)"
            }
        }
        resp = requests.request(method=method,url=url,json=json)
        return resp
if __name__ == '__main__':
    # build_url = 'http://192.168.1.188:8080/job/apiframework20250615/1'
    args = sys.argv
    build_url = args[1]
    notice_type = args[2]
    resp = JenkinsStatus().send(build_url)
    print(resp.text)
    # 提取执行人
    user = jsonpath.jsonpath(resp.json(),'$..shortDescription')[0]
    print(user)

    # 提取执行结果
    result = jsonpath.jsonpath(resp.json(),'$..result')[0]
    print(result)

    # 提取任务名称和执行次数
    fullDisplayName = jsonpath.jsonpath(resp.json(),'$..fullDisplayName')[0]
    # apiframework20250615 #1
    job_name = fullDisplayName.split('#')[0].strip()
    print(job_name)
    build_number = fullDisplayName.split('#')[1]
    print(build_number)
    if notice_type=='wx':
        WxNotice().send(job_name,build_number,result,user,build_url)
    elif notice_type=='feishu':
        FeiShuNotice().send(job_name,build_number,result,user,build_url)
    elif notice_type=='dd':
        DingDingNotice().send(job_name,build_number,result,user,build_url)