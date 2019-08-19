#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:35:03 2019
题目：最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。
@author: dawchen
"""
'''哈希表和线性空间的构造
算法
这个优化算法与暴力算法仅有两处不同：这些数字用一个HashSet保存（或者用Python里的Set）
实现O(1)时间的查询，同时，我们只对当前数字-1不在哈希表里的数字，作为连续序列的第一个数字去找
对应的最长序列，这是因为其他数字一定已经出现在了某个序列里。
复杂度分析
时间复杂度：O(n)
尽管在for循环中嵌套了一个while循环，时间复杂度看起来像是二次方级别的。但其实它是线性的算法。
因为只有当currentNum遇到了一个序列的开始，while循环才会被执行（也就是currentNum-1不在数组nums里)
while循环在整个运行过程中只会被迭代n次。这意味着尽管看起来时间复杂度为O(n⋅n) ，实际这个嵌套
循环只会运行O(n+n) =O(n)次。所有的计算都是线性时间的，所以总的时间复杂度是O(n)的。
空间复杂度：O(n)
为了实现O(1)的查询，我们对哈希表分配线性空间，以保存nums数组中的O(n)个数字。除此以外，
所需空间与暴力解法一致
'''
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


'''
：排序
想法
如果我们可以将数组中的数字升序迭代，找连续数字会变得十分容易。为了将数组变得有序，我们将数组进行排序。

算法
在我们开始算法之前，首先检查输入的数组是否为空数组，如果是函数直接返回0 。对于其他情况，
我们将nums数组排序，并考虑除了第一个数字以外的每个数字与它前一个数字的关系。如果当前数字和
前一个数字相等，那么我们当前的序列既不会增长也不会中断，我们只需要继续考虑下一个数字。如果
不相等，我们必须要检查当前数字是否能延长答案序列（也就是nums[i] == nums[i-1] + 1）。
如果可以增长，那么我们将当前数字添加到当前序列并继续。否则，当前序列被中断，我们记录当前序列的
长度并将序列长度重置为 1 。由于nums中的最后一个数字也可能是答案序列的一部分，所以我们将当前
序列的长度和记录下来的最长序列的长度的较大值返回。
'''
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


