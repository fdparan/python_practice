from math import *
from pprint import pprint

user_func = raw_input("type a function: y = ")

for x in range(1,10):
    print "x = ", x , ", y = ", eval(user_func,{})