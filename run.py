# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : run.py
# @author   : 李然
# @Time     : 2025/5/18 10:30
# @Copyright: 焕新生活

import os
import sys

import pytest

from api.Manager.login_apis import ManagerLoginApi
from common.file_load import load_yaml_file, write_yaml
from paths_manager import common_yaml_path, http_yaml_path, db_yaml_path, redis_yaml_path

if __name__ == '__main__':
    # args = sys.argv
    # print(args) # ['run.py', 'sit']
    # #
    #
    #
    # ，是为了兼容不传递环境名称时，默认执行test环境
    # env_name = args[1]
    # env_file = f'config/env_{env_name}.yml'
    # if len(args)>1:
    #     env_name = args[1]
    #     env_file = f'config/env_{env_name}.yml'
    #     del args[1]
    # # 读取环境配置文件所有信息
    # env_info = load_yaml_file(env_file)
    # print(env_info)
    # # 依次写入到各个基础配置文件中去
    # write_yaml(common_yaml_path,env_info['common'])
    # write_yaml(http_yaml_path, env_info['http'])
    # write_yaml(db_yaml_path, env_info['db'])
    # write_yaml(redis_yaml_path, env_info['redis'])

    # 执行pytest测试并生成Allure原始数据
    # 使用report/data作为Allure结果目录，保持与pytest.ini配置一致
    pytest.main(['--alluredir=report/data', '--clean-alluredir'])

    # 生成HTML报告 - 使用项目中的Allure路径并临时清除JAVA_HOME环境变量
    import subprocess
    env = os.environ.copy()
    # 清除JAVA_HOME环境变量以避免Java环境冲突，如果需要可设置为项目内的JRE
    if 'JAVA_HOME' in env:
        env.pop('JAVA_HOME', None)
    allure_cmd = os.path.join('allure', 'allure-2.24.0', 'bin', 'allure.bat')  # 使用相对路径更安全
    subprocess.run([allure_cmd, 'generate', 'report/data', '-o', 'report/html', '--clean'], env=env)

    # 打开报告
    subprocess.run([allure_cmd, 'open', 'report/html'], env=env)
