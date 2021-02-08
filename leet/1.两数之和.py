# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-08 20:45:34
LastEditTime: 2021-02-08 20:45:34
"""
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (49.65%)
# Likes:    9888
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 3.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums[:-1]):
            s = idx + 1
            tmp = target - i
            if tmp in nums[s:]:
                return (idx, s + nums[s:].index(tmp))
        return None
# @lc code=end

