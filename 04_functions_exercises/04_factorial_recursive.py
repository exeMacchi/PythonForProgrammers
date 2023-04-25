# 4) Define a function called factorial that computes the factorial of a number 
#    using recursion.
def main():
    user_number = ask_number()
    print(f"# The factorial of {user_number} is {factorial(user_number)}")


def ask_number():
    while True:
        try:
            user_number = int( input("4) Enter a number: ") )
        except:
            print("Error: non-numeric value.")
        else:
            return user_number


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    main()
