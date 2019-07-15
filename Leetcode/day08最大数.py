#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:56:44 2019
题目：最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
示例 1:
输入: [10,2]
输出: 210
示例 2:
输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

@author: dawchen
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ### 暴力解法
        ### 次解法时间复杂度为O(n2),空间复杂度O(n)
        if all([x==0 for x in nums]): return '0'
        def orde(x1, x2):
            return not x1+x2 > x2+x1
        
        nums = [str(x) for x in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if orde(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
    
        return ''.join(nums)