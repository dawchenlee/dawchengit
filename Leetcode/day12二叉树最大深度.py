#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:20:16 2019
二叉树最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归法时间复杂度O(n)空间复杂度O(n)
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth) + 1
            
            
#遍历法 时间复杂度O(n)空间复杂度O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        cur = [root]
        depth = 1
        while cur:
            nex = []
            while cur:
                pnode = cur.pop(0)
                if pnode.left is not None:
                    nex.append(pnode.left)
                if pnode.right is not None:
                    nex.append(pnode.right)
            if nex != []:
                depth += 1
            cur = nex
        return depth     