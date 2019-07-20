#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:57:17 2019
题目：用队列实现栈
@author: dawchen
"""
### 运用两个队列方法
'''
栈是一种 后进先出（）的数据结构，栈内元素从顶端压入（push），从顶端弹出（pop）。
一般我们用数组或者链表来实现栈，但是这篇文章会来介绍如何用队列来实现栈。队列是一种与栈相反的
先进先出的数据结构，队列中元素只能从后端（rear入队（push），然后从 前端（front）端出队（pop)
为了满足栈的特性，我们需要维护两个队列 q1 和 q2。同时，我们用一个额外的变量来保存栈顶元素。
'''
class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self, x):
        return self.queue.append(x)
        
    def pop(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
        
    def empty(self):
        return self.queue == []
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.top_v = None
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.push(x)
        self.top_v = x
        print(self.top_v)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        pre_v = None
        pop_v = self.top_v
        if self.queue1.empty():
            return None
        while not self.queue1.empty():
            if self.queue1.peek() is self.top_v:
                self.queue1.pop()
            else:
                pre_v = self.queue1.pop()
                print(pre_v)
                self.queue2.push(pre_v)
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.top_v = pre_v
        return pop_v

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_v

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue1.empty()


