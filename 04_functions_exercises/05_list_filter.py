# 5) Define a function called list_filter that takes a list of integers and a 
#    prime number filter function as arguments. The prime number filter function 
#    should take an integer as input and return True if the integer is prime, 
#    and False otherwise. The list_filter function should return a new list 
#    containing only the prime numbers from the original list.
def main():
    length = ask_length()
    number_list = list()
    for i in range(length):
        number_list.append( ask_number(i + 1) )

    print(f"# Original list: {number_list}")
    print(f"# Filtered list: {list_filter(number_list, is_prime)}")


def ask_length():
    while True:
        try:
            length = int ( input("5) Enter the amount of numbers for the list: "))
        except:
            print("Error: non-numeric value.")
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


def is_prime(number):
    if number <= 1:
        return False
    
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def list_filter(original_list, prime):
    return [number for number in original_list if prime(number)]


if __name__ == '__main__':
    main()
