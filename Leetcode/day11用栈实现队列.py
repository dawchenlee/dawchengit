#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:16:08 2019
题目：用栈实现队列
@author: dawchen
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack_in:
            self.stack_out .append(self.stack_in.pop())
        pop_v = self.stack_out.pop()
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return pop_v

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        pop_v = self.stack_out.pop()
        self.stack_in.append(pop_v)
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return pop_v

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()