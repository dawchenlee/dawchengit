#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 03:41:56 2019
题目：使用最小花费爬楼梯
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

@author: dawchen
"""

'''
时间复杂度O(n)， 空间复杂度O(l)。基本上都是击败95%以上的用户，大家可以参考一下。
初始状态：dp[0] = cost[0], dp[1] = cost[1]
状态转移方程： dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
实际上是求到最后一个楼梯的下一个楼梯需要多少体力。
'''
class Solution:
    # dp[i] = min(dp[i-1],dp[i-2])+cost[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n==2:
            return min(cost)
        
        p = cost[0]
        q = cost[1]
        for i in range(2,n):
            next_ = min(p,q) + cost[i]
            p = q
            q = next_  
        return min(p,q)
