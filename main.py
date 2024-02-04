class MethodChange(type):
    def __new__(cls, name, bases, dct):
        dct["age_print"] = lambda self, age: f"Age: {age}" if 0 < age < 50 else exec('raise(ValueError("Invalid age"))')
        dct["name_printer"] = lambda self, name_of: f"Name: {name_of}" if "A" in name_of or "a" in name_of else exec('raise(ValueError("Invalid name"))')
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MethodChange):
    def age_print(self, age):
        return f"Age: {age}"

    def name_printer(self, name_of):
        return f"Name: {name_of}"


cl = MyClass()

print(cl.age_print(10))
print(cl.name_printer("And"))
