#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:17:10 2019
题目：有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

@author: dawchen
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 运用栈的特征来解决问题。时间复杂度O(n)空间复杂度O(n)
        dic = {'{': '}',  '[': ']', '(': ')'}
        if s and s[0] not in dic: return False
        stack = []
        for c in s:
            if not stack or c in dic: stack.append(c)
            elif stack[-1] in dic and dic[stack[-1]] == c: stack.pop()
            else: return False  
        return not stack
