#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:12:33 2019
题目：字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
@author: dawchen
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 时间复杂度O(n)，空间复杂度O(n)
        # 创建哈希表记录s中字母出现的次数
        dic = {}
        for c in s:
            dic[c] = dic.get(c,0) + 1
        
        # 找到索引
        index = 0
        for ch in s:
            if dic[ch] == 1:
                return index
            else:
                index += 1       
        return -1
