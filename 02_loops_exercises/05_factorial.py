# 5) Create a program that asks the user for a number and calculates its factorial.
def main():
    while True:
        user_number = int( input("5) Enter a positive integrer: ") )
        if user_number >= 0:
            break
    
    result = 1
    for n in range(user_number, 0, -1):
        result *= n
    
    print(f"The factorial of {user_number} is {result}")

if __name__ == '__main__':
    main()
