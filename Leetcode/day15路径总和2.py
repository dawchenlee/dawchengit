#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:41:39 2019
题目：路径综合2
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。
@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 使用DFS用递归 时间复杂度O(n),空间复杂度O(n)
        res = []
        if root is None:
            return
        def helper(root,sums,temp):
            if root is None:
                return
            if not root.left and not root.right and sums == root.val:
                temp.append(root.val)
                res.append(temp)
                return
            helper(root.left,sums-root.val,temp+[root.val])
            helper(root.right,sums-root.val,temp+[root.val])
        
        helper(root,sum,[])
        return res
        