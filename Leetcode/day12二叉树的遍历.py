#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 03:28:53 2019
二叉树的遍历
@author: dawchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''前序遍历递归'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归解法 时间复杂度O(n),空间复杂度O(n)
        res = []
        if root:
            res.append(root.val)
            res += self.inorderTraversal(root.left)
            res += self.inorderTraversal(root.right) 
        return res
    
'''前序遍历迭代'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


'''中序遍历递归'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归解法 时间复杂度O(n),空间复杂度O(n)
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right) 
        return res

'''中序遍历迭代'''
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            # 看右子树
            p = tmp.right
        return res


'''后序遍历递归'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 运用递归 时间复杂度O(n),空间复杂度O(n)
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res
    
'''后序遍历迭代'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]

'''层次遍历'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #时间复杂度O(n)空间复杂度O(n)
        if root is None:
            return []
        res,cur_level = [],[root]
        while cur_level:
            temp = []
            next_level = []
            for i in cur_level:
                temp.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            res.append(temp)
            cur_level = next_level
        return res