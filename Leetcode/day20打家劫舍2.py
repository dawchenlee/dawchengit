#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:18:17 2019
题目：打家劫舍2
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈
，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间
相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

@author: dawchen
"""
'''
打家劫舍 的升级版，加入了一个限制条件：第一间屋子和最后一间屋子不能同时被抢。即，要么抢第一间，
要么抢最后一间。
因此，可以把问题拆分为两个基础版的 打家劫舍：

去掉第一间，打劫一次
去掉最后一间，打劫一次
取两次打劫能获得的最大值
对于基础版打家劫舍而言，设打劫到第 i 家的最大收益为 dp[i]，则有：

dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        
        def rob_action(nums):
            length = len(nums)
            dp = [0 for _ in range(length)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp
        
        # 去掉第一间
        nums1 = nums[1:]
        dp1 = rob_action(nums1)
        # 去掉最后一间
        nums2 = nums[:-1]
        dp2 = rob_action(nums2)
        
        return max(dp1[-1], dp2[-1])