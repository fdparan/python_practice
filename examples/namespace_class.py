
class Foo:
    class_attr = 2

    def __init__(self, x):
        self.instance_attr = x

first = Foo(4)
second = Foo(10)

print '-' * 50, "\nClass Foo\n", '-' * 50
print "first:", first.class_attr, first.instance_attr
print "second:", second.class_attr, second.instance_attr

# Class attribute class_attr is accessible either by using the dot operator from the class name,
print "class attribute 'class_attr':", Foo.class_attr

# or through class instances.
print "class_attr through first instance:", first.class_attr
print "class_attr through second instance:", second.class_attr

# This will change the value of class_attr ONLY for the instance variable first.
first.class_attr = 5

print "class attribute 'class_attr':", Foo.class_attr

print "class_attr through first instance:", first.class_attr
print "class_attr through second instance:", second.class_attr

# Checking namespaces of the instances, we can see that first has
# class_attr defined in it while second doesn't have one.
print 'Checking namespaces'

print 'first:', first.__dict__.has_key('class_attr') # class_attr here is instance attribute for first
print 'second:', second.__dict__.has_key('class_attr')

# Despite that, both first & second still refer to the same
# class __dict__ that holds namespace for class_attr.
print first.__class__.__dict__ is second.__class__.__dict__

# So, this is perfectly legal
del first.class_attr # This deletes instance attribute class_attr from first
print 'first:', first.__dict__.has_key('class_attr')


# If default value for a class attribute is defined as a mutable type (e.g., a list),
# then any instance of that class can change its value.

class Bar:
    class_attr = []

    def __init__(self, x):
        self.x = x

first = Bar(4)
second = Bar(10)

print '-' * 50, "\nClass Bar\n", '-' * 50
print "class attribute 'class_attr':", Bar.class_attr

# You can also call it through instances
print "class_attr through first instance:", first.class_attr
print "class_attr through second instance:", second.class_attr

first.class_attr.append('bar')
first.class_attr.append('blah')
print "class attribute 'class_attr':", Bar.class_attr

second.class_attr.append('spam')
print "class attribute 'class_attr':", Bar.class_attr

# You could wind up having the mutable class attribute deleted by accident

# del first.class_attr
# # raises "AttributeError: Bar instance has no attribute 'class_attr'"
# print "class attribute 'class_attr':", Bar.class_attr

# You can prevent this by either having that attribute defined as part of the
# instance (i.e., define it in __init__), instead of defining it in the class
# namespace, or set the class attribute to an immutable value like None.


print '-' * 50, "\nClass Spam\n", '-' * 50


class Spam:
    __non_public_attr = []

    def __init__(self, inst_attr):
        self.inst_attr = inst_attr

first = Spam(4)
second = Spam(10)

print 'Checking namespaces'

print 'first:', first.__class__.__dict__.has_key('__non_public_attr')
print 'second:', second.__class__.__dict__.has_key('__non_public_attr')

# Let's check out the class namespace
print 'Spam:', Spam.__dict__

# So, it's _Spam__non_public_attr
print 'first:', first.__class__.__dict__.has_key('_Spam__non_public_attr')
print 'second:', second.__class__.__dict__.has_key('_Spam__non_public_attr')
