"""
Created on Oct 3, 2015

@author: francisparan
"""

import functools


# A wrapper/decorator is a function that takes another
# function as an argument, and returns it in a replacement function.
def decorate(func):
    def inner():
        print 'We\'re calling the function from here!'
        
        return func()
    return inner

@decorate
def foo():
    return 'bar'
    
print foo()

# Wrapper function wrap takes a
# variable number of positional arguments,
# which are in this case functions.
def wrap(*fs):
    def inner(x):
        result = x
        for f in fs:
            result = f(result)
            print('%s: %d' %(f.__name__, result))
            
        return  result # reduce((lambda class_attr, z: class_attr(z)), fs, instance_attr)
    return inner

BACK_CALL = False

# A more concise way of implementing functon composition using reduce
def function_composition(*function_list):
    return reduce(lambda y, z: lambda x: y(z(x)), function_list)

def call_forth(g):
    def inner(func):
        def call(*args,**kwargs):
            return func(*args, **kwargs) if not BACK_CALL else g(func(*args, **kwargs))
        return call
    return inner

def a(x = None):
    return x + 5

@call_forth(a)
def b(x = None):
    return x + 7

@call_forth(b)
def c(x = None):
    return x - 9

@call_forth(c)
def d(x = None):
    return x + 2


def code_portion(msg = ''):
    print '*' * 50
    print msg

func = function_composition(a,b,c,d)
print(func(3))

func = d
print(func(3))

code_portion()


def func(arg1, arg2=foo()):
    print 'Entering func1'

    # The default argument for inner_func gets assigned
    # a value at the moment this def is created at compiletime.
    def inner_func(arg3=arg2):
        # arg3 will have whatever arg2 was at that time, not whatever
        # it is the moment you call inner_func.

        print 'entering inner_func'
        return arg1, arg3

    arg1 = arg2 = None

    return inner_func

print func('spam')()

code_portion('Now, using functools.wraps to wrap a function')


def my_decorator(f):

    @functools.wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print 'Called example function'

example()

# Without the use of functools.wraps, the name of the example function would have been 'wrapper'
print 'Function "{}": {}'.format(example.__name__, example.__doc__)

code_portion('Multiple decorators')


def makebold(fn):
    return getwrapped(fn, "b")


def makeitalic(fn):
    return getwrapped(fn, "i")


def getwrapped(fn, tag):
    @functools.wraps(fn)
    def wrapped():
        return "<%s>%s</%s>" % (tag, fn(), tag)
    return wrapped


# wrapping of decorators for a function starts from the bottom all the way up
@makebold
@makeitalic
def hello():
    """a decorated hello world"""
    return "hello world"

if __name__ == '__main__':
    print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))