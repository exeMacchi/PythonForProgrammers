# 1) Define a function called multiply_numbers that takes two numbers as arguments 
#    and returns their product.
def main():
    user_number_one = ask_number(1)
    user_number_two = ask_number(2)

    print(f"# {user_number_one} * {user_number_two} = " +
          f"{multiply_numbers(user_number_one, user_number_two)}")


def multiply_numbers(num1, num2):
    return num1 * num2


def ask_number(n):
    while True:
        try:
            if n == 1:
                user_number = int( input("1) a) Enter the first number: ") )
            elif n == 2:
                user_number = int( input("1) b) Enter the second number: ") )
            else:
                return 0
        except:
            print("Error: non-numeric value.")
        else:
            return user_number


if __name__ == '__main__':
    main()
