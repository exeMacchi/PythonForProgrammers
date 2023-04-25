# 3) Create a program that asks the user for a word and determines whether it is 
#    a palindrome or not.
def main():
    user_word = input("3) Enter a word: ").strip().lower()
    for i, char in enumerate(reversed(user_word)):
        if char != user_word[i]:
            print("The word is not palindrome.")
            break
        i += 1
    else:
        print("The word is palindrome.")

if __name__ == '__main__':
    main()
