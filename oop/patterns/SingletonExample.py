class Point:
    __instance = None

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):  # cls - reference to a class Point. Arguments are mandatory
        print("Call __new__ method first")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # all classes extend basic class Object
        return cls.__instance

    def __init__(self, x=0, y=0):
        print("Call __init__ method after __new__")
        self.x = x
        self.y = y

    def __del__(self):
        Point.__instance = None


point = Point(1, 20)
print(point)
point2 = Point(1, 20)
print(point2)
print(id(point2) == id(point))

