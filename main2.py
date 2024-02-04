class NameChange(type):
    def __new__(cls, name, bases, dct):
        if "attr" in dct.keys():
            name = "Classer"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=NameChange):
    def namer(self):
        return MyClass.__name__


class MyClass1(metaclass=NameChange):
    attr = 10

    def namer(self):
        return MyClass1.__name__


m = MyClass()
n = MyClass1()

print(m.namer())
print(n.namer())
