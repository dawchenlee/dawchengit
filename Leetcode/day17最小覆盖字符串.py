#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:14:06 2019
题目：最小覆盖字符串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
@author: dawchen
"""
'''
本问题要求我们返回字符串S中包含字符串TT的全部字符的最小窗口。我们称包含T的全部字母的窗口为可行窗口。
可以用简单的滑动窗口法来解决本问题。
在滑动窗口类型的问题中都会有两个指针。一个用于延伸现有窗口的right指针，和一个用于收缩窗口
的left指针。在任意时刻，只有一个指针运动，而另一个保持静止。
本题的解法很符合直觉。我们通过移动right指针不断扩张窗口。当窗口包含全部所需的字符后，
如果能收缩，我们就收缩窗口直到得到最小窗口。
答案是最小的可行窗口。

算法
1.初始，left指针和right指针都指向SS的第一个元素.
2.将 right指针右移，扩张窗口，直到得到一个可行窗口，亦即包含T的全部字母的窗口。
3.得到可行的窗口后，将leftt指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。
4.若窗口不再可行，则跳转至2。
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t and s:
            return ''
# 时间复杂度:O(|S|+|T|)其中|S|和|T|代表字符串S和T的长度。
# 空间复杂度:O(|S|+|T|)
        # 用字典记录t中所有字母出现的次数
        dic_t = collections.Counter(t)
        # t需要在滑动窗口中出现中唯一字母的长度
        required = len(dic_t)
        # 初始化左右指针
        r, l = 0, 0
        # formed 用来记录t中字母在滑动窗口中出现次数符合要求的
        formed = 0
        # 用字典记录滑动窗口中所有字母出现的次数
        window_counts = {}

        # 用元组表示答案包括长度，左右指针
        ans = (float('inf'),None,None)

        while r < len(s):
            # 从右往窗口中添加字母
            character = s[r]
            window_counts[character] = window_counts.get(character,0) + 1
            # 如果当前字母的数量达到t中所要求的则foremd加1
            if character in dic_t and window_counts[character] == dic_t[character]:
                formed += 1

            # 当窗口覆盖t时停止r，并尝试移动l缩短窗口
            while l <= r and formed == required:
                character = s[l]
                #记录目前位置最小的窗口
                if r - l + 1 < ans[0]:
                    ans = (r-l+1,l,r)
                # 当前左指针所指的字母剔除窗口
                window_counts[character] -= 1
                if character in dic_t and window_counts[character] < dic_t[character]:
                    formed -= 1
                # 先移动左指针，寻找新窗口
                l += 1
            # 移动右指针
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

 '''
解法二：优化滑动窗口
对上一方法进行改进，可以将时间复杂度下降到O(2*|filtered_S|+|S|+|T|)其中Sfiltered_S
是从S中去除所有在T中不存在的元素后，得到的字符串。
当∣filtered_S∣<<<∣S∣时，优化效果显著。这种情况可能是由于T的长度远远小于S，因此S中包括
大量T中不存在的字符。

算法
我们建立一个filtered_S列表，其中包括S中的全部字符以及它们在S的下标，但这些字符必须在T中出现。
比如S = "ABCDDDDDDEEAFFBC" T = "ABC" 
filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
此处的(0, 'A')表示字符'A' 在字符串SS的下表为0。
现在我们可以在更短的字符串ffiltered_S中使用滑动窗口法。
 '''
 def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
