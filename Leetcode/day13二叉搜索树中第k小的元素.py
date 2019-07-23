#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:43:13 2019
题目：二叉搜索树中第k小的元素
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

@author: dawchen
"""
'''
二叉搜索树BST有一个重要性质：中序遍历为排序数组，根据这个性质，我们可将问题转化为寻找中序遍历
第k个节点的值；
实现的方法是建立两个全局变量res和count，分别用于存储答案与计数：
在每次访问节点时，计数器-1；
当count == 0时，代表已经到达第k个节点，此时记录答案至res；
找到答案后，已经不用继续遍历，因此每次判断res是否为空，若不为空直接返回。
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res, self.count = None, k
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.res: return
            self.count -= 1
            if not self.count: self.res = root.val
            inorder(root.right)
        inorder(root)
        return self.res

## 模拟系统栈的方式：使用二叉树非递归遍历的通用方法。
class Solution:

    # 模拟系统栈的方式实现，是一种比较通用的做法，
    # 可以作为二叉树的三种非递归遍历

    def kthSmallest(self, root, k):
        # 0 表示当前遍历到它，1 表示压入栈
        # 刚开始是 1 ，不要写成 0 了
        stack = [(1, root)]

        while stack:
            command, node = stack.pop()
            if node is None:
                # 不能写 return ，这不是递归
                continue
            if command == 0:
                k -= 1
                if k == 0:
                    return node.val
            else:
                # 此时 command == 1 的时候，表示递归遍历到的
                # 注意：写的时候倒过来写
                stack.append((1, node.right))
                stack.append((0, node))
                stack.append((1, node.left))


