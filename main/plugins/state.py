#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import redis


def set_user_state(openid, state):
    """设置用户状态"""
    redis.hset('wechat:user:' + openid, 'state', state)
    return None


def get_user_state(openid):
    """获取用户状态"""
    return redis.hget('wechat:user:' + openid, 'state')