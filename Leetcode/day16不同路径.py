#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:44:40 2019
题目：不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径
@author: dawchen
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # 动态规划 时间复杂度O(n)空间复杂度O(n)
    # 思路：右下角的点只能由其上方和左方的格子过去所以
    # 动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
