#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:21:52 2019
题目：三数之和
给定一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c，
使得a + b + c = 0？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

@author: dawchen
"""
### 题解思路
'''
如果Brute force，则是O(n3)时间复杂度，有优化空间。
先将给定nums排序，简化问题，复杂度为O(nlogn)。
令nums[k] + nums[i] + nums[j] == 0，找所有的组合的思路是：遍历三个数字中最左数字的指针k
，找到数组中所有不重复k对应所有b c组合，即每指向新的nums[k]，都通过双指针法找到所有和为0的
nums[i] nums[j]并记录：
当nums[k] > 0时，直接跳出，因为j > i > k，所有数字大于0，以后不可能找到组合了；
当k > 0 and nums[k] == nums[k - 1]，跳过此数字，因为nums[k - 1]的所有组合已经被加入
到结果，如果本次搜索，只会搜索到重复组合。
i, j分设在[k, len(nums)]两端，根据sum与0的大小关系交替向中间逼近，如果遇到等于0的组合则
加入res中，需要注意：移动i j需要跳过所有重复值，否则重复答案会被计入res。
整体算法复杂度O(n2)。
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 本题时间复杂为O(n2),空间复杂度为O(n)
        n = len(nums)
        nums.sort()
        target = 0
        res = []
        for i in range(n -2):# 时间复杂度O(n)
            if i > 0 and nums[i] == nums[i-1]: # 选的这个数不能重复
                continue
            if nums[i] + nums[i+1] + nums[i+2] > target: # 最小的结果
                break
            if nums[n-1] + nums[n-2] + nums[i] < target: # 最大的结果
                continue
            l = i + 1
            r = n - 1
            while l < r:# 时间复杂度O(n)
                temp = nums[i] + nums[l] + nums[r]
                if temp == target:
                    res.append([nums[i], nums[l], nums[r]]) # 空间复杂度O(n)
                    l += 1
                    r -= 1
                    # 去掉重复
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif temp < target:
                    l += 1
                else:
                    r -= 1         
        return res 