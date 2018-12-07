#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: li
@file: time_util.py
@time: 2018/11/29 10:15 AM
"""

import time


def time_to_timestamp(time_str, style=None):
    """
    固定格式的时间转换成时间戳
    :param time_str:
    :param style:
    :return:
    """
    if style is None:
        style = "%Y-%m-%d %H:%M:%S"
    time_array = time.strptime(time_str, style)
    time_stamp = int(time.mktime(time_array))
    return time_stamp


def timestamp_to_time(time_stamp, style=None):
    """
    时间戳转换成固定格式的时间
    :param time_stamp:
    :param style:
    :return:
    """
    if style is None:
        style = "%Y-%m-%d %H:%M:%S"
    time_array = time.localtime(time_stamp)
    date_time = time.strftime(style, time_array)
    return date_time


if __name__ == '__main__':
    # now = int(time.time())
    # print now
    print time_to_timestamp("2018-12-5 21:49:7", "%Y-%m-%d %H:%M:%S")
    print timestamp_to_time(1544017747, "%Y-%m-%d %H:%M:%S")
