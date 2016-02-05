# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:10:52 2015

@author: francisparan
"""


def fib(limit):
    a,b = 0, 1

    for x in range(1,limit+1):
        a, b = b, a+b
        yield a
       
print '\nfib:', 
for x in fib(10):
    print x,


def fib2(limit):
    a,b = 0, 1

    result = []    
    
    for x in range(1, limit+1):
        a, b = b, a+b
        result.append(a)
    return result

print '\nfib2:',   
for x in fib2(10):
    print x,

# def factorial(n): return reduce(lambda a,b: a*b, range(1, n+1), 1)


def fib3(n): return [ x + (x + 1) for x in range(1,n-1)]