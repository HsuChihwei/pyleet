# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-18 17:16:34
LastEditTime: 2021-02-18 17:36:20
"""
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.70%)
# Likes:    2163
# Dislikes: 0
# Total Accepted:    528.7K
# Total Submissions: 1.2M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([)]"
# 输出：false
# 
# 
# 示例 5：
# 
# 
# 输入：s = "{[]}"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 方案一
        # while '{}' in s or '()' in s or '[]' in s:
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('()', '')
        # return s == ''
        
        # 方案二
        # dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        # stack = ['?']
        # for c in s:
        #     if c in dic:
        #         stack.append(c)
        #     elif dic[stack.pop()] != c:
        #         return False
        # return len(stack) == 1
        
        # 官方
        # if len(s) % 2 == 1:
        #     return False
        # pairs = { ")": "(", "]": "[", "}": "{",}
        # stack = list()
        # for ch in s:
        #     if ch in pairs:
        #         if not stack or stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(ch)
        # return not stack

        # 我的
        res = []
        maps = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in '([{':
                res.append(maps.get(i)) 
            elif i in ')]}':
                if not res or i != res[-1]:
                    return False
                res.pop()
        return False if res else True
# @lc code=end

