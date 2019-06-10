
class classTest:

    name = 2

    def __init__(self):
        self.name = 4



    def f(x):
        return x*2

    def f2(self):
        return self.name



a = classTest()

print(classTest.f(4))