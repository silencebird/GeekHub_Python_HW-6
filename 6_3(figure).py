
class Figure:
    def __init__(self, color="white"):
        self.color = color

    def setColor(self,color):
        self.color = color

class Oval(Figure):
    def __init__(self, centerPoint, xAxis, yAxis):
        super().__init__()
        self.centerPoint = centerPoint
        self.xAxis = xAxis
        self.yAxis = yAxis


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

ellipse = Oval((34,56),34,45)

square = Square(45)

square.setColor("blue")

print(ellipse.__dict__)
print(square.__dict__)
