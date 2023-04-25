# 2) Create a program that asks the user for a number and determines whether it 
#    is prime or not.
def main():
    while True:
        user_number = int( input("2) Enter a positive integer (other than 1): ") )
        if user_number > 1:
            break

    for n in range(2, user_number):
        if user_number % n == 0:
            print(f"{user_number} is not prime.")
            break
    else:
        print(f"{user_number} is prime.")

if __name__ == '__main__':
    main()
