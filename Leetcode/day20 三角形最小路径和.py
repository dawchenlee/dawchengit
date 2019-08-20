#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:39:33 2019
题目：三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
@author: dawchen
"""
# 动态方程: dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + triangle[i][j]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        #print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]       
