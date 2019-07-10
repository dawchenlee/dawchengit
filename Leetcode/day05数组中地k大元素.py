#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:25:08 2019
题目： 数组中的第K个最大元素
在未排序的数组中找到第k个最大的元素。请注意，你需要找的是数组排序后的第k个最大的元素，
而不是第k个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

@author: dawchen
"""
### 自己的解法也是最简单的
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ### 本题时间复杂度为O(nlogn),空间复杂度为O(1)
        if nums == []:
            return False
        nums.sort()
        return nums[-k]
'''
当本题为海量数据时，因为本题占用空间复杂度为O(n),所以空间有可能吃紧，时间复杂度为O(nlogn)
时间复杂度也不小
内存方面由于使用为列表复制一次占有同样内存大小的数据，可能爆内存？
'''

### 网上推荐解法一
'''
方法一：堆
思路是创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小小于等于k。这样，堆中就保留
了前 k 个最大的元素。这样，堆顶的元素就是正确答案。
像大小为k的堆中添加元素的时间复杂度为O(logk)，我们将重复该操作N次，故总时间复杂度为O(Nlogk)。
在Python的heapq库中有一个nlargest方法，具有同样的时间复杂度，能将代码简化到只有一行。
本方法优化了时间复杂度，但需要O(k)的空间复杂度。
'''

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]

### 网上推荐解法二
'''
方法二：快速选择
快速选择算法 的平均时间复杂度为O(N)。就像快速排序那样，本算法也是Tony Hoare发明的，
因此也被称为 Hoare选择算法。
本方法大致上与快速排序相同。简便起见，注意到第k个最大元素也就是第N - k个最小元素，因
此可以用第k小算法来解决本问题。
首先，我们选择一个枢轴，并在线性时间内定义其在排序数组中的位置。这可以通过划分算法的帮助来完成。
为了实现划分，沿着数组移动，将每个元素与枢轴进行比较，并将小于枢轴的所有元素移动到枢轴的左侧。
这样，在输出的数组中，枢轴达到其合适位置。所有小于枢轴的元素都在其左侧，所有大于或等于的元素都
在其右侧。
这样，数组就被分成了两部分。如果是快速排序算法，会在这里递归地对两部分进行快速排序，时间复杂度
为O(NlogN)。
而在这里，由于知道要找的第 N - k小的元素在哪部分中，我们不需要对两部分都做处理，这样就将平均时
间复杂度下降到O(N)。
最终的算法十分直接了当 :
随机选择一个枢轴。
使用划分算法将枢轴放在数组中的合适位置pos。将小于枢轴的元素移到左边，大于等于枢轴的元素移到右边。
比较 pos 和 N - k 以决定在哪边继续递归处理。
时间复杂度平均O(n),最坏O(n2)
空间复杂度O(1)
! 注意，本算法也适用于有重复的数组
'''

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)

