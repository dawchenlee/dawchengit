#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:23:25 2019

@author: dawchen
"""
### 栈
class StackUnderflow(ValueError):
    pass



class SStack():# 基于顺序表实现栈类
    
    def __init__(self):# 用list对象储存栈中元素
        self._elems = []
        
    def is_empty(self):
        return self._elems ==[]
    
    def top(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.top')
        return self._elems[-1]
    
    def push(self, elem):
        self._elems.append(elem)
        
    def pop(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.pop')
        return self._elems.pop()
    
    
st1 = SStack()
st1.push(3)
st1.push(5)
while not st1.is_empty():
    print(st1.pop())
    

class LStack():# 基于链接表技术实现栈类，用LNode作为节点
    
    def __init__(self):
        self._top = None
      
    def is_empty(self):
        return self._top == None
    
    def top(self):
        if self._top == None:
            raise StackUnderflow('in LStack.top')
        return self._top.elem
    
    def push(self,elem):
        self._top = LNode(elem, self._top)
        
    def pop(self):
        if self._top is None:
            raise StackUnderflow('in SStack.top')
        p = self._top.elem
        self._top = self._top.next
        return p
    

### 栈的应用
        
'''括号的匹配问题'''

def check_parens(text):
    '''括号配对检查函数，text是被检查字符串'''
    parens = '() [] {}'
    open_parens = '([{'
    opposite = {')':'(',']':'[','}':'{'}
    
    def parentthese(text):
        '''括号生成器，每次调用分会text中的下个括号极其位置'''
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
            
        st = SStack()  #保存括号的栈
        for pr, i in parenthese(text):
            if pr in open_parens:
                st.push(pr)
            elif st.pop() != oppostie[pr]:
                print('Unmatching is found at %s for %s'%(i,pr))
                return False
        print('All parenthese are correctly matched')
        return True
        
'''后缀表达式的计算'''
class ESStack(SStack):
    def depth(self):
        return len(self._elems)
    
def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()
    
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError('short of operands')
        a = st.pop()
        b = st.pop()
        
        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break
        st.push(c)
        if st.depth() == 1:
            return st.pop()
        raise SyntaxError('Extra operands')
        
        
'''中缀表达式转换后缀表达式'''
def trans_infix_suffix(line):
    st = SStack()
    exp = []
    
'''简单背包问题'''
'''
knap(weight,n)表示n件物品相对于总重量weight的背包问题通过考虑一件物品的选取与否来把
原问题分解为两种情况。
如果不选择最后一件物品那么knap(weight,n-1)的解就是knap(weight,n)的解
如果选择最后一件物品，那么如果kanp(weight-w,n-1)有解
根据上述情况原问题被归结到更简单的问题
1.重量weight等于零说明问题有解
2.重量weight已经小于零，那么按照已做安排不能得到解
3.重量大于0但没有物品可用说明本安排无解
'''
def knap_rec(weight,wlist,n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - weight[n-1],wlist,n-1):
        return True
    if knap_rec(weight,wlist,n-1):
        return True
    else:
        return False


### 队列
class SQueue():
    
    def __init__(self,init_len=8):
        self._len = init_len
        self._elems =  [0] * init_len
        self._head = 0
        self._num = 0
    
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self.elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e
        
    def enqueue(self,elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1
    
    def __extend(self):
        old_len = self._len
        self._lem *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head +i) % old_len]
        self._elems, self._head = new_elems, 0
        
        
        
        
'''迷宫类题：状态空间搜索问题基本特征：
1.存在一集可能状态（位置、情况等）
2.有一个初始状态s0，一个或者多个结束状态，或有判断成功结束的方法。
3.对每个状态s，有neighbor(s)表示与s相邻的一组状态（一步可达）
4.有一个判断函数valid(s)判断s是否为可行状态。
5.问题：找出从s0出发到达结束状态的路径；或者从s0出发设法找到一个或全部解。
'''
def mark(maze,pos):# 给迷宫maze的位置pos标2表示已走过
    maze[pos[0],pos[1]] = 2
    
def passable(maze,pos): #检查迷宫的位置pos是否可行
    return maze[pos[0],pos[1]] == 0

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
#迷宫题栈的递归
def find_path(maze,pos,end):
    mark(maze.pos)
    if pos == end:# 到达出口
        print(pos,end='')
        return True
    for i in range(4):# 按四个方向顺序探查
        nextp = pos[0] + dirs[i][0],  pos[1] + dirs[i][1]
        if passable(maze,nextp):# 不可行的位置不管
            if find_path(maze,nextp,end):#从nextp可行
                print(pos, end='')
                return True
    return False


#迷宫题栈和回溯法
'''回溯法执行两种基本操作：前进和后退
前进：
条件：当前位置存在尚未探查的四邻位置
操作：选择下一个位置并向前探查。如果还存在其他可能未探查的分之，就记录相关信息以便将来使用。
如果找到出口就成功推出

后退（回溯）：
条件：遇到死路，不存在尚未探索的四邻位置
操作：退回最近记录的那个分支点，检查那里是否还存在尚未探索的分支。如果有就取一个未探查相邻位置
    作为当前位置并前进，没有就将其删除并继续回溯。
已穷尽所有可能：不能找到出口时易失败结束
'''

# 算法实现

def maze_solver(maze,start,end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze,start)
    st.pushu((start,0))# 入口和方向0的需对入栈
    while not st.is_empty:
        pos, nxt = st.pop()
        for i in range(nxt,4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if nextp == end:
                pirnt_path(end,pos,st)
                return
            if passable(maze,nextp):
                st.push((pos,i+1))
                mark(maze,nextp)
                st.push((nextp,0))
                break
    print('not found')
    

## 基于队列实现

def maze_solver_queue(maze,start,end):
    if start == end:
        print('path find')
        return
    mark(maze,start)
    qu = SQueue()
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze,nextp):
                if nextp == end:
                    print('find path')
                    return
                mark(maze,nextp)
                qu.enqueue(nextp)
        print('no path')
        
'''习惯上把基于栈的搜索称为深度优先搜索，把基于队列的搜索称为宽度优先搜索'''

    