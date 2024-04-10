class Shape:
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z

class circle(Shape):
    def cir_area(self,l,b,c):
        area= 3.14*l*l
        perimeter=2*3.14*l
        print("the Area of a circle:",area)
        print("the perimeter of a circle",perimeter)

class rectangle(Shape):
    def rec_area(self,l,b,c):
        area= l*b
        perimeter=2*(l+b)
        print("the Area of a rectangle:",area)
        print("the perimeter of a rectangle",perimeter)

class triangle(Shape):
    def tri_area(self,l,b,c):
        area= 0.5*l*b
        perimeter=l+b+c
        print("the Area of a triangle:",area)
        print("the perimeter of a triangle",perimeter)

obj1=triangle(1,2,3)
obj1.tri_area(1,2,3)

obj2=circle(1,2,3)
obj2.cir_area(1,2,3)

obj3=rectangle(1,2,3)
obj3.rec_area(1,2,3)

