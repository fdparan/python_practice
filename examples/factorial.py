# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:54:52 2015

@author: francisparan
"""


def print_factorial(func, num_size = 6):
    print '=' * 50
    
    for x in range(num_size):
        print '{0} {1}: {2}'.format(func.__name__, x, func(x))

# non-recursive implementation
def factorial_non_recursive(num):
    result = 1
    for n in range(result, num+1):
        result *= n
    return result

print_factorial(factorial_non_recursive)

# recursive implementation
def factorial_recursive(num):
    
    if num == 0:
        return 1
    
    return num * factorial_recursive(num-1)
    
print_factorial(factorial_recursive)

# generator implementation
def factorial_generator(num):
    result = 1
    
    for n in range(result, num+1):
        result *= n
        yield result

print '=' * 50
    
for i, x in enumerate(factorial_generator(6)):
    print 'factorial_generator {0}:'.format(i), x

# one-liner (lambda) implementation
factorial_one_lambda = lambda num: reduce(lambda x,y: x*y, range(1, num+1), num+1)

print_factorial(factorial_one_lambda)