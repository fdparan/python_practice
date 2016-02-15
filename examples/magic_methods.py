
class Foo:
    def __init__(self, value):
        self.bar = value

    def __new__(cls, *args, **kwargs):
        # __new__: gets called usually before __init__
        # but is not used that often
        print('__new__ called for some reason')

    def __del__(self):
        # __del__: to delete some values before garbage
        # collecting this object, not guaranteed to get called
        # especially if the interpreter abruptly quits for
        # some reason. This is NOT to override the del statement.
        print('__del__ called')

    def __str__(self):
        """
        __str__: defines behavior for the instance when a user
        prints it out, such as

            print(obj)
                OR
            obj.__str__()

        :return: str output of the instance
        """

        return self.bar

    def __setattr__(self, name, value):
        """
        __setattr__: overrides the default __setattr__ from
        super, defines behavior when a user assigns an
        attribute to an instance, such as

            self.name = value

        :param name: attribute name
        :param value: attribute value
        :return: nothing
        """

        self.__dict__[name] = value

    def __getattr__(self, name):
        """
        __getattr__: overrides the default __getattr__ from
        super, defines behavior when a user attempts to
        retrieve/get an attribute from an instance, such as
            self.name
        :param name: attribute name
        :return: attribute value
        """

        if name not in self.__dict__:
            print('attr "%s" not defined' % name)
            return ''

        return self.__dict__[name]

if __name__ == '__main__':
    obj = Foo('bar')

    print(obj.__dict__)

    print(obj)

    print(obj.attr1)
    print(obj.bdfl)

    obj.attr1 = 'spam'
    obj.bdfl = 'Guido'

    print(obj.__dict__)
    print(obj.attr1)
    print(obj.bdfl)


