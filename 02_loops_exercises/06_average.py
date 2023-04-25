# 6) Create a program that asks the user for a list of numbers and calculates 
#    their average.
def main():
    while True:
        length = int( input("Enter the amount of numbers from the list: "))
        if length > 0:
            break
    
    numbers = list()
    accumulative_sum = 0
    for i in range(length):
        numbers.append( int( input(f"{i + 1}. Enter a number: ") ) )
        accumulative_sum += numbers[i]
    
    average = accumulative_sum / length
    print(f"The average number of numbers in the list is {average}")

if __name__ == '__main__':
    main()
