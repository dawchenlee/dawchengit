#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:48:58 2019
题目：验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
@author: dawchen
"""
### 自己的版本
# 思路首先判断字符串是否为空，然后将字符串中的字母全变换为小写字母
# 再剔除字符串中的非字母和数字，然后通过前后两个指针从头和尾往中间
# 移动来判断其是否符合回文串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        s = s.lower()
        n = ''
        # for循环的时间复杂度为O(n),空间复杂度为O(n).
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                n += c
        i, j = 0, len(n) - 1
        # while循环的时间复杂度为O(n),空间复杂度为O(n).
        while i < j:
            if n[i] == n[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
### 解题时间复杂度为O(n),空间复杂度为O(n).
        
    
### 网上热门解法
#class Solution:
#    def isPalindrome(self, s):
#        """
#        :type s: str
#        :rtype: bool
#        """
#        s = ''.join(filter(str.isalnum,s)).lower()
#        return s==s[::-1]
"""
值得学习的地方，首先代码简短，运用filter函数来剔除非字母和数字字符串
运用列表的切片[::-1],逆序做对比。
"""