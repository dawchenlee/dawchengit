#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:09:33 2019

@author: dawchen
"""

class Rational():
    @staticmethod
    def _gdc(m,n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n%m ,m
        return n
            
    def __init__(self, num, den=1):
        if not isinstance(num,int) or not isinstance(den,int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1    
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gdc(num,den)
        self._num = sign * (num // g)
        self._den = den // g
        
    def num(self):
        return self._num
    
    def den(self):
        return self._den
    
    def __add__(self,another):
        den = self._den * another.den()
        num = (self._num * another.den()+
               another.num() * self._den)
        return Rational(num,den)
    
    def __mul__(self,another):
        return Rational(self._num * another.num(),
                        self._den * another.den())
    
    def print(self):
        print(str(self._num)+'/'+str(self._den))

r1 = Rational(3,5)
r2 = Rational(7,15)
r3 = r2 + r1
r3.print()

a = [1,3,[2,3]]
b = a
print(a,b)
b[0] = 2
print(a,b) 
