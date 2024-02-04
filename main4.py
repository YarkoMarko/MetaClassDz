class InitClass(type):
    def __new__(cls, name, bases, dct):
        def new_init(self, value):
            if value < 50:
                self.value = value

            else:
                self.value = 0

        dct["__init__"] = new_init
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=InitClass):
    value = 0

    def __init__(self, value):
        self.value = value


m = MyClass(20)

print(m.value)

