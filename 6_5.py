class Class1:
    def __init__(self,atr1 , atr2):
        self.atr1= atr1
        self.atr12= atr2

    def meth(self,obj):
        obj.atr1 = 1
        obj.atr2 = 1
        return obj

class Class2:
    def __init__(self,atr1 , atr2):
        self.atr1= atr1
        self.atr2= atr2

obj1 = Class1(1,2)
obj2 = Class2(3,4)
obj1.meth(obj2)
print(obj2.__dict__)
