# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import logging
import logging.handlers

from paths_manager import project_path


class  GetLogger:
    # 把logger定义类属性，默认是None
    logger = None

    # 整个框架其实只需要一个对象即可，可以用单例模式实现
    @classmethod
    def get_logger(cls,worker_id='master'):
        if cls.logger is None:
            # 如果logger没有值，我才去创建这个logger对象
            # 创建日志名称apiautotest,这个值是自定义的
            cls.logger = logging.getLogger('apiautotest')
            # 日志级别，debug/info/warning/error/critical
            # 级别从左到右逐步升高
            cls.logger.setLevel(logging.DEBUG) # 设置为DEBUG，意味着比他高的级别的日志都会被记录
            # 定义日志格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s] [%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)

            # 创建日志处理器，把日志存储到文件，按照一定的规则
            tf = logging.handlers.TimedRotatingFileHandler(
                filename=f'{project_path}/logs/requests_{worker_id}.log',
                when='H',# 间隔多少时间生成新的日志文件的时间单位
                interval=1, # 间隔的时间数量
                backupCount=3, # 除了最新的日志文件外，最多可以保留3个之前的日志文件
                encoding='utf-8'
            )
            # 在处理器中添加日志格式fm
            tf.setFormatter(fm)
            # 在日志对象中添加处理器
            cls.logger.addHandler(tf)

            # 将日志输出到控制台上
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(fm)
            cls.logger.addHandler(console_handler)

        return cls.logger

if __name__ == '__main__':
    logger = GetLogger.get_logger() # 得到一个日志对象
    logger.debug('这是debug日志')
    logger.info('这是info日志')
    logger.warning('这是warning日志')
    logger.error('这是error日志')
    logger.critical('这是critical日志')