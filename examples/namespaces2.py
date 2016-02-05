"""
Created on Dec 1, 2015
 
@author: francisparan
"""


import pprint


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
        global len
        print 'Globals:', filter(lambda x: not x.startswith('_') , globals())
        print 'Locals:', filter(lambda x: not x.startswith('_') , locals())
        
        d['a'] += ' variable'
        
    inner()
    
    a = d['a']
    
    print 'a is', a
    print len(a)


class A:
    a = 42

    # The 'a' in the list comprehension assignment of b here
    # refers to the global a. Names defined in a class block
    # don't extend to the code blocks of methods, since they
    # are implemented using a function scope. This will fail.
    # b = list(a + i for i in range(10))

if __name__ == '__main__':
    print '''
    ===============================================================================
     Example
    ===============================================================================
    '''

    a = 'global'

    print 'Globals:', filter(lambda x: not x.startswith('_') , globals())
    print 'Locals:', filter(lambda x: not x.startswith('_') , locals())
    print type(globals())

    outer2()

    print len(a)
    print 'a is', a

    print 'Globals:', filter(lambda x: not x.startswith('_') , globals())
    print 'Locals:', filter(lambda x: not x.startswith('_') , locals())

    samp = globals()

    print '\npprint in samp referring to samp:', 'pprint' in samp

    print '\npprint in samp referring to globals():', 'pprint' in globals()
