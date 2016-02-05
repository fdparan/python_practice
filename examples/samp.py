# class parent:
#  def __init__(self, param):
#    self.v1 = param
#
# class child(parent):
#  def __init__(self, param):
#    parent.__init__(self,param)
#    self.v2 = param
#
# obj = child(11)
# print "%d %d" % (obj.v1, obj.v2)
#
# matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
#
# print zip(*matrix)
#
# samp = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del samp['Name']
# samp.clear();
# print samp


x = 0

print globals()


def foo():
    global x
    print x, locals()

foo()
print locals()


def make_contains_function(char):
    def contains(s):
        return char in s
    return contains

print 'assigning contains_a to make_contains_function'
contains_a = make_contains_function('a')

print 'calling contains_a:', contains_a('cat')
