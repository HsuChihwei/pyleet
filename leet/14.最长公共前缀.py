# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-18 16:10:37
LastEditTime: 2021-02-18 17:01:10
"""
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (39.20%)
# Likes:    1460
# Dislikes: 0
# Total Accepted:    447.6K
# Total Submissions: 1.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 方案一
        # if strs == []:
        #     return ""
        # min_len = min([len(x) for x in strs])
        # pub = ""
        # for x in range(min_len):
        #     letter = strs[0][x]
        #     IsSame = True
        #     for t in strs:
        #         if t[x] != letter:
        #             IsSame = False
        #             break
        #     if IsSame == False:
        #         return pub
        #     else:
        #         pub += letter
        # return pub

        # 方案二
        # s = ""
        # for i in zip(*strs):
        #     if len(set(i)) == 1:
        #         s += i[0]
        #     else:
        #         break
        # return s

        # 方案三
        # if not strs:
        #     return ""
        # s1 = min(strs)  # ascII是和字符对应的，从前往后按位比较，当前面的几位字符相等时当前位要是大于或小于那就不用往后比了
        # s2 = max(strs)
        # for i, c in enumerate(s1):
        #     if c != s2[i]:
        #         return "" if i == 0 else s1[:i]
        # return s1
        
        # 我的
        res = ""
        if not strs:
            return res
        if len(strs)== 1:
            return strs[0]
        res = strs[0]
        for now in strs[1:]:
            tmp = ""
            lens = len(now)
            for i in range(len(res)):
                if i >= lens or res[i] != now[i]:
                    break
                tmp += res[i]
            res = tmp
            if not res:
                break
        return res

# @lc code=end

