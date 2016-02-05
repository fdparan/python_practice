# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:06:23 2015

@author: francisparan
"""

import pickle


class foo():

    def __init__(self, msg = ''):
        self.msg = msg
    
    def get_msg(self):
        return self.msg

obj = foo('bar')

marco = obj

print marco.get_msg()

marco.msg = 'polo!'
print marco.get_msg()

print '=== %s ===' %'Pickling object to samp.txt - use pickle.dump'

pickle.dump(marco, open('samp.txt', 'w'), protocol = 1)

print '''
===================================================================
 pickle protocols
 0 - default
 1 - old binary format, compatible with earlier versions of Python.
 2 - pickle.HIGHEST_PROTOCOL, from Python 2.3 onwards
===================================================================
'''

print '=== %s ===' % 'Unpickling object from samp.txt - use pickle.load'

loaded_obj = pickle.load(open('samp.txt', 'r'))

print loaded_obj.get_msg()


print '=== %s ===' % 'Pickling object to console - use pickle.dumps'

print pickle.dumps(marco, protocol = pickle.HIGHEST_PROTOCOL)

print '=== %s ===' % 'Unpickling object from  - use pickle.loads'

pickled_obj = pickle.dumps(marco, protocol = pickle.HIGHEST_PROTOCOL)

print pickle.loads(pickled_obj).get_msg()