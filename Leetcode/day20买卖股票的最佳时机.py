#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 03:24:51 2019
题目：买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
@author: dawchen
"""
# 动态规划,我们可以遍历数组,记录前面最小的价格,用当天价格减去最小价格,一定是这天可以获得最大利润!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        res = 0
        for i in range(1,len(prices)):
            res = max(res,prices[i] - min_p)
            min_p = min(min_p, prices[i])
        return res