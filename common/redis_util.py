# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001.py
# @author   : 李然
# @Time     : 2025/5/25 9:53
# @Copyright: 焕新生活
import javaobj
import redis


class RedisUtil:

    def __init__(self,host,pwd=None,port=6379,decode_responses=False,db=0):
        self.pool = redis.ConnectionPool(
            host=host,
            password=pwd,
            port=port,
            decode_responses=decode_responses,
            db=db
        )
        self.r = redis.Redis(connection_pool=self.pool)

    # 封装一个统一的获取数据方法
    def get(self,key):
        # 我先得到这个key对应的redis数据类型是什么
        # 再根据类型来判断要调用哪个数据获取方法
        data_type = self.r.type(key)
        if data_type=='string' or data_type==b'string':
            return self.r.get(key)
        elif data_type=='hash' or data_type==b'hash':
            return self.r.hgetall(key)
        elif data_type=='list' or data_type==b'list':
            return self.r.lrange(key,0,-1)
        elif data_type=='set' or data_type==b'set':
            return self.r.smembers(key)
        elif data_type=='zset' or data_type==b'zset':
            return self.r.zrange(key,0,-1)
        else:
            raise BaseException(f'{key} 的数据类型不支持')
if __name__ == '__main__':
    # redis_util = RedisUtil(
    #     host='localhost',
    #     decode_responses=True
    # )
    # print(redis_util.get('userinfo10'))
    # print(redis_util.get('zset10'))
    redis_util = RedisUtil(
        host='192.168.3.163',
        port=6379,
        pwd='sinzeeaA@188',
        decode_responses=False,
        db=0
    )
    redis_util.set("liran", 123)
    value = redis_util.get("liran")
    print(f"键 liran 对应的值：{value}")
    # 立即购买数据解析
    # res = redis_util.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_59')
    # print(res)
    # # res是开发把后台源码中的java对象做了序列化后存储的数据
    # # 我们需要借助一个第三方库将他转成python对象，才好去解析
    # res_obejct = javaobj.loads(res)
    # print(res_obejct)
    # print(type(res_obejct))
    # buy_now_obejct = res_obejct[0]
    # print(buy_now_obejct)
    # # buy_now_obejct 这个对象到底有哪些属性，可以问开发
    # print(dir(buy_now_obejct)) # 得到某个对象的各个属性信息
    #
    # # 从buy_now_obejct中得到skuId和num属性
    # skuId = buy_now_obejct.skuId
    # num = buy_now_obejct.num
    # print(skuId,num)


    # 订单确认参数数据解析
    # res = redis_util.get('{CHECKOUT_PARAM_ID_PREFIX}_59')
    # # print(res)
    # # 该数据是redis里的hash类型，对应的就是python中的字典
    # # 所以我们遍历
    # for key,value in res.items():
    #     key = javaobj.loads(key)
    #     if value==b'':
    #         value = ''
    #     else:
    #         value = javaobj.loads(value)
    #     if key=='paymentType':
    #         print(dir(value))
    #         value = value.constant
    #     print(f'{key}:{value}')
