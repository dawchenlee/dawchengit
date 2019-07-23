#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:23:45 2019
题目：有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 时间复杂度O(n)空间复杂度O(n)
        if len(nums)==0:
            return  
        # 取nums列表的中间下标值
        mid_index = len(nums)//2
        pNode = TreeNode(nums[mid_index])
        pNode.left = self.sortedArrayToBST(nums[:mid_index])
        pNode.right = self.sortedArrayToBST(nums[mid_index+1:])
        return pNode