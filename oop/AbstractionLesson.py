# abstraction and polymorphism

class Figure:

    def get_perimeter(self):  # force user to implement method in subclasses. there are no abstract methods in Python
        raise NotImplementedError("Implement method in subclass!!!")


class Rectangle(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self) -> float:
        return 2 * (self.w + self.h)


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self) -> float:
        return 4 * self.a


