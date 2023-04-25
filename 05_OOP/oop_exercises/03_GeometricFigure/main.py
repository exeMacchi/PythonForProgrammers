# 3) Create a class called "GeometricFigure" that has attributes "side1", 
#    "side2", and "side3". Add methods to calculate the perimeter and area of 
#    the figure. Then, create two child classes called "Triangle" and "Rectangle" 
#    that inherit from "GeometricFigure". In the "Triangle" class, add a method 
#    to calculate the area using Heron's formula. In the "Rectangle" class, add 
#    a method to calculate the area using the multiplication of the sides. 
#    Finally, create objects of type "Triangle" and "Rectangle" and display the 
#    perimeter and area of each one in the console.
from geometric_figure import Triangle, Rectangle
from functions import rectangle_sides, triangle_sides


def main():
    triangle = Triangle(*triangle_sides())
    print()
    rectangle = Rectangle(*rectangle_sides())

    print("================================")
    print(f"Perimeter of the triangle: {triangle.calculate_perimeter()}")
    print(f"Area of the triangle: {round(triangle.calculate_area(), 2)}")
    print("================================")
    print(f"Perimeter of the rectangle: {rectangle.calculate_perimeter()}")
    print(f"Area of the rectangle: {rectangle.calculate_area()}")
    print("================================")


if __name__ == '__main__':
    main()
