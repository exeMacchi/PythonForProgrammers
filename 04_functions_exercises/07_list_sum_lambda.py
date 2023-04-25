# 7) Define a lambda function that takes a list of numbers as argument and 
#    returns the sum of all the numbers in the list.
def main():
    length = ask_length()

    numbers = list()
    for i in range(length):
        numbers.append(ask_number(i + 1))
    
    list_sum = lambda lista: sum(numero for numero in lista)
    print(f"The sum of the numbers in the list {list_sum(numbers)}")


def ask_length():
    while True:
        try:
            length = int ( input("7) Enter the amount of numbers for the list: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if length > 0:
                return length
            else:
                print("Error: the number must be greater than 0.") 


def ask_number(i):
    while True:
        try:
            number = int( input(f"{i}. Enter an integer number: ") )
        except:
            print("Error: non-numeric value.")
        else:
            return number


if __name__ == '__main__':
    main()
