# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Date: 2021-02-08 15:41:29
 LastEditTime: 2021-02-08 15:44:27
'''
import time
import logging
import traceback
from functools import wraps


def time_used(func):

    @wraps(func)
    def time_use(*arg, **kwargs):
        st = time.time()
        ret = func(*arg, **kwargs)
        used = time.time() - st
        logging.info("time_used: {}s, timed_func: {}".format(round(used, 6), func.__name__))
        return ret
    return time_use


def trace_comm(func):

    @wraps(func)
    def catch_err(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logging.error("gen_fea_err: {}, args:{}".format(traceback.format_exc(), [args, kwargs]))
            return None
    return catch_err
