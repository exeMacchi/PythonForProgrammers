# 4) Create a program that prints the first 10 numbers of the Fibonacci series.
def main():
    r1 = 0
    r2 = 1
    r3 = 0
    print("4)", end=" ")
    for i in range(10):
        if i == 9:
            print(r1, end=".\n")
        else:
            print(r1, end=", ")
            r3 = r1 + r2
            r1 = r2
            r2 = r3

if __name__ == "__main__":
    main()
