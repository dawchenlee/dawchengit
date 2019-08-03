#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 01:32:26 2019
题目：到达数字终点
在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
返回到达终点需要的最小移动次数。

@author: dawchen
"""
'''
因为比如达到target=2=1-2+3.
如果是-2，那就是-2=-1+2-3
所以相当于是完全对称的一个选择。
那么不妨设这个target是正的（用abs函数）
所以我们尽量往右移动就可以达到目的地。
假设1+2+3+...+k=sum
如果sum=target，毫无疑问那么k就是最终答案。#1
如果sum>target，而且sum-target是一个偶数，那么我们可以翻转一个数字的符号来完成等式。
比如sum-target=4，那么我们把2变成-2，那么sum减小了4.
这是由于（1+2+3+...k）-（1-2+3...k）=4
也就是可以归结为：
当sum-target为偶数，1+...-（sum-target）/2+...+k=target，那么答案依然是k。#2
当sum-target为奇数，那么sum-target+1是一个偶数
类似#2的证明，1+...-(sum-target+1)/2+...k=target-1
此时再考虑k的奇偶性。
如果k是偶数并且k>sum-target+1
那么1+...-(sum-target+1)/2+....-(k/2)...+k+(k+1)=target
由#2相似可证，相当于在1+2....+k+(k+1)减去了sum-target+1和k。
等价于sum+（k+1）-sum+target-1-k====>target也就是答案是k+1.#3
如果k=sum-target+1，由#3可知依然是k+1.#4
如果k是奇数：
1+2+...-(sum-target+1)/2.....+k-(k+1)+(k+2)=sum-(sum-target+1)+1=target,
因此答案是k+2.#5
'''
class Solution:
    def reachNumber(self, target: int) -> int:
        #时间复杂度O(1),空间复杂度O(1)
        target = abs(target)
        sum = 0
        i = 1
        while True:
            sum += i
            if sum>= target and (sum - target)%2==0:
                return i
            i += 1

