#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:39:25 2019
题目：零钱兑换2
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
假设每一种面额的硬币有无限个。 


@author: dawchen
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 动态规划 时间复杂度O(mn),空间复杂度O(n)
        if amount==0:
            return 1
        if len(coins)==0 or coins==None:
            return 0
        dp=[0 for _ in range(amount+1)]
        dp[0]=1
        for coin in coins:
            #记录每添加一种面额的零钱，总金额j的变化
            for i in range(coin,amount+1):
                dp[i]=dp[i]+dp[i-coin]
        return dp[amount]
        