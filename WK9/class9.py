class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setW(self, w):
        self.width = w

    def setH(self, h):
        self.height = h

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __str__(self):
        return ("Width is : " + str(self.getWidth()) + '\n' + "Height is : " + str(
            self.getHeight()) + '\n' + "Area is : " + str(self.area()) + '\n' + "Perimeter is : " + str(
            self.perimeter()) + '\n')


# r = Rectangle(30, 20)
# r.area()
# r.perimeter()
# print(r)
import random

lst = []
sum = 0
for i in range(20):
    temp = Rectangle()
    temp.setH(random.randint(1, 10))
    temp.setW(random.randint(1, 10))
    lst.append(temp)
    sum += 1

for i in lst:
    print(i)
print(sum)
