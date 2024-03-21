class Point:
    __instance = None   # __private, only inside a class
    __private_attr = 48  # __private can be access by _Point__private_attr reference. DON'T DO THIS!
    _middle = 50    # _protected, all siblings
    MIN_COORD = 0   # public, everywhere
    MAX_COORD = 100

    @classmethod  # can work with class fields only and with cls variable. Can't change self instances.
    def __validate(cls, arg) -> bool:  # __method means private method. Have access by self reference in class code
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod   # fully independent method without self or cls references. Can be accessed within class also
    def norm2(x, y) -> float:
        return x * x + y * y    # can access Point.MIN_COORD too, but is not recommended

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):  # cls - reference to a class Point. Arguments are mandatory
        print("Call __new__ method first")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # all classes extend basic class Object
        return cls.__instance

    def __init__(self, x=0, y=0):
        print("Call __init__ method after __new__")
        self._x = self._y = 0
        if self.__validate(x) and self.__validate(y):  # self knows about @classmethods as well
            self._x = x
            self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    def __del__(self):
        Point.__instance = None


point = Point(1, 20)
print(point._x, point._y)  # protected still can be accessed, but it is not recommended!
# print(point.__private_attr)  # will cause an error, because private vars can't be accessed directly
point.x = 44    # use property setter here
print(point.x)  # use property getter here
