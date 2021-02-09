# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-09 19:44:29
LastEditTime: 2021-02-09 21:05:12
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
        # 参考一
        # INTMAX10 = 214748364
        # INTMIN10 = -214748364
        # ans = 0
        # while x:
        #     pop = x % 10 if x > 0 else x % -10
        #     x = x // 10 if x > 0 else int(x / 10)
        #     if ans > INTMAX10 or (ans == INTMAX10 and pop > 7):
        #         return 0
        #     if ans < INTMIN10 or (ans == INTMIN10 and pop < -8):
        #         return 0
        #     ans = ans * 10 + pop
        # return ans

        # 参考二
        # a = str(x) if x > 0 else str(-x) + '-'
        # a = int(a[::-1])
        # return a if -2**31 < a < 2**31 - 1 else 0

        # 参考三
        # strinf = str(x)
        # if x >= 0:
        #     reverse_str = strinf[::-1]
        # else:
        #     reverse_str = '-%s' % strinf[:0:-1]
        # rev_int = int(reverse_str)
        # if (rev_int < - 2 ** 31) or (rev_int > 2 ** 31 - 1):
        #     rev_int = 0
        # return rev_int

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
        # if tmp[0] == '0':
        #     tmp = tmp[1:]
        res = int(res + tmp)
        if (res > 2**31 - 1) or (res < -2**31):
            return 0
        return res
# @lc code=end
