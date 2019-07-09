#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:36:59 2019
题目：寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1
示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0

@author: dawchen
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 时间复杂度O(n),空间复杂度O(1)
        a = nums[0]
        for i in nums:
            if i < a :
                a = i
        return a
        