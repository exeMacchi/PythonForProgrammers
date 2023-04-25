def rectangle_sides():
    while True:
        try:
            height = float(input("# Enter the height of the rectangle: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if height > 0:
                break
            else:
                print("The height must be greater than 0.")

    while True:
        try:
            base = float(input("# Enter the base of the rectangle: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if base > 0:
                break
            else:
                print("The base must be greater than 0.")
    
    return height, height, base, base


def triangle_sides():
    while True:
        try:
            side_A = float(input("# Enter the first side of the triangle: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if side_A > 0:
                break
            else:
                print("The side must be greater than 0.")

    while True:
        try:
            side_B = float(input("# Enter the second side of the triangle: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if side_B > 0:
                break
            else:
                print("The side must be greater than 0.")

    while True:
        try:
            side_C = float(input("# Enter the third side of the triangle: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if side_C > 0:
                break
            else:
                print("The side must be greater than 0.")

    return side_A, side_B, side_C
