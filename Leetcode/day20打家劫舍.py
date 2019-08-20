#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:05:17 2019
题目：打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素
就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
@author: dawchen
"""
'''
当前最大的累计收益= max(前一家的收益，前前一家的收益加上当前的收益)

状态转移方程： dp[i] = max(dp[i-1], dp[i-2]+nums[i])
'''
class Solution:
    # dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        p = nums[0]
        q = max(nums[0],nums[1])
        
        for i in range(2,n):
            next_ = max(p+nums[i],q)
            p,q = q, next_
            
        return q