# 6) Define a lambda function that takes a number as argument and returns the 
#    number squared.
def main():
    user_number = ask_number()
    squared = lambda n: n ** 2
    print(f"# {user_number} squared is {squared(user_number)}")


def ask_number():
    while True:
        try:
            user_number = int( input("6) Enter a number: ") )
        except Exception as e:
            print(f"Error: {e}")
        else:
            return user_number


if __name__ == '__main__':
    main()
