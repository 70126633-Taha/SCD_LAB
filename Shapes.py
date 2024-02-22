import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area_to_perimeter_ratio(self):
        return self.area() / self.perimeter()


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius

    def area_to_perimeter_ratio(self):
        return self.area() / self.perimeter()

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    # Print details of Rectangle and Circle, including the area-to-perimeter ratio
    print("Rectangle Details:")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    print("Area-to-Perimeter Ratio:", rectangle.area_to_perimeter_ratio())

    print("\nCircle Details:")
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())
    print("Area-to-Perimeter Ratio:", circle.area_to_perimeter_ratio())
