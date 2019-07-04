#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:37:06 2019

@author: dawchen
题目：亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 
中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
题目考点：一种是两个字符串完全相等，那么交换两个字符还要使得他们相等
，只能交换两个相同的字符。另一种就是只有两处不一样，且不一样的位置的值交错相等。
"""
###自己的版本
本题的考点为
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        count = 0
        l = []
        # 比较字符串A与B的长度
        if len(A) == len(B):
            # 判断A与B相同位置的字母是否一致 for语句的时间复杂度为O(n),空间复杂度O(n)
            for i in range(0,len(A)):
                if A[i] == B[i]:
                    pass
                # 记录不一致的数量并记录索引值
                else:
                    count += 1
                    l.append(i)
            # 根据count值分别判断
            if count > 2 or count == 1:
                return False
            elif count == 2:
                if A[l[0]] == B[l[1]] and A[l[1]] == B[l[0]]:
                    return True
                else:
                    return False
            elif count == 0:
            # 当A、B字符串完全相同时判断字符串中是否有重复字符，时间复杂度为O(n),空间复杂度O(1)
                for a in A:
                    # 这里A.count的时间复杂度为O(n)
                    if A.count(a) >= 2:
                        return True
                return False
        else:
            return False
                    
### 本题的时间复杂度T(n) = O(n2),空间复杂度S(n) = O(n)





#### 老师提供的一个版本 时间复杂度T(n)=O(n),空间复杂度S(n)=O(n)
#class Solution:
#    def buddyStrings(self, A: str, B: str) -> bool:
#        if len(A) != len(B): 
#            return False
#        if A == B and len(set(A)) < len(A): 
#            return True
#        dif = [(a, b) for a, b in zip(A, B) if a != b]
#        return len(dif) == 2 and dif[0] == dif[1][::-1]
#
#提示python中的hash用set来处理。