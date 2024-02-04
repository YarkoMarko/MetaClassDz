class AttrAdder(type):
    def __new__(cls, name, bases, dct):
        dct["attr"] = 10
        dct["attr_print"] = lambda self: dct["attr"]
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AttrAdder):
    pass


obj = MyClass()

print(obj.attr_print())