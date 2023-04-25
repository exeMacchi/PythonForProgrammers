# 3) Create a program that asks the user for a number and determines if it is a 
#    perfect number. If the user enters a non-integer value or a negative 
#    number, the program should display an error message and ask the user to 
#    enter a valid value.
def main():
    while True:
        try:
            user_number = int( input("3) Enter a positive integrer: ") )
        except:
            print("Error: non-numeric value.")
        else:
            if user_number > 0:
                break
            else:
                print("Error: the number must be greater than 0.")
    
    dividers = [divider for divider in range(1, user_number) if user_number % divider == 0]
    print(f"Dividers: {dividers}")
    
    dividers_sum = sum(divider for divider in dividers)
    
    if user_number == dividers_sum:
        print(f"# {user_number} is a perfect number.")
    else:
        print(f"# {user_number} is not a perfect number.")

if __name__ == '__main__':
    main()
