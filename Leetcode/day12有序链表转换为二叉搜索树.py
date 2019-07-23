#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:22:55 2019
题目：有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
@author: dawchen
"""
# 双指针法

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        p,q,pre = head, head, None
        while q and q.next:
            pre = p
            p = p.next
            q= q.next.next
        pre.next = None
        root = TreeNode(p.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p.next)
        return root
    
# 底顶递归法
'''
链表的特性导致我们无法像数组那样通过下标访问各个元素。若想按照108题的做法，就需要设置两个指针
p1 p2，p1每走一步p2走两步，这样p2结束时p1就在中点。但这样会导致每次递归都需要重复遍历链表，效率较低。
我们考虑是否可以让建立节点的顺序匹配链表元素顺序？这样每次建立节点时，只需要获取链表下一个元素即可。
使用递归模拟中序遍历过程，建立节点的顺序即与链表元素顺序一一对应，bottom-up建立树，最终返回根节点。
递归前需要统计链表长度n，整体算法复杂度O(N)。
'''
class Solution:
    # 此解法时间复杂度O(n)空间复杂度O(1)
    def __init__(self):
        self.head = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n, self.head = 0, head
        while head:
            head = head.next
            n += 1
        return self.to_bst(0, n - 1)
    def to_bst(self, left, right):
        if left > right: return
        m = (left + right) // 2
        left_child = self.to_bst(left, m - 1)
        father = TreeNode(self.head.val)
        self.head = self.head.next
        father.left = left_child
        father.right = self.to_bst(m + 1, right)
        return father
