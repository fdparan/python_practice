"""
Created on Nov 22, 2015

@author: francisparan
"""

MEMO = {}


def _add_to_memo(arg_key, func_value):
    MEMO[arg_key] = func_value


def memoize(f):
    
    def inner(*args, **kwargs):
        
        print "Tuple args: ", args
        print "Keyword args: ", kwargs
        
        argv = args + tuple(kwargs.items())
        
        if argv in MEMO:
            print "Retrieving from MEMO"
            return MEMO[argv]
          
        print "Adding arguments to MEMO for the first time:", argv
        result = f(*args, **kwargs)
    
        _add_to_memo(argv, result)
        
        return  result
    return inner


@memoize
def foo(x, y):
    return x + y


@memoize
def bar(x,y, **kwargs):
    return x**y 

if __name__ == '__main__':
    
    memo_msg = "\nMemo: {}\n"
    
    print memo_msg.format(MEMO)

    print foo(1,1)
    print memo_msg.format(MEMO)
    print foo(1,1)

    print foo(2,3)
    print memo_msg.format(MEMO)
    print foo(2,3)
    
    print bar(2, 3, samp="spam")
    print bar(2, 3, samp="monty")
    print bar(2, 3, samp="monty") 
    print memo_msg.format(MEMO)
