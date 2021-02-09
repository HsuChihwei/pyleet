# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-09 19:44:29
LastEditTime: 2021-02-09 19:47:17
"""
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.83%)
# Likes:    2416
# Dislikes: 0
# Total Accepted:    542.7K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if len(s) == 1:
            return x
        res = ''
        if x < 0:
            res = '-'
            s = s[1:]
        tmp = ''
        for i in s:
            tmp = i + tmp
        if tmp[0] == '0':
            tmp = tmp[1:]
        return int(res + tmp)
# @lc code=end

