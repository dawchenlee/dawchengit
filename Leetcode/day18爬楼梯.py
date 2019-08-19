#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:33:58 2019
题目：爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
@author: dawchen
"""
# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
       # dp[i] = dp[i-1] + dp[i-2]
       # 时间复杂度O(n),空间复杂度O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])