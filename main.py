from Shapes import Rectangle, Circle

def print_details(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

if __name__ == "__main__":
    # Instantiate objects of Rectangle and Circle
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    # Demonstrate polymorphism by calling print_details() with instances of both Rectangle and Circle
    print("Rectangle Details:")
    print_details(rectangle)

    print("\nCircle Details:")
    print_details(circle)
