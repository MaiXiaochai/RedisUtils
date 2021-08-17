# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : redis_utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/8/17 16:01
------------------------------------------
"""
from redis import Redis, ConnectionPool


class RedisUtils:
    def __init__(self, host: str, port: int = 6279, password: str = None, pool_size=None, decode_responses=True):
        """
            操作 redis的一些常用功能，连接池版

            host: redis服务器地址
            port: 端口
            password: 密码
            pool_size: 连接池大小，也就是最大连接池数
            decode_responses: 是否对返回内容进行解码，redis默认返回字节

        """
        pool = ConnectionPool(
            host=host,
            port=port,
            password=password,
            max_connections=pool_size,
            decode_responses=decode_responses
        )

        # 到这里，其实还没真正连接到 redis，现在还是个连接池的状态
        # 在真正要执行操作的时候，redis库会自己取连接、释放连接
        self.db = Redis(connection_pool=pool)

    def sadd(self, name, value):
        """
            向集合 name中添加 value
        """
        return self.db.sadd(name, value)

    def scard(self, name):
        """
            获取对应集合中元素的个数
        """
        return self.db.scard(name)

    def sismembers(self, name, value) -> bool:
        """
            判断 value是否在 name集合中
        """
        return self.db.sismember(name, value)
