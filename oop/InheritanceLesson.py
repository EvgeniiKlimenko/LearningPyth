class Geometry:  # implicitly extends object class
    name = "Geometry class"

    def __init__(self):
        self.y2 = None
        self.x2 = None
        self.y1 = None
        self.x1 = None

    def set_coordinates(self, x1, y1, x2, y2):  # self - reference to a subclass as well
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        #self.draw()  # here we can call methods of subclasses. But if we call Geometry.set_coordinates(...)
                        # we can catch an exception.

    def override_me(self):
        print("Super class method is called")


class Rectangle(Geometry):
    def draw(self):
        print("Drawing a rectangle...")

    def override_me(self):
        print("Subclass method is called")


class Line(Geometry):
    def draw(self):
        print("Drawing a line...")


geom = Geometry()
geom.set_coordinates(1, 2, 3, 4)  # here we set values for a Geometry object

rect = Rectangle()
rect.set_coordinates(5, 6, 7, 8)  # set values for a Rectangle obj with superclass method
rect.override_me()  # first Python look into subclass, then -> upper in hierarchy(superclass)

