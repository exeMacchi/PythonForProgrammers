# 8) Create a program that asks the user for a list of numbers and removes all 
#    duplicate numbers.
def main():
    while True:
        length = int( input("8) Enter the amount of numbers from the list: "))
        if length > 0:
            break
    
    numbers = list()
    for i in range(length):
        numbers.append( int( input(f"{i + 1}. Enter a number: ") ) )
    
    unduplicated_numbers = list()
    for number in numbers:
        duplicate = 0
        for n in numbers:
            if number == n:
                duplicate += 1
        if duplicate < 2:
            unduplicated_numbers.append(number)
    
    print(f"List of numbers without duplicates: {unduplicated_numbers}")

if __name__ == '__main__':
    main()
