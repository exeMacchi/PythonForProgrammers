# 4) Create a program that asks the user for a list of numbers and determines 
#    how many numbers in the list are even and how many are odd. If the user 
#    enters a non-numeric value, the program should display an error message and 
#    ask the user to enter a valid value.
def main():
    while True:
        try:
            length = int ( input("4) Enter the amount of numbers for the list: "))
        except:
            print("Error: non-numeric value.")
        else:
            if length > 0:
                break
            else:
                print("Error: the number must be greater than 0.")
    
    numbers = list()
    count_of_even_numbers = 0
    count_of_odd_numbers = 0
    i = 0
    while i < length:
        try:
            number = int( input(f"{i + 1}. Enter a number: ") )
        except:
            print("Error: non-numeric value.")
        else:
            numbers.append(number)
            if number % 2 == 0:
                count_of_even_numbers += 1
            else:
                count_of_odd_numbers += 1
            i += 1
    
    print(f"# {numbers}")
    print(f"# Count of even numbers: {count_of_even_numbers}")
    print(f"# Count of odd numbers: {count_of_odd_numbers}")

if __name__ == '__main__':
    main()
