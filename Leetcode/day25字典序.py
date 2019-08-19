#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:30:47 2019
题目：字典序
交换操作：
对于数组中的两个下标i,j（1<=i.j<=n）,如果ai+aj为奇数，那么就可以交换这两个数
现在允许我们的交换次数不限，求出能够通过若干次操作后得到的数组中字典序最小的一个
example:
  {A）  
    输入 7 3 5 1    输出 7 3 5 1
（B）
    输入 53941 38641 31525 75864 29026 12199 83522 58200 64784 80987
    输出 12199 29026 31525 38641 53941 58200 64784 75864 80987 83522 

@author: dawchen
"""

def sortdic(nums):
    if nums == []:
        return nums
    sign = 0
    for i in nums:
        if i % 2 == 0:
            sign += 1
    if sign == 0 or sign == len(nums):
        return nums
    def quick_sort(nums,start,end):
        if start >= end:
            return 
        left = start
        right = end
        mid_value = nums[start]
        while left < right:
            while left < right and nums[right] >= mid_value:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < mid_value:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid_value
        quick_sort(nums,start,left)
        quick_sort(nums,left+1,end)
    quick_sort(nums,0,len(nums)-1)
    return nums
      


nums = [53941, 38641, 31525, 75864, 29026, 12199, 83522, 58200, 64784, 80987]      
sortdic(nums)
nums

