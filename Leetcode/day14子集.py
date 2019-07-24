#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:56:32 2019
题目：子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
@author: dawchen
"""
# 递归和回溯
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 运用回溯和递归 时间复杂度O(n),空间复杂度O(n)
        if nums is None:
            return []
        res = []
        def _dfs(pos,ls,nums):
            res.append(ls[:])
            for i in range(pos,len(nums)):
                ls.append(nums[i])
                _dfs(i+1,ls,nums)
                ls.pop()
        _dfs(0,[],nums)
        return res
    
    
# 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

