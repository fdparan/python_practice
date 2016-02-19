"""
Created on Dec 1, 2015

@author: francisparan
"""

from sys import modules

import namespaces2


def example(example_name):
    print('\n{0}\nExample {1}\n{0}'.format('=' * 10, example_name))


def print_func_name(func):

    def inner(*args, **kwargs):
        print "\n**\nFunction {}: ".format(func.func_name)
        result = func(*args, **kwargs)
        print "**\n"
        return result
    return inner


def print_namespace(namespace):
    print 'Local namespace:', namespace.keys()


example('1')
# ----------- global
a_var = 'global value'

print_namespace(locals())

@print_func_name
def a_func():
    # ----------- local variable here "masking" a_var in the outside scope
    a_var = 'local value'
    print '[ a_var inside a_func() ]', a_var
    print_namespace(locals())

a_func()

print '[ a_var outside a_func() ]', a_var
print_namespace(locals())


example('2')
a_var = 'global value'


@print_func_name
def a_func2():
    # use global to refer to a_var
    # in the outside scope.
    global a_var
    a_var += ' + local value'

    print '[ a_var inside a_func2() ]', a_var
    print_namespace(locals())  # a_var from globals should not show up in here


print '[ a_var outside a_func2() ]', a_var  # global value

a_func2()
print '[ a_var outside a_func2() ]', a_var  # global value + local value


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


example('4')
#----------- global
a_var = 'global value'


@print_func_name
def outer():
    #----------- enclosed
    a_var = 'enclosed value'

    @print_func_name
    def inner():
        #----------- local
        a_var = 'local value'
        print a_var
        print_namespace(locals())
    
    # inner() will print a_var defined 
    # within the local namespace.
    inner()

    # prints a_var defined within this enclosed namespace.
    print a_var
    print_namespace(locals())

outer()


example('5')

a_var = 'global variable'

print globals().keys()
print 'a_var in globals()?', 'a_var' in globals()

# call to len in __builtins__
print 'built-in len:', len(a_var)


# len here is redefinition of the built-in len function
@print_func_name
def len(in_var):
    print 'called my len() function'
    l = 0
    for i in in_var:
        l += 1
    print_namespace(locals())
    in_var += 'foo'  # This update won't affect the argument passed into this function
    return l


@print_func_name
def a_func4(in_var):
    # Since the namespace search order is
    # L->E->G->B, finding len within the enclosing
    # namespace will make use of it in this call
    # rather than the built-in one.
    len_in_var = len(in_var)
    print 'Input variable is of length', len_in_var
    print_namespace(locals())
    print in_var

samp = 'Hello, World!'
a_func4(samp)


example('6')
a = 'global'

# globals(): ['a']
# locals(): ['a']


@print_func_name
def outer2():

    @print_func_name
    def len(in_var):
        print 'called my len() function #2'
        l = 0
        for i in in_var:
            l += 1
        return l

    a = 'local'
    d = {'a': a}

    # True, both refer to the same string value in memory
    print d['a'] is a

    @print_func_name
    def inner():
        # This function block is enclosed by the
        # outer2's block above it where len has
        # been defined.
        print 'inner', len(d)

        # d['a'] = "local variable", a = "local"
        d['a'] += ' variable'
        print_namespace(locals())

    print_namespace(locals())
    inner()

    a = d['a']

    print 'a is', a
    print 'outer', len(a)

    print_namespace(locals())

outer2()


example('7')

print len(a)
print 'a is', a

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
