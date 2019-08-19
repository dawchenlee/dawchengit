#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:48:27 2019
题目：零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1

@author: dawchen
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #动态规划 cost[amout] = min(cost[amout-c1],cost[amount-c2...cost[amount-cn]])+1
        #时间复杂度O(mn),空间复杂度O(n),n为amount值，m为coins数量
        res = [0 for i in range(amount+1)]
        for i in range(1,amount+1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost,res[i-c]+1)
            res[i] = cost
        if res[amount] == float('inf'):
            return -1
        return res[amount]