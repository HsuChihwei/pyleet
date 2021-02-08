# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-08 20:36:14
LastEditTime: 2021-02-08 20:39:07
"""

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

def two_sum(nums, target):
        for idx, i in enumerate(nums[:-1]):
            s = idx + 1
            tmp = target - i
            if tmp in nums[s:]:
                return (idx, s + nums[s:].index(tmp))
        return None

def main():
    print(two_sum([2,3,6], 8))


if __name__ == '__main__':
    main()
