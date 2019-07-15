#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:01:01 2019
题目：求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

@author: dawchen
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 本题时间复杂度为O(mn),空间复杂度为O(m),m为不同数字个数，n为总数字个数
        se = set(nums)
        for i in se:
            count = 0
            for j in nums:
                if i ==j:
                    count += 1
            if count > len(nums) // 2:
                return i
            
            
            
class Solution(object):
    # 运用哈希表来解决此问题
    def majorityElement(self, nums):
        # 此解法时间复杂度O(n),空间复杂度O(n)
        list_1=[]
        n=len(nums)
        for i in range(n//2+1):
            if nums[i]  in list_1:
                i+=1
                continue
            else :
                list_1.append(nums[i])
                if nums.count(nums[i])>n//2:
                    return nums[i]
