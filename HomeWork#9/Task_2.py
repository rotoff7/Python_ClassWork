# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)


class MyMetaClass(type):

    def __init__(cls, *args, **kwargs):
        cls.a = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.a == None:
            cls.a = super().__call__(*args, **kwargs)
            cls.a = cls.a = super().__call__(*args, **kwargs)
            return cls.a
        else:
            return cls.a


class MyClass(metaclass=MyMetaClass):

    def method_1(self):
        pass


obj1 = MyClass()
obj2 = MyClass()

print(type(obj1))
print(type(obj2))
print(obj1 == obj2)
print(obj1 is obj2)
