# 1)  Create a program that prints all the even numbers from 0 to 100 using a 
#     for loop.
def main():
    numbers = [number for number in range(0, 101) if number % 2 == 0]
    print("1)", end=" ")
    for i, even_number in enumerate(numbers):
        if i == len(numbers) - 1:
            print(even_number, end=".\n")
        else:
            print(even_number, end=", ")

if __name__ == '__main__':
    main()
