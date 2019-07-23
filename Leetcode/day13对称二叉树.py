#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:43:40 2019
题目：对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

@author: dawchen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归法时间复杂度O(n),空间复杂度O(n)
        return self.isMirror(root, root)
        
    def isMirror(self, leftRoot: TreeNode, rightRoot:TreeNode):
        if leftRoot == None and rightRoot == None:
            return True
        if leftRoot == None or rightRoot == None:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isMirror(leftRoot.left, rightRoot.right) and 
                self.isMirror(leftRoot.right, rightRoot.left)


# 方法二 队列实现
class Solution:
    def isSymmetric(self, root):
        """
        队列
        :param root:
        :return:
        """

        if not root:
            return True

        node_queue = [root.left, root.right]  # 在空队列中加入左子树和右子树

        while node_queue:
            left = node_queue.pop(0)          # 依次弹出两个元素
            right = node_queue.pop(0)

            if not right and not left:        # 如果均为空，继续下一个循环
                continue
            if not right or not left:         # 如果只有一个为空，返回False
                return False

            if left.val != right.val:         # 都非空，再判断值是否相等
                return False

            node_queue.append(left.left)      # 将两个左右子树的左右子树逆序加入队列
            node_queue.append(right.right)
            node_queue.append(left.right)
            node_queue.append(right.left)
     #node_queue.extend([left.left, right.right, left.right, right.left]) 
     #或者用这一句话写

        return True

