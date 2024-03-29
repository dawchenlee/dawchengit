#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:42:35 2019
题目：二叉树展开为链表
给定一个二叉树，原地将它展开为链表。
例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 递归法 时间复杂度O(n)空间复杂度O(n)
        if not root or (not root.left and not root.right):
            return root
        
        #先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right #把捋直的右子树备份一下
        root.right = root.left #把捋直的左子树放到右边
        root.left = None #记得把左子树置空
        while(root.right): #找到现在右子树的最后一个node
            root = root.right
        root.right = tmp #把捋直的原来的右子树接上去        