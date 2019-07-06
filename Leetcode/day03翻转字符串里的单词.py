#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 17:10:47 2019
题目：翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"
示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

@author: dawchen
"""
### 自己的解法
class Solution:
    ### 本题的时间复杂的为O(n),空间复杂度为O(n).
    def reverseWords(self, s: str) -> str:
        # 将字符串分割为列表，并倒序拷贝给l，空间复杂度为O(n)
        l = s.split(' ')[::-1]
        c = ''
        # 循环处时间复杂度为O(n)
        for i in l:
            # 注意这里如果开头和结尾有所选定分割符会传入相同数目的''（空字符）
            # 而字符串中间出现的分割符则会传入分割符数目减1数目的''（空字符）
            if i == '':
                pass
            else:
                c += i +' '
        return c[:-1]
    
    
### 网友的另一种解法
'''
先处理字符串，将首尾空格都删除；
倒序遍历字符串，当第一次遇到空格时，添加s[i + 1: j]（即添加一个完整单词）；
然后，将直至下一个单词中间的空格跳过，并记录下一个单词尾部j；
继续遍历，直至下一次遇到第一个空格，回到1.步骤；
由于首部没有空格，因此最后需要将第一个单词加入，再return。
python可一行实现。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i + 1: j] + ' '
                while s[i] == ' ': i -= 1
                j = i + 1
            i -= 1
        return res + s[:j]

