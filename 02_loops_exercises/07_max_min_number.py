# 7) Create a program that asks the user for a list of numbers and determines 
#    which is the largest and smallest number.
def main():
    while True:
        length = int( input("7) Enter the amount of numbers from the list: "))
        if length > 0:
            break
    
    numbers = list()
    for i in range(length):
        numbers.append( int( input(f"{i + 1}. Enter a number: ") ) )
    
    max_number = numbers[0]
    for i in range(length):
        if numbers[i] > max_number:
            max_number = numbers[i]
            
    min_number = numbers[0]
    for i in range(length):
        if numbers[i] < min_number:
            min_number = numbers[i]
    
    print(f"Maximum number: {max_number}")
    print(f"Minimum number: {min_number}")

if __name__ == '__main__':
    main()
