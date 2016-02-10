"""
Created on Dec 1, 2015

@author: francisparan
"""

from sys import modules

import namespaces2


def example(example_name):
    print('{0}\nExample {1}\n{0}'.format('=' * 10, example_name))


example('1')
# ----------- global
a_var = 'global value'


def a_func():
    # ----------- local
    a_var = 'local value'
    print '[ a_var inside a_func() ]', a_var

a_func()
print '[ a_var outside a_func() ]', a_var


example('2')
a_var = 'global value'


def a_func2():
    # a_var refers to the a_var 
    # within global namespace.
    global a_var
    a_var += '+local value'

    print '[ a_var inside a_func2() ]', a_var

print '[ a_var outside a_func2() ]', a_var
a_func2()
print '[ a_var outside a_func2() ]', a_var


example('3')
a_var = 'global value'


def a_func3():
    # Variable assignment for a_var here is evaluated 
    # from left to right (i.e., a_var = a_var + '+local value').
    # a_var is not defined within local namespace.
    a_var += '+local value'
    print a_var, '[ a_var inside a_func3() ]'

print a_var, '[ a_var outside a_func3() ]'
# a_func3() # will raise UnboundLocalError
print a_var, '[ a_var outside a_func3() ]'


example('4')
#----------- global
a_var = 'global value'

def outer():
    #----------- enclosed
    a_var = 'enclosed value'
    
    def inner():
        #----------- local
        a_var = 'local value'
        print a_var
    
    # inner() will print a_var defined 
    # within the local namespace.
    inner()

    # prints a_var defined within this enclosed namespace.
    print a_var

outer()

example('5')

a_var = 'global variable'

print globals()
print 'a_var in globals()?', 'a_var' in globals()

# call to the built-in len()
print 'built-in len():', len(a_var)


# len here is redefinition of the built-in len function
def len(in_var):
    print 'called my len() function'
    l = 0
    for i in in_var:
        l += 1
    return l


def a_func4(in_var):
    # Since the namespace search order is
    # L->E->G->B, finding len within the enclosing
    # namespace will make use of it in this call
    # rather than the built-in one.
    len_in_var = len(in_var)
    print 'Input variable is of length', len_in_var

a_func4('Hello, World!')


example('6')
a = 'global'

# globals(): ['a']
# locals(): ['a']


def outer2():

    def len(in_var):
        print 'called my len() function'
        l = 0
        for i in in_var:
            l += 1
        return l
    a = 'local'

    d = {'a': a}

    def inner():
        # This function block is enclosed by the
        # outer2's block above it where len has
        # been defined.
        print 'inner', len(d)

        # locals(): ['d']
        d['a'] += ' variable'

    inner()

    a = d['a']

    print 'a is', a
    print 'outer', len(a)

outer2()

print len(a)
print 'a is', a

print '=' * 50

print 'printing class A from', namespaces2.__name__

obj = namespaces2.A()

print 'obj.a:', obj.a

# obj.a & a below are bound to two separate namespaces.
# The former is bound to the class defined in the imported
# module, whereas the latter is bound to this module's
# namespace.
obj.a = 5

# new variable a, not the same as obj.a
a = 7

print 'obj.a:', obj.a
print 'new variable a:', a

print 'namespaces2' in modules
