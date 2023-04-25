# 3) Define a function called calculate_area that takes the radius of a circle 
#    as argument and returns its area. Use the formula area = pi * radius^2, 
#    where pi is a constant equal to 3.14159
import math

def main():
    radius = ask_radius()
    print(f"# The area of the circle is {round(calculate_area(radius), 2)}")


def ask_radius():
    while True:
        try:
            radius = float( input("3) Enter the radius of a circle: ") )
        except:
            print("Error: non-numeric value.")
        else:
            return radius


def calculate_area(radius):
    return math.pi * (radius ** 2)


if __name__ == '__main__':
    main()
