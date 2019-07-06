#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 17:34:19 2019
题目：最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
@author: dawchen
"""
### 自己的解法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ### 本题时间复杂度为O(mn)空间复杂度为O(m)
        if strs == []:
            return ''
        s = strs[0]
        c = ''
        # 此循环时间复杂度为O(m)
        for i in range(0,len(s)):
            # 遍历列表中的每个单词与第一个单词s，按索引i进行对比
            # 时间复杂度为O(n)空间复杂度为O(m)
            for string in strs:
                if len(string) <= i:
                    return c
                if s[i] == string[i]:
                    pass
                else:
                    return c
            c += s[i]
        return c


### 网上解法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''
    
'''
利用好 zip 和 set
【第一行】每次都取各个字符串的同一列字符，放进 set，set 中不会储存重复元素，所以长度为1代表各个字符都是相同的，此时 == 会让它变成 True
【第二行】index 搜索第一个 0 的位置，0 与 False 在值上是等价的，相当于搜索第一个 False 的位置也就是公共前缀的长度
细节补充
zip(*str) 将 str 中所有字符串并列到迭代器中，逐次并列返回 str 中所有字符串的第 1、2、3、…… 个字符
第一行代码末尾添加了一个 [0] 是为了防止 index 函数搜索不到 0 时报错
'''

### 多种解法
'''
思路：
思路 1：
Python 特性，取每一个单词的同一位置的字母，看是否相同。

思路 2：
取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词

思路 3：
按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。

代码:
思路一：
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
思路二：
PythonJava
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res
思路三：
PythonJava
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
‘’‘
