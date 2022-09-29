class A:
    def f(self):
        return "A"


class B:
    def g(self):
        return "B"


class Child(A, B):
    pass


child = Child()
print(child.f(), child.g())
print(Child.mro())
