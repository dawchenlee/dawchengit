#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:09:39 2019

@author: dawchen
"""

class Node():
    
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = None
        

class SinCycleLinkList():
    
    def __init__(self):
        self.__head = None
        
    def is_empty(self):
        return self.__head == None
    
    def length(self):
        if self.__head == None:
            return 0
        cur = self.__head.next
        count = 1
        while cur != self.__head:
            cur = cur.next
            count += 1
        return count
    
    def elements(self):
        if self.is_empty():
            return None
        yield self.__head.elem
        cur = self.__head.next
        while cur != self.__head:
            yield cur.elem
            cur = cur.next
    def travel(self):
        for x in self.elements():
            print(x,end=',')
            
    def add(self,elem):
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = node
        node.next = self.__head
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        self.__head = node
        
    def append(self,elem):
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        
    def insert(self,pos,elem):
        if pos <= 0:
            self.add(elem)
        elif pos >= (self.length() - 1):
            self.append(elem)
        else:
            node = Node(elem)
            cur = self.__head
            count = 0
            while count < (pos - 1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
    
    def remove(self, elem):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self.__head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.elem == elem:
            # 如果链表不止一个节点
            if cur.next != self.__head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self.__head.next
                self.__head = self.__head.next
            else:
                # 链表只有一个节点
                self.__head = None
        else:
            pre = self.__head
            # 第一个节点不是要删除的
            while cur.next != self.__head:
                # 找到了要删除的元素
                if cur.elem == elem:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.elem == elem:
                # 尾部删除
                pre.next = cur.next
            
            
    def search(self, elem):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        if cur.elem == elem:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.elem == elem:
                return True
        return False



if __name__ == "__main__":
    ll = SinCycleLinkList()
    ll.add(1)  # 1
    ll.add(2)  # 21
    ll.append(3) # 213
    ll.insert(2, 4) # 2143
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(5))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()

