#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:52:02 2019
题目：移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
@author: dawchen
"""
### 自己解法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ## 此解法时间复杂度为O(n),空间复杂度为O(1)
        if head == None:
            return head
        pre = None
        cur = head
        while cur:
            if cur.val == val:
                if pre == None:
                    head = cur.next
                    cur = cur.next
                    continue
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head


### 网上解法

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        pre, cur = head, head and head.next
        while cur:
            if cur.val == val:
                pre.next = cur = cur.next
            else:
                pre, cur = cur, cur.next
        return head
'''    
迭代：
第一个 while 用于找到应该返回的链表头（应该跳过所有特殊 val 的节点）
第二个 while 用于把前一个节点指针接到下一个节点（如果当前节点值为 val）
'''
