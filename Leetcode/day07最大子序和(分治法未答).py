#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:33:24 2019
题目： 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
@author: dawchen
"""

class Solution:
'''
动态规划典型题：
遍历数组，记录max(nums[i-1] + nums[i], nums[i])（含义为保留前面累加和与以当前元素为开始，哪种更优）
即判断后面subarray是否舍去前面的累计加和，并继续遍历下一元素。
最后return加和中最大值。
'''
    def maxSubArray(self, nums: List[int]) -> int:# 此解法时间复杂度为O(n),空间复杂度为O(1)
        size = len(nums)
        if nums == 1:
            return nums[0]
        for i in range(1,size):
            nums[i] = max(nums[i-1] + nums[i],nums[i])
        return max(nums)
            
    
    
### 此题的分治法还未看