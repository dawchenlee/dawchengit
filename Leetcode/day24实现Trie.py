#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:27:19 2019
题目：实现Trie（前缀树）
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

@author: dawchen
"""

'''
本质上是字典按字母迭代
apple:{'a': {'p': {'p': {'l': {'e': {'end': True}}}}}}            #第一次insert
最后一个'e'存在结束'end'
app:  {'a': {'p': {'p': {'l': {'e': {'end': True}}, 'end': True}}}}#第二次insert
第二个'p'存在结束'end'
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if not i in node.keys():
                node[i] = {}
            node = node[i]
        node['end'] = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if not i in node.keys():
                return False
            node = node[i]
        return node.get('end',False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if not i in node.keys():
                return False
            node = node[i]
        return True


