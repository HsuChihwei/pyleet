# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-08 17:46:47
LastEditTime: 2021-02-08 17:51:16
"""

from random import randint

from utils.decorate import time_used


@time_used
def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


if __name__ == "__main__":
    alist = [randint(0, 10000) for _ in range(10000)]
    bubble_sort(alist)
    print(alist)
