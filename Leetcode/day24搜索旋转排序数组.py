#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:31:42 2019
题目：搜索旋转排序数组 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

@author: dawchen
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 时间复杂度O(n),空间复杂度O(1)
        if nums == []:
            return False
        pre = nums[0]
        index = 0
        if len(nums) == 1:
            return nums[0] == target 
        for i in range(1,len(nums)):
            if nums[i] < pre:
                index = i
            pre = nums[i]
        if nums[0] > target:
            first = index
            last = len(nums) - 1
            while first <= last:
                midpoint = (first + last) // 2
                if nums[midpoint] == target:
                    return True
                if nums[midpoint] < target:
                    first = midpoint + 1
                else:
                    last = midpoint - 1
            return False
        else:
            first = 0
            if index == 0:
                index = len(nums)
            last = index - 1
            while first <= last:
                midpoint = (first + last) // 2
                if nums[midpoint] == target:
                    return True
                if nums[midpoint] < target:
                    first = midpoint + 1
                else:
                    last = midpoint - 1
            return False
                