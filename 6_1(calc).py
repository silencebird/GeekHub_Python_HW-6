class Calc:
    last_result = None

    def sum(self,a,b):
        self.last_result = a+b
        return self.last_result

    def destract(self,a,b):
        self.last_result = a-b
        return self.last_result

    def multip(self,a,b):
        self.last_result = a*b
        return self.last_result

    def devision(self,a,b):
        self.last_result = a/b
        return self.last_result


calc = Calc()
print(calc.last_result)
calc.sum(45,56)
calc.destract(2,1)
print(calc.last_result)

"""
try:
    calc.devision(3,0)
except:
    print "Oops! Zero devision. Try again..."
"""