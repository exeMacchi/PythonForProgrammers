# 2) Define a function called is_even that takes a number as argument and returns 
#    True if the number is even and False if the number is odd.
def main():
    user_number = ask_number()
    if is_even(user_number):
        print(f"# {user_number} is even.")
    else:
        print(f"# {user_number} is odd.")


def ask_number():
    while True:
        try:
            user_number = int( input("2) Enter a number: ") )
        except:
            print("Error: non-numeric value.")
        else:
            return user_number


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
