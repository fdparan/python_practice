# NOTE: __dict__ is a dictionary attribute that contains the mapping of
# names and values defined in the namespace of a class instance.


class Foo:

    __shared_state = {}
    count = 0

    def __init__(self, state="Init"):

        # Assigning __dict__ to another dict defined at the class level means that all
        # instances of the class will share the same namespace.
        self.__dict__ = self.__shared_state
        self.state = state
        self.count += 1

    def __str__(self):
        return self.state


class Bar(Foo):
    pass

samp1 = Foo(); samp2 = Foo()

print 'samp1: {}, samp2: {}'.format(samp1, samp2)

# The objects aren't the same,
print samp1 is samp2

# but their namespaces are.
print samp1.__dict__ is samp2.__dict__

# We declare an instance attribute x in samp1.
# x is defined and stored in __dict__.
samp1.x = 1

# samp2 also has this attribute, since both samp1 and samp2 share the same namespace.
print samp1.x, samp2.x

# sampBar1 is an instance of class Bar, which inherits from Foo.
sampBar1 = Bar()

print 'sampBar1: {}'.format(sampBar1)

# Since sampBar1 is of class Bar that inherits from Foo, it also inherits Foo's namespace.
# Changing its state changes for the existing instances of the parent and child classes
# that all share the same namespace (i.e., __dict__).
sampBar1.state = 'Running'

print 'samp1: {}, samp2: {}'.format(samp1, samp2)
print 'sampBar1: {}'.format(sampBar1)


sampBar2 = Bar()
print 'sampBar2: {}'.format(sampBar2)

print 'samp1: {}, samp2: {}'.format(samp1, samp2)
print 'sampBar1: {}'.format(sampBar1)

print sampBar1.count


class PartyGoer:
    count = 0
    __shared_state = {}
    greet = True

    def __init__(self):
        # self.__dict__ = self.__shared_state
        self.__class__.greet = True  # self.greet = True
        self.__class__.count += 1  # self.count += 1

    def __del__(self):
        self.__class__.count -= 1  # self.count -= 1

    def chat_around(self):

        if self.count > 1:
            if not self.greet:
                return 'blah blah blah'

            self.__class__.greet = False # self.greet = False
            return 'Hey we have a new visitor, LET PARTY!!!'

        else:
            return 'Looks like I\'m the first one here'

    def __str__(self):
        return self.chat_around()

francis = PartyGoer()

print 'Francis:', francis

mj = PartyGoer()

print 'Francis:',francis
print 'MJ: {}, Francis: {}'.format(mj, francis)

chloe = PartyGoer()
print 'MJ: {}, Francis: {}'.format(mj, francis)

del chloe
print 'Francis:', francis

del mj
print 'Francis:', francis

