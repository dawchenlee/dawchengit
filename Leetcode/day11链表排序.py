#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:23:01 2019
题目：排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

@author: dawchen
"""
'''
题目要求时间空间复杂度分别为O(nlogn)和O(1)，根据时间复杂度我们自然想到二分法，从而联想到归并排序；
对数组做归并排序的空间复杂度为O(n)，而根据链表可以通过修改引用来断开的特性，无需开辟额外空间，
因此可以满足题目 O(1)空间复杂度的要求；
对链表使用归并排序，需要解决以下几个问题：
分割cut环节：找到当前链表中点，并从中点将链表断开（以便在下次递归cut时，链表片段拥有正确边界）；
我们使用fast,slow快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
找到中点slow后，执行slow.next = None将链表切断。
递归分割时，输入当前链表左端点head和中心节点slow的下一个节点tmp(因为链表是从slow切断的)。
cut 递归终止条件：当head.next == None时，说明只有一个节点了，直接返回此节点。
合并 merge 环节：将两个排序链表合并，转化为一个排序链表。
双指针法合并，建立辅助ListNode h作为头部。
设置两指针left, right分别指向两链表头部，比较两指针处节点值大小，由小到大加入合并链表头部，
指针交替前进，直至添加完两个链表。
返回辅助ListNode h 作为头部的下个节点 h.next。
时间复杂度 O(l+r)，l, r分别代表两个链表长度。
当题目输入的 head == None 时，直接返回None。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 此解法为归并算法。时间复杂度O(nlogn),空间复杂度O(1)
        if head == None or head.next == None:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        p = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left:
            p.next = left
        else:
            p.next = right
        return res.next