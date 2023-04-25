# 1) Create a program that asks the user for a list of numbers and calculates 
#    their average, but if the user enters a non-numeric value, the program 
#    should display an error message and ask the user to enter a valid value.
def main():
    while True:
        try:
            length = int ( input("1) Enter the amount of numbers for the list: "))
        except:
            print("Error: non-numeric value.")
        else:
            if length > 0:
                break
            else:
                print("Error: the number must be greater than 0.")

    numbers = list()
    acum_sum = 0
    i = 0
    while i < length:
        try:
            numbers.append( int( input(f"{i + 1}. Enter a number: ") ) )
        except:
            print("Error: non-numeric value.")
        else:
            acum_sum += numbers[i]
            i += 1
    
    average = acum_sum / length
    print(f"The average number of numbers in the list is {average}")

if __name__ == '__main__':
    main()
