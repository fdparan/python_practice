'''
Created on Dec 5, 2015
This script demonstrates the use of closures in Python.
@author: francisparan
'''


# A closure is a function that returns a fuunction object.
def generate_power_func(n):

    # n is defined within this function block.
    # We print the id of n.
    print "id(n): %X" % id(n)

    def nth_power(x):

        # The n referenced here is our n above in the
        # the enclosing namespace.
        return x**n

    # We print the id of nth_power.
    print "id(nth_power): %instance_attr" % id(nth_power)

    # nth_power returned here is a function object that
    # still remembers/retains values in enclosing scopes.
    return nth_power

raised_to_4 = generate_power_func(4)

# This should print out the function object
# for nth_power and its id.
print raised_to_4

del generate_power_func

# Even with generate_power_func deleted,
# raised_to_4 can still return a value
# based on generate_power_func's implementation.
print raised_to_4(2)

print raised_to_4.func_closure[0].cell_contents


def to_log(msg="blah"):

    def wrapped(func):

        print 'wrapped call'

        def inner(*args, **kwargs):

            print 'inner call'

            print msg, func.__name__

            return func(*args, **kwargs)

        print "id(inner): %instance_attr" % id(inner)

        return inner

    return wrapped


@to_log("spam")
def foo():
    return "bar"

f = foo

print f, f.func_closure[-1].cell_contents

print f()


def greeter():
    print "Hello"


def print_call(fn):

    def fn_wrap(*args, **kwargs): #take any arguments

        print "Calling %s" % fn.func_name
        return fn(*args, **kwargs) #pass any arguments to fn()

    # We would most likely want to keep the original name of the function
    fn_wrap.func_name = fn.func_name

    return fn_wrap

f = print_call(greeter)

print 'f() is', f

f()
