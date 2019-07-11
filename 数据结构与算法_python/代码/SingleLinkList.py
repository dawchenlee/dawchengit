#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:15:33 2019

@author: dawchen
"""

class SingleNode():
    # 单链表的节点
    def __init__(self,elem,next_ = None):
        # elem存放数据
        self.elem = elem
        # next 存放下一个节点的标识
        self.next = next_


class SingleLinkList():
    
    def __init__(self):
        self.__head = None
        
    def is_empty(self):# 判断节点是否为空
        return self.__head == None
    
    def length(self):# 返回节点长度
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def elements(self):# 节点元素生成器
        cur = self.__head
        while cur:
            yield cur.elem
            cur = cur.next
    
    def travel(self):# 遍历节点
        for x in self.elements():
            print(x,end=',')
    
    def add(self,elem):# 在头部添加节点
        node = SingleNode(elem)
        node.next = self.__head
        self.__head = node
        
    def append(self,elem):# 在尾部插入元素
        node = SingleNode(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
    
    def insert(self,pos,elem):
        node = SingleNode(elem)
        if self.is_empty() or pos <= 1:
            self.add(elem)
        elif pos >= self.length():
            self.append(elem)
        else:
            cur = self.__head
            pre = None
            count = 0
            while count < pos:
                count += 1
                pre = cur
                cur = cur.next
            node.next = cur
            pre.next = node
            
    def search(self,elem):
        cur = self.__head
        while cur:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False
    
    def remove(self,elem):
        cur = self.__head
        pre = None
        while cur:
            if cur.elem == elem:
                if not pre:
                    self.__head  == cur.next
                else:
                    pre.next = cur.next
                break
            pre = cur
            cur = cur.next
            
            
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(5))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()        
