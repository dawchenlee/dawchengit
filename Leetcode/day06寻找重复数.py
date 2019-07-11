#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:36:02 2019
题目：寻找重复数
给定一个包含n + 1个整数的数组nums，其数字都在1到n之间（包括1和n），可知至少存在
一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:
输入: [3,1,3,4,2]
输出: 3
说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

@author: dawchen
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 此解法时间复杂度为O(n),空间复杂度为O(1)
        # slow每次走一步，fast每次走两步，查找交叉口
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 从起始点开始一个新的每次步数为一的点，直到其和slow点相遇
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
                    # 当两个值相等时返回
            if slow == finder:
                return slow
'''
使用数组中的值作为索引下标进行遍历，遍历的结果肯定是一个环（有一个重复元素） 检测重复元素问题转换成检测环的入口 为了找到环的入口，可以进行如下步骤：

设置两个快慢指针， fast每次走两步，slow每次走一步，最终走了slow走了n步与fast相遇，fast走了2*n，fast可能比slow多饶了环的i圈，得到环的周长为n/i
slow指针继续走, 且另设第三个指针每次走一步，两个指针必定在入口处相遇
假设环的入口和起点的距离时m
当第三个指针走了m步到环的入口时
slow刚好走了n + m步，换句话说时饶了环i圈（环的周长为n/i）加m步（起点到入口的距离）
得到相遇的是环的入口，入口元素即为重复元素
'''