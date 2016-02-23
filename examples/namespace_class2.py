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


class PartyGoer:
    count = 0
    __shared_state = {}
    greet = True

    def __init__(self, name):
        # self.__dict__ = self.__shared_state
        self.name = name
        self.__class__.greet = True  # self.greet = True
        self.__class__.count += 1  # self.count += 1

    def __del__(self):
        self.__class__.count -= 1  # self.count -= 1

    def message(self):

        if self.count > 1:
            if not self.greet:
                return 'blah blah blah'

            self.__class__.greet = False # self.greet = False
            return 'Hey, we have a guest. LET PARTY!!!'
        elif self.__class__.greet:
            return "Looks like I\'m the first one here."
        return "-_-"

    def __str__(self):
        return "{}: {}".format(self.name, self.message())


def foo_example():
    samp1 = Foo()
    samp2 = Foo()

    print 'samp1: {}, samp2: {}'.format(samp1, samp2)

    # The objects aren't the same,
    print samp1 is samp2

    # but their namespaces are.
    print samp1.__dict__ is samp2.__dict__

    # We declare an instance attribute x in samp1.
    # x will be defined and stored in its shared namespace.
    samp1.x = 1

    # samp2 also has this attribute, since both samp1 and samp2 share the same namespace.
    print samp2.x
    print samp1.x is samp2.x

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


def party_goer_example():
    francis = PartyGoer("Francis")

    print 'Francis:', francis

    mj = PartyGoer("MJ")

    print(francis)
    print('{}, {}'.format(mj, francis))

    chloe = PartyGoer("Chloe")
    print('{}, {}'.format(mj, francis))

    del chloe
    print(francis)

    del mj
    print(francis)

if __name__ == '__main__':
    # foo_example()
    party_goer_example()
