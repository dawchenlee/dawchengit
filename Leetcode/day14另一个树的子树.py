#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:56:27 2019
题目：另一个树的子树
给定两个非空二叉树s和t，检验s中是否包含和t具有相同结构和节点值的子树。s的一个子树包括
 s 的一个节点和这个节点的所有子孙。s也可以看做它自身的一棵子树。
@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 递归法 时间复杂度O(n),空间复杂度O(n)

        if not t:
            return True
        if not s:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.isSame(p.left,q.left) and self.isSame(p.right,q.right)
    
    
# 先序遍历两个树，生成两个字符串，判断一个字符串是不是另一个字符串的子串**(可以参考：二叉树各种遍历算法)**。
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = self.inorder(s)
        st = self.inorder(t)
        print(st,ss)
        return st in ss
        
    def inorder(self,root):
        if not root:
            return '#'
        return '*'+str(root.val)+self.inorder(root.left)+self.inorder(root.right)
        # *是为了防止两个数个位数相同（比如：2，12）造成的误判，因此用一个符合标记数字开头


