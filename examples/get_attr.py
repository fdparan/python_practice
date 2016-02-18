class Foo(object):
    def __init__(self):
        self.__a = 'a'
        self.b = 'b'
        self.d = 'd'

    def c(self):
        pass


class Bar(Foo):
    def __getattr__(self, name):
        print('This is our fallback option: getting %s' % name)
        return 123456

if __name__ == '__main__':
    t = Bar()
    print 'object variables: %r' % t.__dict__
    print 'object variables: %r' % t.__dict__.keys()
    print t.a
    print t.b
    del t.b
    print t.b
    print t.c
    print getattr(t, 'd')
    print hasattr(t, 'x')