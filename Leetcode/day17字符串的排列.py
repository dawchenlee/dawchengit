#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:10:54 2019
题目：字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。
@author: dawchen
"""
# 滑动窗口解法
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 时间复杂度O(m+n),空间复杂度O(n+m),n,m为s1,s2长度
        l1 = len(s1)
        l2 = len(s2)
        charDict1 = collections.Counter(s1)
        tempCharDict = collections.Counter(s2[0:l1])
        for index2 in range(l2-l1+1):
            if index2 != 0:
                lastC = s2[index2-1]
                newC = s2[index2+l1-1]
                tempCharDict[lastC] = tempCharDict[lastC]-1
                if tempCharDict[lastC] == 0:
                    del tempCharDict[lastC]
                if newC in tempCharDict:
                    tempCharDict[newC] = tempCharDict[newC]+1
                else:
                    tempCharDict[newC] = 1
            # print(tempCharDict)
            if tempCharDict.__eq__(charDict1):
                return True
        return False