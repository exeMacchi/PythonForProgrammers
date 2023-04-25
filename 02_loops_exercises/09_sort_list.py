# 9) Create a program that asks the user for a list of numbers and sorts them 
#    from smallest to largest.
def main():
    while True:
        length = int( input("9) Enter the amount of numbers from the list: "))
        if length > 0:
            break
    
    numbers = list()
    for i in range(length):
        numbers.append( int( input(f"{i + 1}. Enter a number: ") ) )
    print(f"Not sorted list: {numbers}")


    while True:
        sorted = True
        for i in range(length - 1):
            if numbers[i + 1] < numbers[i]:
                aux = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = aux
                sorted = False
        if sorted:
            break
    print(f"Sorted list: {numbers}")

if __name__ == '__main__':
    main()
