class MyClass:
    counter = 0
    def __init__(self):
        MyClass.counter += 1

    def getInstanceCount(self):
         return MyClass.counter


class1 = MyClass()
class2 = MyClass()
class3 = MyClass()
class4 = MyClass()
class5 = MyClass()
class6 = MyClass()
class7 = MyClass()
class8 = MyClass()
class9 = MyClass()

print(MyClass.counter)