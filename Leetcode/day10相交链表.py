#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:09:20 2019
题目：相交链表

@author: dawchen
"""
# 哈希表法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 此解法时间复杂度为O(m+n)，空间复杂度为O(n)
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        return None





'''
我们通常做这种题的思路是设定两个指针分别指向两个链表头部，一起向前走直到其中一个到达末端，另一个与末端距离则是两链表的 长度差 。再通过长链表指针先走的方式消除长度差，最终两链表即可同时走到相交点。

换个消除长度差的方式：拼接两链表。 设长-短链表为 C ，短-长链表为 D （分别代表长链表在前和短链表在前的拼接链表），则当 C 走到长短链表交接处时， D 走在长链表中，且与长链表头距离为 长度差;

以下图片帮助理解：当 ha == hb 时跳出，返回即可
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
