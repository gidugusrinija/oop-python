class A(object):
    instance = None

    def __new__(cls):
        print("Entered __new__")
        if not cls.instance:
            print("Instance Creating...")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __eq__(self, other):
        return id(self) == id(other)


a1 = A()
b1 = A()

print(a1.__eq__(b1))
