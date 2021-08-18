# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : demo.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/8/17 17:11
------------------------------------------
"""
from os import getenv

from redis_utils import RedisUtils

redis_cfg = {
    'host': getenv("REDIS_HOST"),
    'port': 6379,
    'password': getenv("REDIS_PASSWORD"),
}


def main():
    set_name = 'demo'
    values = ['maixiaochai', 'hello']

    db = RedisUtils(**redis_cfg)

    # for value in values:
    #     db.sadd(set_name, value)

    total = db.scard(set_name)

    print(total)  # 2
    print(type(total))  # int


if __name__ == '__main__':
    main()
