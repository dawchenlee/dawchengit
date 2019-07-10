#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:34:34 2019
题目：搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

@author: dawchen
"""
### 自己的解法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## 本题时间复杂度O(mn),空间复杂度O(1) ,其中m为行数，n为列数
        if matrix == [] or matrix == [[]]: # 排除矩阵为空的特殊情况
            return False
        if matrix[0][0] > target or matrix[-1][-1] < target:# target小于最小或大于最大数情况
            return False
        # 此循环时间复杂度为O(m)
        for i in range(len(matrix)):# 先找出target可能在哪行出现，然后在相应行中遍历寻找
            if matrix[i][-1] < target:
                continue
            elif matrix[i][-1] == target:
                return True
            else:
                # 此循环时间复杂度为O(n)
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
                else:
                    return False     
                
                
###  改进自己的版本
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## 时间复杂度为O(m+n),空间复杂度为O(1)
        if matrix == [] or matrix == [[]]:
            return False
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            elif matrix[i][-1] == target:
                return True
            else:
                m = i
                break
        for j in range(len(matrix[0])):
            if matrix[m][j] == target:
                return True
        else:
            return False
        
        
### 二分查找
'''
注意到输入的m x n矩阵可以视为长度 m x n的有序数组。由于该 虚 数组的序号可以由下式方便
地转化为原矩阵中的行和列(我们当然不会真的创建一个新数组) ，该有序数组非常适合二分查找。
      row = idx // n ， col = idx % n。
      
算法
这是一个标准二分查找算法 :
初始化左右序号 left = 0 和 right = m x n - 1。
While left < right :

选取虚数组最中间的序号作为中间序号: pivot_idx = (left + right) / 2。

该序号对应于原矩阵中的row = pivot_idx // n行,col = pivot_idx % n列, 由此可以
拿到中间元素pivot_element。该元素将虚数组分为两部分。

比较 pivot_element 与 target 以确定在哪一部分进行进一步查找。
'''

### 复杂度分析

## 时间复杂度 : 由于是标准的二分查找，时间复杂度为O(log(mn))。
## 空间复杂度 : O(1)O(1)。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        #二分查找
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
             